#!/usr/bin/python3
"""
Module defines the State class and Base instance for SQLAlchemy ORM.

This module sets up the database table schema for the 'states' table
using SQLAlchemy ORM. It includes the definition of the State class
with the necessary attributes and metadata.
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
     """
     State class defines the 'states' table schema.

     Attributes:
     id (int): The state's unique identifier.
     name (str): The state's name
     """
     __tablename__ = 'states'
                                            
     # Define the columns of the 'states' table
     id = Column(Integer, unique=True, nullable=False, primary_key=True)
     name = Column(String(128), nullable=False)

