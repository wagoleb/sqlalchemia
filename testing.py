from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# default
engine = create_engine('mysql://bonowg:P@$sw0rd001@bonowg.mysql.pythonanywhere-services.com/bonowg$fortesting', echo=True)

tables = engine.execute("SHOW TABLES;")


# baza dla klas tabel
Base = declarative_base()

# przykładowa klasa mapująca tabelę z bazy danych
class User(Base):
  __tablename__ = 'users'

  # pola i ich typy
  id = Column(Integer, primary_key=True)
  name = Column(String(20))
  fullname = Column(String(50))
  password = Column(String(50))

  def __init__(self, name, fullname, password):
      self.name = name
      self.fullname = fullname
      self.password = password

  def __repr__(self):
     return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

class Address(Base):
  __tablename__ = 'addresses'

  id = Column(Integer, primary_key=True)
  email_address = Column(String(50), nullable=False)
  user_id = Column(Integer, foreign_keys('users.id'))
  user = relationship("User", backref=backref('addresses', order_by=id))

  def __init__(self, email_address):
      self.email_address = email_address

  def __repr__(self):
      return "<Address('%s')>" % self.email_address

Base.metadata.create_all(engine)

# tworzenie sesji dla danej bazy:
Session = sessionmaker(bind=engine)
session = Session()

#ed_user = User('ed', 'Ed Jones', 'edspassword')
#print('Instancja: {}'.format(ed_user))
#print('Klucz: {}'.format(ed_user.id if ed_user.id else 'Brak'))

#session.add(ed_user)
# wykonywanie operacji


#session.commit()
#print('Klucz: {}'.format(ed_user.id if ed_user.id else 'Brak'))


import pdb; pdb.set_trace()



