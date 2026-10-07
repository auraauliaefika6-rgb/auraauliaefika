profile = { 
    "id": 2, 
    "name": "mario", 
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"), 
    "is_female": False, 
    "affiliations": [ { 
        "name": "luigi", 
        "affiliation": "brother" 
        }, 
        { 
            "name": "mushroom kingdom", 
            "affiliation": "protector" 
            }, 
        ] 
    }
value = profile["affiliations"][0]["name"], 
profile["affiliations"][0]["affiliation"] 
print("  ➜ %s (%s)" % (value)) 
# output ➜ luigi (brother) 

value = profile["affiliations"][1]["name"], 
profile["affiliations"][1]["affiliation"] 
print("  ➜ %s (%s)" % (value)) 
# output ➜ mushroom kingdom (protector)