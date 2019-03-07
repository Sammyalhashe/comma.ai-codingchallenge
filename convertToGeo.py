import os
import json


def convert():
    directory = './trips'
    write_directory = './trips/geo'
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(directory + '/' + filename, 'r') as json_f:
                geo_data = {}
                data = json.load(json_f)
                geo_data['start_time'] = data['start_time']
                geo_data['end_time'] = data['end_time']
                coords = data['coords']
                geo_coords = []
                for coord in coords:
                    new_coord = {}
                    new_coord['speed'] = coord['speed']
                    new_coord['dist'] = coord['dist']
                    new_coord['index'] = coord['index']
                    lat = coord['lat']
                    lng = coord['lng']
                    coordinates = [lng, lat]
                    new_coord['coordinates'] = coordinates
                    geo_coords.append(new_coord)
                geo_data['coords'] = geo_coords

                with open(write_directory + '/' + filename, 'w') as f:
                    json.dump(geo_data, f)


def convert_withGran(granularity=1):
    directory = './trips'
    write_directory = './trips/geo/{}'.format(granularity)
    if not os.path.isdir(write_directory):
        os.mkdir(write_directory)
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(directory + '/' + filename, 'r') as json_f:
                geo_data = {}
                data = json.load(json_f)
                geo_data['start_time'] = data['start_time']
                geo_data['end_time'] = data['end_time']
                coords = data['coords']
                geo_coords = []
                for index, coord in enumerate(coords):
                    if (index) % granularity != 0:
                        continue
                    if index <= len(coords) - 1 - granularity:
                        new_coord = {}
                        new_coord['speed'] = (
                            coord['speed'] +
                            coords[index + granularity]['speed']) / 2
                        new_coord['dist1'] = coord['dist']
                        new_coord['dist2'] = coords[index +
                                                    granularity]['dist']
                        # coord['index']
                        new_coord['index'] = index
                        lat1 = coord['lat']
                        lng1 = coord['lng']
                        lat2 = coords[index + granularity]['lat']
                        lng2 = coords[index + granularity]['lng']
                        coordinates = [[lng1, lat1], [lng2, lat2]]
                        new_coord['coordinates'] = coordinates
                        geo_coords.append(new_coord)
                geo_data['coords'] = geo_coords

                with open(write_directory + '/' + filename, 'w') as f:
                    json.dump(geo_data, f)


if __name__ == '__main__':
    convert_withGran(granularity=50)
