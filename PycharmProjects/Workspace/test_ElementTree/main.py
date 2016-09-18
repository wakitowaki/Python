from lxml import etree as ET
from xml.dom import minidom

#tree = ET.ElementTree(file='aaa.xml')
parser = ET.XMLParser(remove_blank_text=True)                                           # needed to correctly print out stuff
tree = ET.parse('aaa.xml',parser=parser)                                                # Parse xml file and build and ET.tree
root = tree.getroot()                                                                   # Get root of the tree (DEBUG)
print type(root), root.tag, root.attrib, root.text                                      # Print tag attrib and text of the root node (DEBUG)



#--------XML strings for test-----------#


material_type = '''<MaterialGroup Name="CUSTOM" SystemValue="false" GUID="{RANDOMIZE}"></MaterialGroup>'''

material = '''<Material Description="" GUID="{103c54a8-efab-43bb-b12c-939360ffde72}" Name="Custom Material" SystemValue="false" Thickness="0.00000"></Material>'''

snippet = '''<MaterialParameter Color="CIUCCIAMELO" Enabled="false" Index="0" Name="0"></MaterialParameter>'''

material_type_xml = ET.fromstring(material_type)                                        # Build an Element object from a string
material_xml = ET.fromstring(material)
snippet_xml = ET.fromstring(snippet)

material_type_xml.append(material_xml)                                                  # Add <material_xml> as child of <material_type_xml>
material_xml.append(snippet_xml)                                                        # <material_type_xml> ----> <material_type> ----> <snippet_xml>

#print type(material_type_xml), material_type_xml.tag, material_type_xml.attrib         # Print stuff (DEBUG)
#print type(snippet_xml), snippet_xml.tag, snippet_xml.attrib
#ET.dump(material_type_xml)                                                             # Print the Element object material_type_xml
#tree2 = ET.ElementTree(material_type_xml)                                               # Build a ElementTree from Element
#tree2.write('out4.xml')                                                                 # Write to file
#tree.write('out3.xml')

for elem in tree.iterfind('.//MaterialGroups'):                                         # Get all the elements of the tree wich are tagged MaterialGroups
    print elem.tag, elem.attrib, elem.text                                              # Print tag, attributes and text of the element
    elem.append(material_type_xml)                                                      # Add <material_type_xml> (with all his children) to <MaterialGroups> node Of the ElementTree 'tree'

tree.write('test.xml',pretty_print=True,method='xml')                            #CORRETTO PURE QUESTO!!!!!!!!!


out2 = open('outfile2.xml', 'w')                                                #CORRETTO!!!!!USARE QUESTO!!!!!!
rough_tree2 = ET.tostring(root,pretty_print=True,xml_declaration=True,standalone=True)
out2.write(rough_tree2)
out2.close()









