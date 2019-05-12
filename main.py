import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

# I want the output to look something like
'''
PR-1780: taco bell is a sport
<img src="foo.jpg" width=300 />
## Description
* first commit (one line)
* second commit (two lines)
* third commit (three lines)
## Screenshots
<!-- please put screenshots here -->
'''
# since that's the approximate github pull request template

# I want to pull from the scryfall API a random card image and
# use that URL as the header for the pull request

# the scryfall API looks like
'''
https://api.scryfall.com/cards/random
{
  "object": "card",
  "id": "da248001-ed75-4b68-9532-37d3cd5afc4c",
  "name": "Gauntlet of Might",
  "uri": "https://api.scryfall.com/cards/da248001-ed75-4b68-9532-37d3cd5afc4c",
  "image_uris": {
    "art_crop": "https://img.scryfall.com/cards/art_crop/en/lea/244.jpg?1525123863",
  },
  "artist": "Christopher Rush",
  "related_uris": {
    "gatherer": "https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=15",
  },
}

and accepts the following parameters:

> format
> version

and sets the following headers:
> X-Scryfall-Card-Image
'''

# in our case, we would like the request to look like
# https://api.scryfall.com/cards/random?format=json
# and to grab the 'art_crop' and 'artist' fields, as well as apply a link
# to the URI along with the copyright '(c) Wizards of the Coast'
# for example, we should probably do something like
'''
<img src="https://img.scryfall.com/cards/art_crop/en/lea/244.jpg" width=300 /><br/>
<a href='https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=15'>
`Christopher Rush (c) Wizards of the Coast`
</a>

## Description
* adds something
* adds something else
* changes something

## Screenshots
<!-- wat -->
'''
