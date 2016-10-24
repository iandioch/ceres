import json
import time

s = time.strftime("%X")
d = {'time': s, "var": "xD"}
j = json.dumps(d, indent=4)
print(j)
with open('data.json', 'w') as filewriter:
	filewriter.write(j)
	filewriter.write("\n")
