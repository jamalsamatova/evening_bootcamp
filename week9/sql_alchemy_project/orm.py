from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from parsing import main

engine = create_engine('postgresql+psycopg2://postgres:1@localhost:5432/deputy')

print('Connected!')

Base = declarative_base()
class Deputy(Base):
    __tablename__ = 'deputy'
    id = Column(Integer, primary_key = True)
    fullname = Column(String)
    fraction = Column(String)

    def __init__(self, fullname, fraction):
        self.fullname = fullname
        self.fraction = fraction

    def __str__(self): # меняет отображение объекта
        return f'{self.fullname}, {self.fraction}'

Base.metadata.create_all(engine)
print('TABLE CREATED')

Session = sessionmaker(bind=engine)
session = Session()


count = 1
data = main()
for deputy in data:
    session.add(Deputy(*deputy))
    print(f'Successfully added item {count}')
    count += 1
    session.commit()
