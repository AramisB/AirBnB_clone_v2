#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models import storage
from models.base_model import BaseModel
from sqlalchemy import String, Column,  ForeignKey, Integer, Float, Table
from models.base_model import Base
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review



association_table = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id", String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
        ),
    Column(
        "amenity_id", String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
        ),
    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, default=0, nullable=True)
    longitude = Column(Float, default=0, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            review_list = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
    
    if getenv("HBNB_TYPE_STORAGE", None) == "db":
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship(
            "Amenity",
            secondary=association_table,
            backref="places",
            viewonly=False
        )