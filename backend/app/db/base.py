
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

# Import models so their tables are registered in Base.metadata.
from app.models.user import User
from app.models.item import Item