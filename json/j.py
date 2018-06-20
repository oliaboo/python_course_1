import json
with open('aaa.txt') as f:
    r = json.load(f)
    print(r)
    print(r['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'])
