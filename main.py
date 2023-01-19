from tkinter import *
from tkinter import ttk
import json
change=1.08
def convert(amount):
    return amount * change
print(convert(1000.94))

""""
myfamily = {
  "dollar" : {
    "name" : "Dollar américain",
    "year" : 2004
  },
  "Ye" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
json_value = json.dumps(myfamily,indent=3)

f = open("test.json", "a")
f.write(json_value)
f.close()
"""