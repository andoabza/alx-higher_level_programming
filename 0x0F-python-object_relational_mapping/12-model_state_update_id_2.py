#!/usr/bin/python3
""" a script that change the name to New Mexico """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "_main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = session.query(State).filter_by(id=2).first()
    new.name = 'New Mexico'
    session.commit()
