import os
import re
os.chdir('..')
cwd = os.getcwd()
from gintool import getfilename

class MethodItem:
    nmethod=""
    methods=[]


def get_endsplitstring(x):
    return x.split(" ")[len(x.split(" "))-1].strip("\n")

def get_method_invoke():
    k = []
    invoke = re.compile("^invoke")
    for i in getfilename(cwd+"/methoddump"):
        with open(i, "r") as readfile:
            tmp = MethodItem()
            tmp.methods = []
            tmp.nmethod=i
            for line in readfile:
                if invoke.match(line.strip()):
                    tmp.methods.append(get_endsplitstring(line))
        k.append(tmp)
    return k