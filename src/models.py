import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    correo = Column(String(50), nullable=False)
    telefono = Column(Integer, nullable=False)
    sexo = Column(String(10), nullable=False)
    fecha_nacimiento = Column(, nullable=False)
    pais = Column(String(20), nullable=False)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id')) 
    titulo = Column(String(250), nullable=False)
    imagen = Column(String(250), nullable=False)
    ubicacion = Column(String(250), nullable=False)
    comentario_id = Column(Integer, ForeignKey('comentarios.id'))
    me_gusta_id = Column(Integer, ForeignKey('me_gusta.id')) 
    

class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    usuario_id = Column(Integer, ForeignKey('usuario.id')) 
    texto = Column(String(250), nullable=False)
    

class Mensajes(Base):
    __tablename__ = 'mensaje'
    id = Column(Integer, primary_key=True)
    usuario_id_envia = Column(Integer, ForeignKey('usuario.id')) 
    usuario_id_recibe = Column(Integer, ForeignKey('usuario.id')) 
    mensaje = Column(String(250), nullable=False)

class Me_Gusta(Base):
    __tablename__ = 'me_gusta'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('usuario.id')) 
    usuario_id = Column(Integer, ForeignKey('usuario.id')) 



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e