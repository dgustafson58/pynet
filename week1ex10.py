from ciscoconfparse import CiscoConfParse

config=CiscoConfParse('cisco_ipsec.txt')

cryptoaes=config.find_objects_wo_child(parentspec=r'^crypto map', childspec=r'set transform-set AES-SHA')



for line in cryptoaes:
    print line.text
    for child in line.children:
        print child.text
