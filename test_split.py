#-*- coding:utf-8-*-
import re
import dataSplit as ds
T = ds.dataSplit()
d = '/home/hadoop/Desktop/72.txt'
tr = '/home/hadoop/Desktop/train.txt'
te = '/home/hadoop/Desktop/test.txt'
T.split(d,tr,te)

