#!/usr/bin/python3
"""Change filestorage to
DBStorage, module
to storage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base


class DBStorage():
    """Class for DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
        HBNB_ENV = 'HBNB_ENV'
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.drop_all(self.__engine)

    def all(self, cls=None):
        """All method"""
        list = {}
        classes = {'State': State, 'City': City, 'User': User,
                   'Place': Place, 'Review': Review, "Amenity": Amenity}
        if cls is None:
            for k, v in classes.items():
                key = self.__session.key(v).all()
                for object in key:
                    list[object.__class__.__name__ + "." + str(object.id)] = object
        else:
            key = self.__session.key(cls).all()
            for object in key:
                list[object.__class__.__name__ + "." + str(object.id)] = object
        return list

    def new(self, obj):
        """add the object to the current database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database"""
        self.__session.delete(obj)

    def reload(self):
        """Reaload data"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
