import os
import uuid
import re
import time
import threading

#xml_string = '<AUTOSAR>'
#namespace = '<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 autosar_4-0-3.xsd">'

#xml_string = re.sub('<AUTOSAR>', namespace, xml_string, count=1)

#print(xml_string)

#curr = time.time()
#print("curr:", curr)
#time.sleep(1)
#later = time.time()
#print("later:", later)


#n = re.compile('.+Crc.+')

#q = n.match("aaCrcaa")

#if q:  # include crc signal
#    print("OK")
#else:
#    print("Not OK")

t = [[0,1,2],[3,4,5]]

#mul = 5//3
#mul_2 = 5/3
#mul_3 = 5%3

for idx, tmp in enumerate(t):
    print("idx:", idx)
    print("tmp", tmp[2])
#print("mul_2:", mul_2)
#print("mul_3:", mul_3)