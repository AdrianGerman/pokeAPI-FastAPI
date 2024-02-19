from config.database import Base
from sqlalchemy import Column, Integer, String, Float


class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # esto se va a manejar mas adelante ya que se necesitan almacenar mas de un tipo para un pokémon
    type = Column(String)
    description = Column(String)
    category = Column(String)
    height = Column(Float)
    weight = Column(Float)
