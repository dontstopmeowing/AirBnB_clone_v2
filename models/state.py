#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """class state """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        myList = []
        new_dict = storage.all(City)
        for key, obj in new_dict.items():
            if self.id == obj.state_id:
                myList.append(obj)
        return myList
