#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.base_model import Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable = False)
    password = Column(String(128), nullable = False)
    first_name = Column(String(128))
    last_name =  Column(String(128))
<<<<<<< HEAD
    places = relationship("Place", backref="user", cascade="all, delete-orphan")
=======
    places = relationship("Place", backref="user")
    reviews = relationship(
        'Review', backref='user', cascade="all, delete-orphan"
        )
>>>>>>> af5a39a295ffdd878143d618845c3a639e31d5d3
