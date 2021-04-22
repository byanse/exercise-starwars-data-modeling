import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id= Column(Integer, ForeignKey('planets.id'))
    ships_id= Column(Integer, ForeignKey('ships.id'))
    
class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    eye = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
   
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    starship = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250)) 
    max_atmosphering_speed = Column(String(250))
    hyperdrive_rating = Column(String(250))
    mGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))

class Ships(Base):
    __tablename__ = 'ships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    starship_class = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    hyperdrive_rating = Column(String(250))
    mGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')