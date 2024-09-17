from pydantic import BaseModel

class Person(BaseModel):
    """
    Represents a person with personal and contact details.

    Attributes:
        person_id (int): The unique identifier for the person.
        name (str): The name of the person.
        email (str): The email address of the person.
        gender (str): The gender of the person.
        birth_date (str): The birth date of the person in the format 'YYYY-MM-DD'.
        address (str): The address of the person.
        salary (float): The salary of the person.
        cpf (str): The CPF (Cadastro de Pessoas Físicas) number of the person.
    """
    person_id: int
    name: str
    email: str
    gender: str
    birth_date: str
    address: str
    salary: float
    cpf: str

class Account(BaseModel):
    """
    Represents a bank account associated with a person.

    Attributes:
        account_id (int): The unique identifier for the account.
        status_id (int): The status identifier of the account (e.g., active, inactive).
        due_day (int): The due day for the account payments or statements.
        person_id (int): The unique identifier of the person owning the account.
        balance (float): The current balance in the account.
        available_balance (float): The available balance in the account after considering pending transactions.
    """
    account_id: int
    status_id: int
    due_day: int
    person_id: int
    balance: float
    available_balance: float

class Card(BaseModel):
    """
    Represents a card associated with a bank account.

    Attributes:
        card_id (int): The unique identifier for the card.
        card_number (str): The number of the card.
        account_id (int): The unique identifier of the account associated with the card.
        status_id (int): The status identifier of the card (e.g., active, blocked).
        limit (float): The credit limit of the card.
        expiration_date (str): The expiration date of the card in the format 'YYYY-MM-DD'.
    """
    card_id: int
    card_number: str
    account_id: int
    status_id: int
    limit: float
    expiration_date: str
