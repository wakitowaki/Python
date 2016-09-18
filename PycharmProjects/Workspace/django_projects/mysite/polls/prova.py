from django.shortcuts import render
from django.http import HttpResponse
import xmltodict
import json
import os.path
import urllib2
import xml.etree.ElementTree as ET
import pprint
import dicttoxml


class Converter(object):

    def __init__(self, url):

        self.url = url
        pass

    def getJsonWeb(self):

        self.data = urllib2.urlopen(self.url).read()
        return json.loads(self.data)

    def getJsonFile(self):
        pass

    def jsonToDict(self):
        pass

    def dictToJson(self):
        pass

    def getXmlWeb(self):
        pass

    def getXmlFile(self,file_name):

        self.base_path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(self.base_path, file_name)) as fd:
            self.doc = fd.read()
        return self.doc


    def xmlToDict(self,file):

        return xmltodict.parse(file)


    def dictToXml(self):
        pass




if __name__ == '__main__' :

    a = Converter("https://api.github.com/users?since=100")
    #pprint.pprint(a, indent=4)
    test_dict = a.xmlToDict(a.getXmlFile(("aaa.xml")))
    #print a.xmlToDict(a.getXmlFile("aaa.xml"))
    #print type(test_dict)
    #print test_dict.keys()

    partial_dict = test_dict['MaterialDatabase']['MaterialGroups']['MaterialGroup']['@Name'=='Metal']

    #print json.dumps(partial_dict)
    #print '   '
    prova = ET.ElementTree(file = 'aaa.xml')
    root = prova.getroot()
    print root.tag, root.attrib

    for elem in prova.iterfind('MaterialGroups/MaterialGroup[@Name="Metal"]'):
        elem.set('Name','Prova')    #//sostituisce elemento
        print elem.tag, elem.attrib

    for elem in prova.iterfind('MaterialGroups/MaterialGroup/'):
        elem2 = ET.Element('Material')

    prova.write('output.xml')





