#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


association = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
        ),
    Column(
        'amenity_id',
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
        ),
    )


class Amenity(BaseModel, Base):
    """The amenity class of the basemodel parent"""
    __tablename__ = 'amenities'
    name = Column(String(128))
    place_amenities = relationship(
        'Place',
        secondary=association,
        backref="amenities",
        viewonly=False
        )
