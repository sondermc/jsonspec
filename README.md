# jsonspec

I found myself struggling from time to time with gnumake creating specfiles. So I liked to do some efforts on lowering the bar. My idea is to use a json file as input to create the rpm.spec file and the needed tar file containing the binaries, scripts and whatever else. 

My personal believe is creating installable artifacts is the most charming way to handle zero-touch platforms, and next to that I'm convinced that maintainability of code is key.

# moving parts

## data
In this repo you find 'rpm_data.json' which is the input file. 

## schema
json is great since you can validate the input. In the directory 'schema' you find 'rpm_schema.json'. To validate the data
```bash
$ jsonschema -i rpm_data.json schema/rpm_schema.json
```

## template
I use a base template in the 'template' directory but this might change.

## script
the script 'jsonspec.py'. To run:
```bash
$ python jsonspec.py'
```
