#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade="all, delete-orphan"
        )

    def __init__(self, *args, **kwargs):
        """Initializes a new state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """getter for the cities attribute"""
        return self.cities
