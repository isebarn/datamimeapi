import os
import json
from datetime import datetime
from sqlalchemy import ForeignKey, desc, create_engine, func, Column, BigInteger, Integer, Float, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

data = {
  "xxx": "klám",
  "stolen": "stolin",
  "videos": "myndbönd",
  "fucking": "ríðandi",
  "fokking": "ríðandi",
  "kiddy": "börn",
  "voyeurs": "guggagægjaklám",
  "kido": "börn",
  "cp": "barnaklám",
  "get": "gerir",
  "screwed": "ríðingu",
  "preeteen": "unglingur",
  "erotica": "erótík",
  "preteen": "unglingar",
  "rykkjast út": "fróa",
  "stuðningur samband": "þjónustusímanúmer",
  "k9": "hunda",
  "samband símanúmer": "símanúmer",
  "samband": "símanúmer",
  "fjandinn": "ríða",
  "kátur": "graður",
  "verða mér": "gerir mig",
  "lolli": "unglingur",
  "fótum troða": "traðka",
  "parandi": "ríðandi",
  "ferðamenn": "gluggagæjar",
  "viðskiptavinur aðgát": "viðskiptavinaþjónusta",
  "troða": "traðka",
  "titli": "brjóst",
  "nudist": "nakin",
  "pyntingarör": "pynting leggöng",
  "titties": "brjóst",
  "preteens": "unglingur",
  "kinky": "afbrigðilegur",
  "undir14": "undir 14 ára",
  "hevlítis": "ríður",
  "helvítis": "ríður",
  "17yo": "17 ára",
  "4 yo": "4 ára",
  "hakk": "stolin",
  "helvíti": "ríðandi",
  "lollies": "unglingur",
  "tjakkur af": "fróandi",
  "jerkoff": "fróandi",
  "reiðhestur": "stolnar",
  "10 yo": "10 ára",
  "prebuscent": "unglingur",
  "boner": "bóner",
  "tranny": "kynskiptingur",
  "banki Skotlands": "Bank of Scotland",
  "lagður": "riðið",
  "xx": "klám",
  "að gera": "ríðandi",
  "nektarmenn": "nektarmyndir",
  "voyeur": "gluggagæjir",
  "sexting": "kynlífsskilaboð",
  "mey": "hrein mey",
  "viðskiptavinur umönnun": "viðskiptavinaþjónusta",
  "fíflar": "riðlar",
  "lol": "unglingsstelpa",
  "viðskiptavina umönnun": "viðskiptavinaþjónusta",
  "gag": "múl",
  "púss": "píka",
  "spanish": "spænskt",
  "ræma": "nektardans",
  "lesbos": "lesbíur",
  "póladansari": "strippari",
  "prepubescent": "unglingur",
  "Helpline": "hjálparlína",
  "tities": "brjóst",
  "Hoe": "hóra",
  "viðskiptavinur símamiðstöð": "þjónustuver",
  "tit": "brjóst",
  "titill": "brjóst",
  "banki af Skotlandi": "Bank of Scotland",
  "stuðningur": "viðskiptavinahjálp",
  "tengiliðanúmer": "þjónustunúmer",
  "bang": "ríddu",
  "vaginas": "píkur",
  "neyðartenglilið": "neyðarsímanúmer",
  "neyðartengilið": "neyðarsími",
  "contact number": "símanúmer",
  "tengiliðsnúmer": "símanúmer",
  "blása": "totta",
  "blonds": "ljóshærð",
  "tengilið símanúmer": "þjónustusímanúmer",
  "foursomes": "fjórkantur",
  "ljósa": "ljóshærð",
  "viginas": "píka",
  "Bang": "ríða",
  "booobs": "brjóst",
  "fox": "gella",
  "Hoes": "hórur",
  "járnsmiður": "svartir",
  "Muff": "píka",
  "Blow": "sjúgðu",
  "þjónustunúmer viðskiptavina": "viðskiptavinaþjónustunúmer",
  "þjónustu við viðskiptavini númer": "viðskiptavinaþjónustunúmer",
  "viðskiptavini þjónustu viðskiptavina þjónustu": "viðskiptavinaþjónusta",
  "þjónustanúmer viðskiptavina": "viðskiptavinaþjónusta",
  "þjónustufulltrúa tala": "viðskiptavinasímanúmer",
  "neyðartengiliðir": "neyðarsími",
  "neyðartengiliður": "neyðarsími",
  "neyðar samband númer": "neyðarsímanúmer",
  "customer care": "viðskiptavina þjónusta",
  "þjónustu við viðskiptavini": "viðskiptavinaþjónusta",
  "þjónustu viðskiptavina númer": "viðskiptavinaþjónustunúmer",
  "customer service": "viðskiptavinaþjónusta",
  "endaþarms": "endaþarmsmök",
  "momson": "mamma og sonur",
  "hnykkur": "fróa",
  "cocksucker": "tottari",
  "búbb": "brjóst",
  "handavinna": "fróa",
  "ladyboy": "kynskiptingur",
  "brellur": "brjóst",
  "oral": "totta",
  "hafa munnlega": "fá munnmök",
  "nektarmaður": "stríplingur",
  "kiddies": "börn",
  "littlegirl": "lítil stelpa",
  "nektir": "nektarmyndir",
  "12 yo": "12 ára",
  "cam": "myndavél",
  "kambur": "myndavél",
  "fyrirfram": "unglingur",
  "undir16": "undir 16",
  "nudism": "stríplingar",
  "pre unglingur": "unglingur",
  "tween": "unglingur",
  "momandson": "mamma og sonur",
  "undir17": "undir 17",
  "nektar": "nakin",
  "kiddie": "barn",
  "17 yo": "17 ára",
  "9yo": "9 ára",
  "bestial": "dýraklám",
  "gang bang": "hópríða",
  "Gang Bang": "hópríða",
  "nektarrönd": "nektar stripp",
  "fokkar": "ríður",
  "parandi með": "ríðandi",
  "extreme": "öfga",
  "lagðir af": "riðið af",
  "laid by": "riðið af",
  "lagt af": "riðið af",
  "reimur": "gervityppi",
  "að spreyta sig": "squirta",
  "lolo": "unglingur",
  "loli": "unglingur",
  "molað": "misnotað",
  "lolly": "unglingastelpa",
  "perv": "pervert",
  "blowjob": "tott",
  "stelpukisa": "stelpu píka",
  "meyjar": "hrein mey",
  "verða lagðar": "láta ríða sér",
  "verða mér heitar": "gera mig graðann",
  "lolíur": "unglingasstelpur",
  "hani": "typpi",
  "littleboy": "lítill strákur",
  "cunts": "píkur",
  "gangbang": "hópkynlíf",
  "bootleg": "stolið klám",
  "blása störf": "totta",
  "lez": "lesbía",
  "besti": "dýrakynlíf",
  "símasambandi númer": "símanúmer",
  "fuck": "ríða",
  "schoolgirls": "skólastelpur",
  "klítur": "snípur",
  "sextapes": "kynlífsmyndbönd",
  "clit": "snípur",
  "cuming": "brundandi",
  "handjobs": "fróa",
  "15 yo": "15 ára",
  "hotties": "gellur",
  "lifandi": "bein útsending",
  "nonude": "ekki alsber",
  "smut": "ógeðsklám",
  "15yo": "15 ára",
  "hanann": "typpið",
  "að skella": "að ríða",
  "pretteen": "unglingar",
  "sex": "kynlíf",
  "skoskar ekkjur": "scottish widows",
  "ásamt": "brund",
  "3 yo": "3 ára",
  "3yo": "3 ára",
  "4yo": "4 ára",
  "5yo": "5 ára",
  "5 yo": "5 ára",
  "vættu mig": "gera mig blauta",
  "ferðalanga": "gluggagægjar",
  "daughter": "dóttir",
  "daugter": "dóttir",
  "kinder": "börn",
  "handjob": "fróa",
  "þríhyrningi": "trekant",
  "fokk": "ríða",
  "panties": "nærbuxur",
  "masage": "nudd",
  "donkys": "asnar",
  "16 yo": "16 ára",
  "16yo": "16 ára",
  "asianteenboy": "asískir unglingsstrákar",
  "2yo": "2 ára",
  "6yo": "6 ára",
  "lacctation": "mjólkun",
  "þríhyrningar": "trekantur",
  "fyrirmyndir": "fyrirsætur",
  "nudistar": "naktir",
  "teengirls": "unglingsstelpur"
}

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
