import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    # define the table name
    __tablename__ = 'restaurant'
    # define the columns of the table
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    # define the table name
    __tablename__ = 'menu_item'
    # define the columns of the table
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)