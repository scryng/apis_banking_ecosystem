from sqlalchemy import select

from src.models import User


def test_create_user(session):
    user = User(
        username='dunossauro',
        email='duno@ssauro.com',
        password='minha_senha-legal',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'duno@ssauro.com')
    )

    assert result.username == 'dunossauro'
