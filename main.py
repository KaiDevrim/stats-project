import requests
from pprint import pprint
import numpy as np

# https://api.github.com/search/repositories?q=stars:>1&sort=stars
url = f'https://api.github.com/search/repositories?q=stars:>1&sort=stars&per_page=100&page='
langs = []

new_results = True
page = 1
while new_results:
    discover_api = requests.get(url + f"{page}").json()
    new_results = discover_api.get("items", [])
    langs.extend(new_results)
    page += 1

f = open('./langs.txt', 'w')
for i, repo in enumerate(langs):
    f.write(f"{repo['language']}\n")
f.close()

rng= np.random.randint(1,901,100)
data = []
with open("./langs.txt", 'r') as fp:
    for i, line in enumerate(fp):
            if i in rng:
                data.append(line.strip())
f.close()
print(data)