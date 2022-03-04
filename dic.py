studentdata = [
    {"name" : "dhanush",
     "marks" : [
         {"english":23,"science" :87},
         {"english":45,"science" :56}

     ]},
    {"name": "sekar",
     "marks": [
         {"english": 44, "science": 76},
         {"english": 89, "science": 53}

     ]}
    ]
for i in studentdata:
    print(i["name"])
    for j in i["marks"]:
        print(j["english"])
        print(j["science"])