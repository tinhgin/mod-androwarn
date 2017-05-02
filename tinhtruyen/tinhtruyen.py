import os
os.chdir('..')
cwd = os.getcwd()
from gintool import getfilename

print getfilename(cwd)

#def get_method_invoke():
 #   with open('methoddump/' + jarname + '/' + xx[0]) as infile: