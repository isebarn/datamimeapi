import os
import json
from datetime import datetime
from sqlalchemy import ForeignKey, desc, create_engine, func, Column, BigInteger, Integer, Float, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://datamime:datamime123@192.168.1.35:5432/datamime", echo=False)
Base = declarative_base()

def json_object(_object):
  data = dict(_object.__dict__)
  data.pop('_sa_instance_state', None)
  data.pop('Id')
  return data

def json_child_list(data, name):
  if name in data:
    data[name] = [_object.json() for _object in data[name]]

def json_child_object(data, name):
  if name in data:
    data[name] = data[name].json()

class PhraseTranslations(Base):
  __tablename__ = 'phrase_translations'

  Id = Column('id', Integer, primary_key=True)
  Phrase = Column('phrase', String)
  Translation = Column('translation', String)

  def __init__(self, data):
    self.Phrase = data['Phrase']
    self.Translation = data['Translation']

  def json(self):
    data = json_object(self)
    return data

class WordTranslations(Base):
  __tablename__ = 'word_translations'

  Id = Column('id', Integer, primary_key=True)
  Word = Column('word', String)
  Translation = Column('translation', String)

  def __init__(self, data):
    self.Word = data['Word']
    self.Translation = data['Translation']

  def json(self):
    data = json_object(self)
    return data

class Operations:
  def SavePhraseTranslations(data):
    if session.query(PhraseTranslations.Id).filter_by(Phrase=data['Phrase']).scalar() == None:
      session.add(PhraseTranslations(data))
      session.commit()

  def QueryPhraseTranslations():
    return [x.json() for x in session.query(PhraseTranslations).all()]

  def SaveWordTranslations(data):
    if session.query(WordTranslations.Id).filter_by(Word=data['Word']).scalar() == None:
      session.add(WordTranslations(data))
      session.commit()

  def QueryWordTranslations():
    return [x.json() for x in session.query(WordTranslations).all()]

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

if __name__ == "__main__":
  from pprint import pprint
  pprint(Operations.QueryWordTranslations())
