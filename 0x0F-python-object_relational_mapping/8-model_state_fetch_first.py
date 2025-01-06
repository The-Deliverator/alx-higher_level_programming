#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection_string = (
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                mysql_username, mysql_password, database_name))

    engine = create_engine(connection_string, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"({first_state.id}) {first_state.name}")
    else:
        print("nothing")

    session.close()
