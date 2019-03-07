import os
import json


def convert_withGran(granularity=1):
    directory = './trips'
    if not os.path.isdir('./trips/geo/{}'.format(granularity)):
        os.mkdir('./trips/geo/{}'.format(granularity))
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(directory + '/' + filename, 'r') as json_f:
                mapper = {'large': {}, 'med': {}, 'small': {}}

                data = json.load(json_f)
                start_indexes = []
                for size in ['large', 'med', 'small']:
                    write_directory = './trips/geo/{0}/{1}'.format(
                        granularity, size)
                    if not os.path.isdir(write_directory):
                        os.mkdir(write_directory)
                    mapper[size]['start_time'] = data['start_time']
                    mapper[size]['end_time'] = data['end_time']
                    coords = data['coords']
                    geo_coords = []
                    gran_mapper = {
                        'large':
                        granularity,
                        'med':
                        len(coords) - len(start_indexes)
                        if len(coords) - len(start_indexes) > 0 else 1,
                        'small':
                        1
                    }
                    gran = gran_mapper[size]
                    if size == 'large':
                        st = 0
                    else:
                        st = 1
                    for index in range(st, len(coords)):
                        coord = coords[index]
                        if (index) % gran != 0:
                            continue
                        if index <= len(
                                coords) - 2 and index not in start_indexes:
                            start_indexes.append(index)
                            new_coord = {}
                            new_coord[
                                'speed'] = (coord['speed'] +
                                            coords[index + 1]['speed']) / 2
                            new_coord['dist1'] = coord['dist']
                            new_coord['dist2'] = coords[index + 1]['dist']
                            # coord['index']
                            new_coord['index'] = index
                            lat1 = coord['lat']
                            lng1 = coord['lng']
                            lat2 = coords[index + 1]['lat']
                            lng2 = coords[index + 1]['lng']
                            coordinates = [[lng1, lat1], [lng2, lat2]]
                            new_coord['coordinates'] = coordinates
                            geo_coords.append(new_coord)
                        else:
                            continue
                    mapper[size]['coords'] = geo_coords

                    with open(write_directory + '/' + filename, 'w') as f:
                        json.dump(mapper[size], f)


if __name__ == '__main__':
    convert_withGran(granularity=10)
