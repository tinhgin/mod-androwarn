import os
import re
os.chdir('..')
cwd = os.getcwd()
from gintool import getfilename

class MethodItem:
    def __init__(self):
        self.nmethod=""
        self.submethods=[]


def get_endsplitstring(x):
    return x.split(" ")[len(x.split(" "))-1].strip("\n")

def get_method_invoke():
    k = []
    invoke = re.compile("^invoke")
    for i in getfilename(cwd+"/methoddump"):
        with open(i, "r") as readfile:
            tmp = MethodItem()
            tmp.nmethod=i
            for line in readfile:
                if invoke.match(line.strip()):
                    tmp.submethods.append(get_endsplitstring(line))
        k.append(tmp)
    return k


def ClassifySensitiveMethod(ListMethod):
    smali = 'smali.'
    filesink = open('tinhtruyen/Ouput_CatSinks.txt', "r")
    filesource = open('tinhtruyen/Ouput_CatSources.txt', "r")
    ListMethodClassified = []
    for Item in ListMethod:
        tmp = MethodItem()
        tmp.nmethod = Item.nmethod[Item.nmethod.index(smali) + len(smali):-7]
        for submethod in Item.submethods:
            for line in filesink:
                if line.endswith(":\n"):
                    type = line[:-2]
                elif submethod == line[:-1]:
                    strtmp=submethod + "#sink" + "@" + type
                    tmp.submethods.append(strtmp)
                    break
            filesink.seek(0,0)
            for line in filesource:
                if line.endswith(":\n"):
                    type = line[:-2]
                elif submethod == line[:-1]:
                    strtmp = submethod + "#source" + "@" + type
                    tmp.submethods.append(strtmp)
                    break
            filesource.seek(0,0)
        ListMethodClassified.append(tmp)
    return ListMethodClassified
def getDiffMethod(x, nClass, nMethod, nDiffMethod):
    structural_analysis_results = x.tainted_packages.search_methods(nClass, nMethod, ".")
    for result in xrange(len(structural_analysis_results)):
        method = structural_analysis_results[result].get_method()
        if method.get_name() == nDiffMethod :
            return method, structural_analysis_results[result].get_idx()
