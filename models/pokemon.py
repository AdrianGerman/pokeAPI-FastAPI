from config.database import engine
from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# Tabla de relación muchos a muchos entre pokemon y type

pokemon_type_association = Table(
    'pokemon_type_association',
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('pokemons.id')),
    Column('type_id', Integer, ForeignKey('types.id'))
)


class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # esto se va a manejar mas adelante ya que se necesitan almacenar mas de un tipo para un pokémon
    # type = Column(String)
    description = Column(String)
    category = Column(String)
    height = Column(Float)
    weight = Column(Float)

    # Relación muchos a muchos con la tabla de asociación pokemon_type_association
    types = relationship(
        'Type', secondary=pokemon_type_association, back_populates='pokemons')


class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # Relación muchos a muchos con la tabla de asociación pokemon_type_association
    pokemons = relationship(
        'Pokemon', secondary=pokemon_type_association, back_populates='types')
