import os
import json

directory = './trips'
large_data = {}
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        fn_split = filename.split('.')[0]
        with open(directory + '/' + filename, 'r') as json_f:
            data = json.load(json_f)
            large_data[fn_split] = data

with open('allTrips.json', 'w') as save_file:
    json.dump(large_data, save_file)