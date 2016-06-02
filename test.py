import re
import urllib2

ma = urllib2.urlopen(r'http://www.imooc.com/course/list?c=python')
buf = ma.read()
list1 = re.findall(r'http://.*\.?jpg',buf)
num = 0
for i in list1:
    print i
    f = open(str(num)+'.jpg','w')
    buffer2 = urllib2.urlopen(i)
    f.write(buffer2.read())
    f.close()
    num = num + 1
#print buf