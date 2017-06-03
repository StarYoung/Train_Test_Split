#-*- coding:utf-8-*-
import re

# 初始化关于label的四个list
# 初始化关于label的四个list
#labels = dict()


class dataSplit(object):
    # 输入为该条sentence和将要放入的位置
    def __init__(self):
        self.labels = dict()

    def update(self,line,labelsFound,i):

        for label in labelsFound:
            self.labels.get(label)[0] += 1
            self.labels.get(label)[i] += 1


    # 主函数
    def split(self,dataSet,train,test,k=0.9):
        # 读
        pattern = re.compile('[a-z][a-z]+[1234]')
        dataSource = open(dataSet)
        # 写
        trainText = open(train, 'w')
        testText = open(test, 'w')

        for line in dataSource:
            labelsFound = re.findall(pattern, line)

            tempSums = dict()
            for label in labelsFound:

                if self.labels.has_key(label):
                    # 如果字典里存在该lable，就更新temp
                    tempSums[label] = self.labels.get(label)[0]
                else:
                    # 不存在，先在labels中新建，再更新temp
                    self.labels[label] = [0, 0, 0]
                    tempSums[label] = 0

            # 如果是空的一行，则跳过
            if len(tempSums) == 0:
                continue

            # 找到temp中最小的value对应的label
            # focus = min(tempSums.items(), key=lambda x: x[1])[0]
            focus = min(tempSums, key=tempSums.get)

            # print focus

            # 确定归类
            if self.labels.get(focus)[1] <= self.labels.get(focus)[0] * k:
                i = 1
            else:
                i = 2

            self.update(line, labelsFound, i)

            # 写入文件
            if i == 1:
                trainText.write(line)
            else:
                testText.write(line)

        for label in self.labels:
            print label, float(self.labels.get(label)[1]) / float(self.labels.get(label)[0])

        print self.labels




