from ciscoconfparse import CiscoConfParse

config=CiscoConfParse('cisco_ipsec.txt')

crypto2=config.find_objects_w_child(parentspec=r'^crypto map', childspec=r'set pfs group2')



for line in crypto2:
    print line.text
    for child in line.children:
        print child.text
