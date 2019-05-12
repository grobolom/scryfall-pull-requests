import re
from subprocess import Popen, PIPE

import requests

# make a request to the scryfall API
SCRYFALL_BASE_URL = 'https://api.scryfall.com'
RANDOM_ENDPOINT = 'cards/random'
DEFAULT_PARAMS = 'format=json'

resp = requests.get("{}/{}?{}".format(SCRYFALL_BASE_URL, RANDOM_ENDPOINT, DEFAULT_PARAMS))
print("made request to scryfall")
# parse the json response and set up the card and gatherer images

response = resp.json()
card_art_url = response["image_uris"]["art_crop"]
gatherer_url = response["related_uris"]["gatherer"]
card_name = response["name"]

# find the commits on your current branch since master
git_command = "git rev-list --no-merges HEAD ^master --pretty=oneline --abbrev-commit"

with Popen([git_command], stdout=PIPE, shell=True) as proc:
  git_output = proc.stdout.read()

print("grabbed git commits")

lines = git_output.decode('utf-8').strip().split("\n")
rev_list_regex = re.compile(r'^\w+ ')
commit_messages = [re.sub(rev_list_regex, '', line) for line in lines]
commit_lines = "\n".join(["* {}".format(message) for message in commit_messages])
first_commit = commit_messages[0]

# collate these into the pull request body

body = """
{first_commit}

<img src="{card_art_url}" width=300 />
<a href="{gatherer_url}">`{card_name} (c) Wizards of the Coast`</a>
## Description
{commit_lines}

## Screenshots
<!-- paste screenshots here please -->
""".format(first_commit=first_commit, card_art_url=card_art_url,
           gatherer_url=gatherer_url, card_name=card_name,
           commit_lines=commit_lines)

print("built commit message")
print("------")
print(body)
print("------")

with open("message.md", "w") as outfile:
  outfile.write(body)

# use hub with this message to open a pull request

hub_command = "hub pull-request -f message.md -o -c -d"
proc = Popen([hub_command], stdout=PIPE, stderr=PIPE, shell=True)
stdout, stderr = proc.communicate()

print("pushed it")
print(stdout)
print(stderr)
