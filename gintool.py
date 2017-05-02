from ginExtractor import extractor
import sys
import os
import shutil


def getfilename(dir):
    k=[]
    for root, directories, filenames in os.walk(dir):
        for filename in filenames:
            k.append(os.path.join(root,filename))
    return k

def splitfilename(files):
    files1 = []
    for i in range(len(files)):
        files1.append(files[i].split('/', 1)[1])
    return files1



def dump2(jarfile):
    tmp = 'apktool d ' + jarfile
    os.system(tmp)
    directory = jarfile.split('/')[len(jarfile.split('/'))-1]
    if os.path.exists('codedump/' + directory):
        os.system('rm -rf ' + 'codedump/' + directory)
    os.makedirs('codedump/' + directory)
    out = directory + '.out'
    if directory[len(directory)-4:len(directory)] == '.apk':
        out = directory[0:len(directory)-4]    
    files = getfilename(out + '/smali')
    files1 = splitfilename(splitfilename(files))
    for i in range(len(files1)):
        k = files1[i].replace('/','.')
        shutil.copy2(files[i], 'codedump/' + directory + '/' + k)
    os.system('mv -f ' + out + ' smali')




def main(argv):
    a = extractor(argv[1])
    b = extractor(argv[2])

    #a='framework_2016-12-19_18-37-51' ############
    #b='framework_2016-12-19_18-38-00'###########
    aa = getfilename(a)
    bb = getfilename(b)
    aaa = []
    bbb = []
    #print aa,'\n\n',bb############
    a1 = aa[0].split('/',1)[0] + '/'
    #print a1#################
    for i in range(len(aa)):
        tmp = aa[i].split('/',1)[1]
        aaa.append(tmp)
    b1 = bb[0].split('/',1)[0] + '/'
    #print b1################
    for i in range(len(bb)):
        tmp = bb[i].split('/',1)[1]
        bbb.append(tmp)
    #print aaa,'\n\n',bbb###############

    file_to_compare = []
    file_to_check = []
    for i in range(len(bbb)):
        try:
            aaa.index(bbb[i])
            file_to_compare.append(bbb[i])
        except:
            file_to_check.append(bbb[i])
    #print file_to_compare,'\n\n',file_to_check##############
    #print len(file_to_check), len(file_to_compare)
    #return 0


    for i in range(len(file_to_compare)):
        try:
            tmp2 = 'python androsim.py -i ' + a1 + file_to_compare[i] + ' ' + b1 + file_to_compare[i] + ' -c ZLIB -p'
            os.system(tmp2)
        except:
            print 'Error: ' + file_to_compare[i]

    for i in range(len(file_to_check)):
        try:
            dump2(b1 + file_to_check[i])
        except:
            print 'Error: ' + file_to_check[i]            





if __name__ == '__main__':
    main(sys.argv)
