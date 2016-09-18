import xml.etree.ElementTree as ET


#tree = ET.ElementTree(file='aaa.xml')
tree = ET.parse('aaa.xml')
root = tree.getroot()
print type(root), root.tag
#for child in root:
 #   print type(child),child.tag, child.attrib
#a = ET.Element('Material',attrib={'Name':'Forex', 'test':'CIUCCIAAAAAAAA'}) #construct an Element
#b = ET.SubElement(a,'Params',attrib={'prova':'Test'})                       #subelement of element

#for elem in tree.iterfind('MaterialGroups/MaterialGroup'):  #iterate through the tree
 #   elem.append(a)                                          #append a child to MaterialGroups/MaterialGroup

material_type = '''<MaterialGroup GUID="{RANDOMIZE}" Name="CUSTOM" SystemValue="false"></MaterialGroup>'''

material = '''<Material Description="" GUID="{103c54a8-efab-43bb-b12c-939360ffde72}" Name="Custom Material" SystemValue="false" Thickness="0.00000"></Material>'''




snippet = '''<MaterialParameter Color="CIUCCIAMELO" Enabled="false" Index="0" Name="0">
          <Info>Param1</Info>
          <ProcessKind Description="Incisione FIBRA">89999999999999999999999</ProcessKind>
          <Power>60.00000</Power>
          <Frequency Unit="Hz">25000.00000</Frequency>
          <AutoFrequency>false</AutoFrequency>
          <MarkSpeed>15.00000</MarkSpeed>
          <Passes>1</Passes>
          <AirAssist Description="on">1</AirAssist>
          <ZOffset>0.00000</ZOffset>
          <Correction>10.00000</Correction>
          <Links>false</Links>
          <IntelligentPathControl Description="off">0</IntelligentPathControl>
          <HighQuality>false</HighQuality>
          <RasterCorrection>false</RasterCorrection>
        </MaterialParameter>'''

material_type_xml = ET.fromstring(material_type)
material_xml = ET.fromstring(material)
snippet_xml = ET.fromstring(snippet)            #generate an element snippet_xml from an XML string

material_type_xml.append(material_xml)
material_xml.append(snippet_xml)

#print type(material_type_xml), material_type_xml.tag, material_type_xml.attrib
#print type(snippet_xml), snippet_xml.tag, snippet_xml.attrib
#ET.dump(material_type_xml)
tree2 = ET.ElementTree(material_type_xml)
tree2.write('out4.xml')
tree.write('out3.xml')

for elem in tree.iterfind('.//MaterialGroups'):
    print elem.tag, elem.attrib
    elem.append(material_type_xml)

tree.write('out5.xml')

#tree_temp = ET.ElementTree(material_type_xml)
#print material_type_xml



#for elem in tree.iterfind('MaterialGroups'):
 #   print elem.tag, elem.attrib



#snippet_tree = ET.ElementTree(snippet_xml)      #wrap element into a subtree snippet_tree
#print snippet_tree.getroot().tag,snippet_tree.getroot().attrib              #get root element of the snippet_tree subtree

#for child in snippet_tree.getroot():            #iterate through the subtree snippet_tree
#    print child.tag, child.attrib, child.tag    #print out stuff




#tree.write('out3.xml')




