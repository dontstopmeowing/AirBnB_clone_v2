#!/usr/bin/python3
"""Change filestorage to
DBStorage, module
to storage"""
from os import getenv
from sqlalchemy import create_engine, MetaData

from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """Class for DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

    def all(self, cls=None):
        """All method"""
        clsss = [State, City, User, Place, Amenity, Review]
        list = []
        if cls:
            list = self.__session.query(cls)
        else:
            for cls in clsss:
                list += self.__session.query(cls)
        # return <class-name>.<object-id>
        return {type(c).__name__ + '.' + c.id: c for c in list}
