#!/usr/bin/env python

from tinhtruyen import *

def ClassifySensitiveMethod(ListMethod):
    smali = 'smali.'
    filesink = open("C:/Users/Thanh Truyen/PycharmProjects/mod-androwarn/tinhtruyen/Ouput_CatSinks.txt", "r")
    filesource = open("C:/Users/Thanh Truyen/PycharmProjects/mod-androwarn/tinhtruyen/Ouput_CatSources.txt", "r")
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
k = get_method_invoke()
L = ClassifySensitiveMethod(k)
t = "1"