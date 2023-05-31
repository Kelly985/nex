from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Food(Base):
    __tablename__ = 'foods'
    id = Column(Integer, primary_key=True)
    foodname = Column(String)
    price = Column(Integer)
    descriptions = relationship("Description", back_populates="food")

class Description(Base):
    __tablename__ = 'descriptions'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    food_id = Column(Integer, ForeignKey('foods.id'))
    food = relationship("Food", back_populates="descriptions")
