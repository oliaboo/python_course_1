import json

d = {}
with open('sample.json') as j:
	res = json.load(j)
	for item in res["colors"]:
		d[item["color"]] = item["code"]["rgba"]
	print(d)
