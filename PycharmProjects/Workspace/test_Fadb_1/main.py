from lxml import etree as ET
import json
from pprint import pprint

#---- costruzione alberi------


parser = ET.XMLParser(remove_blank_text=True)               # define a parser to remove white spaces
tree = ET.parse('databases/DBtrotec.xml',parser=parser)       # build the etree from xml
root = tree.getroot()                                       # get the root node
#print root.tag, root.attrib, root.text


material = ET.parse('databases/trotec_material.xml', parser=parser)  # build the material tree from xml
materialRoot = material.getroot()                                    # get the root node

#---- carica json------

with open('databases/data.json') as fp:          # load the json into a dict
    fp = json.load(fp)
    pprint(fp)

#for i in range(len(fp)):                         # access the feature of the dict builded from json
 #   pprint (fp[i])


#----modifica parametri-----

newMaterialName = fp['main']['MATERIALE1']['Material']            # access the json dict element
print newMaterialName
newPower = fp['main']['MATERIALE2']['Power']



for elem in material.iterfind('.'):            # find the node with tag <Material>
    print elem.tag, elem.attrib
    elem.set('Name', newMaterialName)          # modify the attribute @Name of the node <Material>!!!
    print elem.tag, elem.attrib

for elem in material.iterfind('MaterialParameter[@Index="0"]/Power'):  # modify the value of the parameter of the Material node
    print 'Power dell \'elemento con indice 0'
    print elem.tag, elem.attrib, elem.text
    elem.text = newPower
    print elem.tag, elem.attrib, elem.text


#-----scrittura su file------

material_string = ET.tostring(material)                              # convert tree into string
material_elem = ET.fromstring(material_string)                       # convert string into an Element for append

for elem in tree.iterfind('MaterialGroups/MaterialGroup[@Name="Custom"]'):    # find the right node
    elem.append(material_elem)                                                # append the new material to custom group

tree.write('output/output_tree.xml', pretty_print=True, method='xml',standalone=True,encoding='utf8') # write output to file


#with open('output/output_tree.xml','w') as fd:              #open the outfile and write the tree into it
 #   tree_string = ET.tostring(tree,method='xml',xml_declaration=True,pretty_print=True,standalone=True)
  #  fd.write(tree_string)
   # fd.close()


