#!/usr/bin/env python

class MethodClassifed:
    method = ''
    type = ''

def ClassifySensitiveMethod(ListMethod):
    sink = []
    source = []
    filesink = open("./Ouput_CatSinks.txt", "r")
    filesource = open("./Ouput_CatSources.txt", "r")
    tmp = MethodClassifed()
    for method in ListMethod:
        for line in filesink:
            if line.endswith(":\n"):
                type = line[:-2]
            elif method == line[:-1]:
                tmp.method = method
                tmp.type = type
                sink.append(tmp)
        for line in filesource:
            if line.endswith(":\n"):
                type = line[:-2]
            elif method == line[:-1]:
                tmp.method = method
                tmp.type = type
                source.append(tmp)
    return sink, source
sink, source = ClassifySensitiveMethod(["Landroid/app/Activity;->startActivity(Landroid/content/Intent;)V", "123"])
print sink[0].method