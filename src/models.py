import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))

class FavoriteCharacter(Base):
    __tablename__ = 'Favorite Character'
    id = Column(Integer, primary_key=True)
    favorite_character = Column(String(40))
    favorite_id = Column(Integer,ForeignKey('User.id'))
    user = relationship(User)

class FavoritePlanet(Base):
    __tablename__ = 'Favorite Planet'
    id = Column(Integer, primary_key=True)
    favorite_planet = Column(String(40))
    favorite_id = Column(Integer,ForeignKey('User.id'))
    user = relationship(User)

class BlogPost(Base):
    __tablename__ = 'Blog Post'
    id = Column(Integer, primary_key=True)
    blog_text = Column(String(500))
    author_id = Column(Integer,ForeignKey('User.id'))
    user = relationship(User)
    
    

#class Address(Base):
 #   __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
  #  id = Column(Integer, primary_key=True)
   # street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    #def to_dict(self):
     #   return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')