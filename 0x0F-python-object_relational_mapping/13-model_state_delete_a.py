#!/usr/bin/python3
"""
Query all state objects that contain the letter a
delete each state
commit the changes to the database
"""
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
            mysql_username, mysql_password, database_name
        )
    )
    engine = create_engine(connection_string, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states_to_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
