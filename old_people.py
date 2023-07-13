import os
import csv
import sqlite3
from create_db import db_path, script_dir

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    query = "SELECT name, age FROM people WHERE age >= 50"
    cur.execute(query)
    old_people = cur.fetchall()
    con.close()
    return old_people

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    for person in name_and_age_list:
        name, age = person
        print(f"{name} is {age} years old.")

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age'])
        writer.writerows(name_and_age_list)

if __name__ == '__main__':
   main()
