import system
import requests

# make a request to the scryfall API

SCRYFALL_BASE_URL = 'https://api.scryfall.com'
RANDOM_ENDPOINT = 'cards/random'
DEFAULT_PARAMS = 'format=json'

resp = requests.get("{}/{}?{}".format(SCRYFALL_BASE_URL, RANDOM_ENDPOINT, DEFAULT_PARAMS))
# parse the json response and set up the card and gatherer images

response = resp.json()
card_art_url = response["image_uris"]["art_crop"]
gatherer_url = response["related_uris"]["gatherer"]

# find the commits on your current branch since master



# collate these into the pull request body
# use hub with this message to open a pull request

