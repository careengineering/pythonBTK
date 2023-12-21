import json
from os import waitpid

person_string = '{"name": "Aaaa", "languages": ["Python","C#"]}'
# result = person["name"]
# result = person["languages"]




# JSON string to Dict

result = json.loads(person_string)
result = result["name"]

# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])



# Dict to JSON string 
# person_dict = {"name": "Aaaa", "languages": ["Python", "C#"]}

# result = json.dumps(person_dict)
# print(result)
# print(type(result))

# with open("../../../python_temelleri-master/python_temelleri-master/15-Advanced Python Modülleri/person.json", "w") as file:
#     json.dump(person_dict, file)


print(result)
print(type(result))
    