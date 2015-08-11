from ciscoconfparse import CiscoConfParse

config=CiscoConfParse('cisco_ipsec.txt')

cryptomap=config.find_objects(r'^crypto map')

print cryptomap

for line in cryptomap:
    print line.text
    for child in line.children:
        print child.text
