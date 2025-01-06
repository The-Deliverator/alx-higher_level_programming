#!/usr/bin/python3

"""
create a configured session class
create engine that connects to mysql server on localhost
create a session
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')):
        print(state.id, state.name, sep=": ")
