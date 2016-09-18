import xmltodict
import json

with open('aaa.xml') as fd:
    doc = xmltodict.parse(fd.read(),process_namespaces=True)

f = file('out.xml',mode='w')
f.write(xmltodict.unparse(doc,pretty=True))
f.close()
j = file('out.json',mode='w')
j.write(json.dumps(doc, indent=2))
j.close()
#print doc
print type(doc)
print (json.dumps(doc,indent=2))
#print xmltodict.parse(fd.read(),process_namespaces=True)
print xmltodict.unparse(doc,pretty=True)
