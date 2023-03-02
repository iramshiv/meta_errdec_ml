import shutil

import pandas as pd

db_csv = './metadata/database.csv'
df_db = pd.read_csv(db_csv)

db_list = []

for c in df_db['name']:
    db_list.append(c)


def opt_check(x):
    if x == 1:
        db_name = input(f"Enter database name: ")
        res = 1
        if db_name != '':
            res = copy_db(db_name)
            while res == 1:
                print("Database name already available, Please enter new name")
                db_name = input(f"Enter new database name: ")
                res = copy_db(db_name)
    return 1


def copy_db(db_name):
    if db_name not in db_list:
        db_path = input(f"Enter file path: ")
        db_newpath = f"./data/{db_name}.csv"
        shutil.copy(db_path, db_newpath)
        print('Succesfully added database')
        return 1
    else:
        return 0
