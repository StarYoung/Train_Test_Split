#-*- coding:utf-8-*-
import re
import sys


labels = dict()

def update(line,labelsFound,i):

    for label in labelsFound:
        labels.get(label)[0] += 1
        labels.get(label)[i] += 1


# 主函数
def split(dataSet,train,test,k=0.9):
    pattern = re.compile('\([a-z][a-z]*[12345]\)')

    dataSource = open(dataSet)
    trainText = open(train, 'w')
    testText = open(test, 'w')

    for line in dataSource:
        labelsFound = re.findall(pattern, line)

        tempSums = dict()
        for label in labelsFound:

            if labels.has_key(label):
                # 如果字典里存在该lable，就更新temp
                tempSums[label] = labels.get(label)[0]
            else:
                # 不存在，先在labels中新建，再更新temp
                labels[label] = [0, 0, 0]
                tempSums[label] = 0

        # 如果是空的一行，则跳过
        if len(tempSums) == 0:
            continue

        # 找到temp中最小的value对应的label
        # focus = min(tempSums.items(), key=lambda x: x[1])[0]
        focus = min(tempSums, key=tempSums.get)

        # print focus

        # 确定归类
        if labels.get(focus)[1] <= labels.get(focus)[0] * k:
            i = 1
        else:
            i = 2

        update(line, labelsFound, i)

        # 写入文件
        if i == 1:
            trainText.write(line)
        else:
            testText.write(line)

    for label in labels:
        print label, float(labels.get(label)[1]) / float(labels.get(label)[0])

    print labels

dataSet = sys.argv[1]
train = sys.argv[2]
test = sys.argv[3]

split(dataSet,train,test)

#
# a='/home/hadoop/Desktop/72.txt'
# b='/home/hadoop/Desktop/train.txt'
# c='/home/hadoop/Desktop/test.txt'

# split(a,b,c)
