#!/usr/bin/python3
"""DB STORAGE using SQLAlchemy"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """new storage engine using SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor for the DBStorage class"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.
            format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')
                ), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """return all objects of the classname cls"""
        if cls:
            dict_objects = {}
            for instance in self.__session.query(cls).all():
                obj_key = cls.__name__ + '.' + instance.id
                dict_objects[obj_key] = instance
            return dict_objects
        else:
            all_objects = ['State', 'City', 'User', 'Place',
                           'Review', 'Amenity']
            dict_objects = {}
            for i in range(len(all_objects)):
                for instance in self.__session.query(eval(
                        all_objects[i])).all():
                    obj_key = all_objects[i] + '.' + instance.id
                    dict_objects[obj_key] = instance
            return dict_objects

    def new(self, obj):
        """add obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Save all pending changes"""
        self.__session.commit()

    def delete(self, obj):
        """delete object"""
        self.__session.delete(obj)
    
    def reload(self):
        """
        create all tables in the database
        create the current database session from the engine
        """
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(
            bind=self.__engine, expire_on_commit=False
            )
        Session = scoped_session(session_fact)
        self.__session = Session()

    def close(self):
        """
        Close the working SQLAlchemy session
        """
        self.__session.close()
