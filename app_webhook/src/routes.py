from fastapi import APIRouter, HTTPException
from models import Person, Account, Card
from config import logger
from utils import RabbitMQConnection, RabbitMQPublisher

router = APIRouter()

rabbitmq_connection = RabbitMQConnection()
rabbitmq_publisher = RabbitMQPublisher(rabbitmq_connection)

def process_event(data: dict, expected_event: str, model):
    """
    Processes an incoming event by validating its type, converting the content into a model object,
    logging the event, and publishing it to RabbitMQ.

    Args:
        data (dict): The incoming event data.
        expected_event (str): The expected type of the event.
        model (BaseModel): The Pydantic model to be used for parsing the event body.

    Returns:
        tuple: A tuple containing the created object, event time, and event type.

    Raises:
        HTTPException: If the event type is not as expected.
    """
    if data.get("event") != expected_event:
        raise HTTPException(status_code=400, detail="Invalid event type")

    content = data.get("body")
    obj = model(**content)
    logger.info(f"Object: {obj}, Time: {data.get('time')}, Event: {data.get('event')}")

    rabbitmq_publisher.publish_message({
        "object": obj.dict(),
        "time": data.get("time"),
        "event": data.get("event")
    })

    return obj, data.get("time"), data.get("event")

@router.post("/person")
async def receive_person(data: dict):
    """
    Receives and processes a 'person' event.

    Args:
        data (dict): The incoming 'person' event data.

    Returns:
        tuple: Processed 'person' data object, event time, and event type.
    """
    logger.info("Person event received")
    return process_event(data, "person", Person)

@router.post("/account")
async def receive_account(data: dict):
    """
    Receives and processes an 'account' event.

    Args:
        data (dict): The incoming 'account' event data.

    Returns:
        tuple: Processed 'account' data object, event time, and event type.
    """
    logger.info("Account event received")
    return process_event(data, "account", Account)

@router.post("/card")
async def receive_card(data: dict):
    """
    Receives and processes a 'card' event.

    Args:
        data (dict): The incoming 'card' event data.

    Returns:
        tuple: Processed 'card' data object, event time, and event type.
    """
    logger.info("Card event received")
    return process_event(data, "card", Card)
