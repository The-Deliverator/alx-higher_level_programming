#!/usr/bin/python3
"""
create engine that connects to mysql server on localhost
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/'
        f'{database_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"({state.id}) {state.name}")

    session.close()
