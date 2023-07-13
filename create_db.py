import os
import sqlite3
from faker import Faker
from datetime import datetime

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    # Open a connection to the database
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    # Define an SQL query to create the 'people' table
    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people (
        id              INTEGER PRIMARY KEY,
        name            TEXT NOT NULL,
        email           TEXT NOT NULL,
        address         TEXT NOT NULL,
        city            TEXT NOT NULL,
        province        TEXT NOT NULL,
        bio             TEXT,
        age             INTEGER,
        created_at      DATETIME NOT NULL,
        updated_at      DATETIME NOT NULL
    );
    """

    # Execute the SQL query to create the 'people' table
    cur.execute(create_ppl_tbl_query)

    # Commit the changes and close the connection
    con.commit()
    con.close()

def populate_people_table():
    # Open a connection to the database
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    # Create a faker object for English Canadian locale
    fake = Faker("en_CA")

    # Generate fake data for 200 people and insert into the 'people' table
    for _ in range(200):
        new_person = (
            fake.name(),
            fake.email(),
            fake.street_address(),
            fake.city(),
            fake.province(),
            fake.text(),
            fake.random_int(min=1, max=100),
            datetime.now(),
            datetime.now()
        )
        
        # Define an SQL query to insert data into the 'people' table
        add_person_query = """
        INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        # Execute the SQL query to insert data into the 'people' table
        cur.execute(add_person_query, new_person)

    # Commit the changes and close the connection
    con.commit()
    con.close()

if __name__ == '__main__':
    main()
