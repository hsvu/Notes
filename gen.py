import json
from os import listdir, getcwd
from os.path import isdir, join

res = {
	"subs": {
		"COMP3131": "How to Build a compiler and understand language semantics",
		"COMP2121": "A intro to microprocessors course",
		"COMP3891": "Operating systems in the context of harvards os161"
	},
    "tree": {

    },
	"counts": {

	}
}

elems = [f for f in listdir(getcwd()) if isdir(join(getcwd(), f)) and f[0] != "."]
for e in elems:
	dir = join(getcwd(),e)
	res["tree"][e] = [f for f in listdir(dir) if isdir(join(dir,f)) and f[0] != "." and f != "other"]
	res["tree"][e].sort()
	res["counts"][e] = len(res["tree"][e])

f = open("desc.json","w")
json.dump(res,f)
f.close()
