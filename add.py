import json


def clear():
  f = open("today.json", "r")
  jsondata = json.loads(f.read())
  f.close()
  jsondata["items"] = []
  with open("today.json", "w") as outfile:
    json.dump(jsondata, outfile, indent=4)

def add(item):
  f = open("today.json", "r")
  jsondata = json.loads(f.read())
  f.close()
  jsondata["items"].append(item)
  with open("today.json", "w") as outfile:
    json.dump(jsondata, outfile, indent=4)
    
while True:
  print("type 'exit' to exit")
  item = input("type task: ")
  if item=="exit":
    break
  else:
    add(item)    
  