import re

rex = ".oo"
line = "The ghost that says boo haunts the loo"

print(re.findall(rex, line, re.IGNORECASE))

