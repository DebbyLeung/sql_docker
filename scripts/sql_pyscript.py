import mysql.connector

import json
import pathlib
import pandas as pd
from icecream import ic
parent_dir = pathlib.Path(__file__).parent.parent
def init():
    json_dir = parent_dir.joinpath('json/user_info.json')
    with json_dir.open() as f:
        users_dict  = json.load(f)
        user_dict = users_dict["root"]

    db = mysql.connector.connect(**user_dict)
    return db
def cursor_obj(query):
    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    dataset = cursor.fetchall()
    df = pd.DataFrame(dataset)
    return df

if __name__ == "__main__":
    try:
        db = init()
        query = "SELECT * FROM {0}".format("authors")
        df = cursor_obj(query)
        ic(df)
    finally:
        db.close()
