#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The amenity class of the basemodel parent"""
    __tablename__ = 'amenities'
    name = ""
