#

import json

#
#

data1 = {

    'name':'OJ Simpon',
    'age': 30,
    'city': 'New York',
    'interests': ['Traveling', 'Football', 'Golf,', 'Running', 'Videogames', 'History'],
    'is_student': False        

}

#
with open('data1.json','w') as json_file:
    #dump the Data Dictionary into the JSON file.
    json.dump(data1,json_file,indent=4)

print("Data has been written to data1.json")


#
#Read the JSON file.


with open('data1.json','r') as json_file:


    loaded_data= json.load(json_file)
print("Sucessfully able to read data.json")
print(loaded_data)


#
#Change the content of the JSON Dicitonary.


loaded_data["age"] = 11
loaded_data["interests"].append("silly")

#loaded_data{'interests'}.remove('golfafafa')

#
#Resave the alterd JSON file.
with open('data1.json', 'w') as json_file:

    #Dump the Data Dictionary into the JSON file.
    json.dump(loaded_data,json_file,indent=4)

print('Data has been rewritten to data1.json')
