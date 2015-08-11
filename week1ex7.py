import yaml
import json

with open("week1.yml") as f:
    ylist=yaml.load(f)

with open("week1.json") as f:
    jlist=json.load(f)

print'Yaml file\n'
for y in ylist:
    print y

print'\nJson file\n'
for j in jlist:
    print j
