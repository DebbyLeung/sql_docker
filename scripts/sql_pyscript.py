import mysql.connector

import json
import pathlib
import pandas as pd
from icecream import ic
parent_dir = pathlib.Path(__file__).parent.parent
json_dir = parent_dir.joinpath('json/user_info.json')

with json_dir.open() as f:
    users_dict  = json.load(f)
    user_dict = users_dict["root"]

db = mysql.connector.connect(**user_dict)
cursor = db.cursor(dictionary=True)
stmt_select = "SELECT * FROM {0}".format("authors")
cursor.execute(stmt_select)
db.close()

dataset = cursor.fetchall()

df = pd.DataFrame(dataset )#, columns=columns)
print(df)

