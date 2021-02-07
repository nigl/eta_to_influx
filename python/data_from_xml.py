import urllib
from urllib.request import urlopen
import xml.etree.ElementTree as etree
import csv
import collections


def get_dict_all_columns(path_to_variable_csv, eta_url):
    uriDict = read_variable_dict(path_to_variable_csv)

    # get values from all sensors
    valueDict = {}
    for key in uriDict.keys():
        valueDict[key] = getValueFromUri(eta_url, uriDict[key])
    valueDict = collections.OrderedDict(sorted(valueDict.items()))
    return valueDict


def read_variable_dict(csvpath):
    with open(csvpath, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        mydict = dict(filter(None, reader))
    return (mydict)


def getValueFromUri(eta_url, uri):
    responseVar = urllib.request.urlopen(eta_url + uri)
    treeVar = etree.parse(responseVar)
    root = treeVar.getroot()
    return root.find("{http://www.eta.co.at/rest/v1}value").attrib["strValue"]


def evaluateTreeLevel(level, uriDict, prefix=""):
    for child in level:
        if (len(child.getchildren()) > 0):
            new_prefix = prefix + "_" + child.attrib["name"]
            evaluateTreeLevel(child, uriDict, new_prefix)
        else:
            uriDict[prefix + "_" + child.attrib["name"]] = child.attrib["uri"]



