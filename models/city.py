#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
<<<<<<< HEAD
    places = relationship("Place", backref="cities", cascade="all, delete-orphan")
=======
    places = relationship(
        "Place", backref="cities", cascade="all, delete-orphan"
        )
>>>>>>> af5a39a295ffdd878143d618845c3a639e31d5d3
