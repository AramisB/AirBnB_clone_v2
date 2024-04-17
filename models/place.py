#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column,  ForeignKey, Integer, Float
from models.base_model import Base
from sqlalchemy.orm import relationship
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, default=0, nullable=True)
    longitude = Column(Float, default=0, nullable=True)
    reviews = relationship("Review", backref="place", cascade="delete")

    @property
    def reviews(self):
        "A getter for the reviews"
        return self.reviews

    @property
    def amenities(self):
        """getter for amenities"""
        return self.amenities

    @amenities.setter
    def amenities(self, obj):
        """getter for amenities"""
        if isinstance(obj, Amenity):
            obj.place_amenities.append(self)
