from lxml import etree as ET
import json
from pprint import pprint
import random
import string



#   Incisione CO2 -----> 1
#   Taglio CO2    -----> 2
#
#   Incisione Fibra ---> 8
#   Taglio Fibra    ---> ?    (Verificare)
#
#
#


def randomKey(length):
    key = ''
    for i in range(length):
        key += random.choice(string.lowercase + string.digits)
    return key


def createTree(path,name):
    parser = ET.XMLParser(remove_blank_text=True)
    tree = ET.parse(path,parser)
    print 'Creation of tree :', name
    return tree

def jsonToDict(path):
    with open(path) as fd:
        fd = json.load(fd)
        print'''*******************************\njson CONTENT ---> TO DICTIONARY\n*******************************\n\n'''
        pprint(fd)
        print '\n'
        return fd


def addMaterial(base_tree,material_tree,param_array):

    #-----------ADD MATERIAL TO MATERIAL GROUP "Custom"----------------

    for i in param_array['main']:
        #print i
        for elem in material_tree.iterfind('.'):
            elem.set('Name',i)
            elem.set('GUID',(randomKey(8) + '-' + randomKey(4) + '-' + randomKey(4) + '-' + randomKey(4) + '-' + randomKey(12)))
            material_string = ET.tostring(material_tree)
            material_element = ET.fromstring(material_string)
            for elem in base_tree.iterfind('MaterialGroups/MaterialGroup[@Name="Custom"]'):
                elem.append(material_element)
                print '''\n**********************************\nADDING MATERIALS NODE TO MAIN TREE\n**********************************\n'''
                print material_element.tag, material_element.attrib

    print '''\n        *****************************************\n        ADDING PARAMETERS NODES TO MATERIAL NODES\n        *****************************************'''


    #-----------ADD PARAMETERS TO "Material" ADDED IN "Custom"-------------


    for i in param_array['main']:
        print '\n        *%s*\n'%i
        for key in param_array['main'][i]:
            for elem in base_tree.iterfind('MaterialGroups/MaterialGroup[@Name="Custom"]/Material[@Name="%s"]/MaterialParameter[@Index="0"]/%s'% (i,key)):
                elem.text = param_array['main'][i][key]
                if elem.tag=='ProcessKind':
                    if param_array['main'][i][elem.tag] == '1':
                        elem.set('Description','Incisione CO2')
                    elif param_array['main'][i][elem.tag] == '2':
                        elem.set('Description','Taglio CO2')
                    elif param_array['main'][i][elem.tag] == '8':
                        elem.set('Description','Incisione FIBRA')
                    elif param_array['main'][i][elem.tag] == '?':
                        elem.set('Description','Taglio FIBRA')
                    else:
                        print 'Error in material ProcessKind'
                        raise TypeError

                print '        %s %s %s'%(key, elem.attrib,elem.text)


    #base_tree.write('output/output_tree.xml', pretty_print=True, method='xml',standalone=True,encoding='utf8')
    return base_tree




if __name__ == '__main__':

    #--------TREE CREATION-------------

    dbTrotec_tree = createTree('databases/DBtrotec.xml','dbTrotec_tree')
    trotecMaterial_tree = createTree('databases/trotec_material.xml','trotecMaterial_tree')

    #-------PARSE JSON INTO DICT----------

    trotecParameter_array = jsonToDict('databases/data.json')

    #-------ADD ELEMENTS TO MAIN TREE------

    out_tree = addMaterial(dbTrotec_tree,trotecMaterial_tree,trotecParameter_array)

    #-------WRITE OUT_TREE TO FILE---------

    out_tree.write('output/output_tree.xml', pretty_print=True, method='xml',standalone=True,encoding='utf8')

