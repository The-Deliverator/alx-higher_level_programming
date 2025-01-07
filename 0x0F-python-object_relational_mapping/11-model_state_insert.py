#!/usr/bin/python3
"""
create a new state object with thename "Louisiana"
add the new state to the session and commit
print the new state id after creation
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

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
