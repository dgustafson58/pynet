import yaml
import json

list=range(7)
list.append('item8')
list.append({'dave': 4059,'john':4938})
list.append(['apple', 'orange', 'banana'])

print 'Yaml\n'
print yaml.dump(list)
print '\nJSON\n'
print json.dumps(list)

with open("week1.yml","w") as f:
        f.write(yaml.dump(list))

with open("week1.json","w") as f:
        json.dump(list, f)

