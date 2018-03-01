#!/usr/bin/python
import json
 
data = json.load(open('rpm_data.json'))

print('-------------------------------------------------------------------------')
print('RPM_NAME: {0}'.format(data['rpmname']))
print('RPM_DESC: {0}'.format(data['rpmdesc']))
print('RPM_VERSION: {0}.{1}.{2}'.format(data['rpmversion.major'], data['rpmversion.minor'],data['rpmversion.patch'] ))
print('FILES:')
for i in data['file']:
  print('FILE: src: {0}, dest: {1}'.format(i['source'],i['destination']))
print('-------------------------------------------------------------------------')

t = open("template/template.spec", "r+")

for row in t:
  newrow = row.replace("{rpmname}", data['rpmname'])
  print newrow

t.close()
