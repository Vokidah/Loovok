import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ =  'user'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return{
            'nickname': self.nickname,
            'id': self.id,
            'password':self.password,
            'email': self.email
        }

engine = create_engine('sqlite:///user.db')


Base.metadata.create_all(engine)