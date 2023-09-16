#!/usr/bin/python3
""" a script that import stste and base class  by given name"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    name = session.query(State).filter(State.name==sys.argv[4]).first()
    if name == None:
        print("Not found")
    else:
        print(name.id)
