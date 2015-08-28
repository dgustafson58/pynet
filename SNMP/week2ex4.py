import snmp_helper

COMMUNITY_STRING='galileo'
IP='50.76.53.27'
SYS_NAME= '1.3.6.1.2.1.1.5.0'
SYS_DESCR='1.3.6.1.2.1.1.1.0'

rtr1=(IP, COMMUNITY_STRING, 7961)
rtr2=(IP, COMMUNITY_STRING, 8022)

for rtr in (rtr1, rtr2):
    for info in (SYS_NAME, SYS_DESCR):
        data=snmp_helper.snmp_get_oid(rtr, oid=info)
        output=snmp_helper.snmp_extract(data)
        print output
        print



