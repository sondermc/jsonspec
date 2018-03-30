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
print('-------------------------------------------------------------------------*')

#t = open("spec/jsonspec.template", "r+")
#print t.read().replace('$rpmname',data['rpmname'])

with open("spec/jsonspec.template", "r+") as inputFile:
    inputText = inputFile.read()
    inputText = inputText.replace('$rpmname',data['rpmname'])
    inputText = inputText.replace('$rpmdesc',data['rpmdesc'])

print inputText 
