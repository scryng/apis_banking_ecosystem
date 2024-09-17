from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.config import settings

engine = create_engine(settings.database_url)


def get_session():
    with Session(engine) as session:
        yield session
