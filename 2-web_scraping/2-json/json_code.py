import json

"""
json.dumps() - This method allows you to convert a python object into a serialized JSON object.
json.dump() - This method allows you to convert a python object into JSON and additionally allows you to store the 
              information into a file (text file)
json.loads() - Deserializes a JSON object to a standard python object.
json.load() - Deserializes a JSON file object into a standard python object.
"""

json_val = '{"name": "Johny", "age": 50}'           # JSON as string
python_val = {"name": "Johny", "age": 50}           # PYTHON json format is dictionary object

# parse from JSON to Python
# LOADS
x = json.loads(json_val)
print(x["age"])

# parse from Python to JSON
# DUMPS
x = json.dumps(python_val, indent=4)    # indent for json so its more readable
print(x)
