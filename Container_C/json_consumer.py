import json
import pprint


def get_artist_from_file():
    with open('artist.json') as json_file:
        data =  json.load(json_file)
        return data

def get_albums_from_file():
    with open('album.json') as json_file:
        data =  json.load(json_file)
        return data

def format_data_for_scrap(artist:list,album:list):
    dict_list = []
    for x in range(len(artist)):
        Music_Data = {
            "Artist":artist[x].get('Artist') ,
            "Album":album[x].get('Album')
        }
        dict_list.append(Music_Data)
    return dict_list

def get_api_key():
    with open('config.json') as json_file:
        data =  json.load(json_file)
        return data.get('api_key')

if __name__ == "__main__":
    albums = get_albums_from_file()
    pprint.pprint(albums)
    pass