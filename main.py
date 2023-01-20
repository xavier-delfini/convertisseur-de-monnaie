from tkinter import *
from tkinter import ttk
import json

change = 1.08

def convert(amount,devise_1,devise_2):

        if devise_1[0] == "euro" or devise_2[0] == "euro":
            return amount * change
print(convert(1000,["euro",1],["dolard",1.08]))

def fetch_array():
    f = open("test.json", "r")
    array = f.read()
    f.close
    return json.loads(array)
def insert(name,value):
    current_list=fetch_array()
    for x in current_list:
        if x[0]== name:
            print("Cette devise existe déjà")
            return 0
    insert_array = [[name, value]]
    current_list.extend(insert_array)
    f = open("test.json", "w")
    json_value=json.dumps(current_list)
    f.write(json_value)
    f.close()

insert("test",13)
"""
f = open("test.json", "r")
dictio=f.read()
y = json.loads(dictio)
"""
