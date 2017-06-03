#-*- coding:utf-8-*-
import codecs
import sys
reload(sys)
default_encoding='utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
from sklearn.cross_validation import train_test_split
import re

def reshape(filePath):
    pattern = re.compile('[a-z][a-z]+[1234]')
    # 原始数据集
    source = open(filePath)

    data = []
    label = []


    # build data[] and label[]
    # 生成以标注个数为准的数据集
    for line in source:
        # line = line.decode('gbk')
        y = re.findall(pattern, line)
        print y
        y = set(y)
        print y
        for sub in y:
            label.append(sub)
            data.append(line)

            # print len(data)
            # print len(label)
    return data,label

def newDateSet(data,label,dataPath,labelPath):
    labelSet = set()
    # 生成的测试特征集和label集
    dataTest = codecs.open(dataPath, 'w', 'utf-8')
    labelTest = open(labelPath, 'w')

    # 写入新特征集与label集
    for index1, l in enumerate(label):
        if l in labelSet:
            continue
        else:
            labelSet.add(l)
            newData = [l]
            newLabel = [data[index1]]

            # 找到所有同类的label，并新建data和label集合，并进行写入
            for index2, others in enumerate(label):
                if others == l:
                    newLabel.append(l)
                    newData.append(data[index2])
                else:
                    continue
            X_train, X_test, Y_train, Y_test = train_test_split(newData, newLabel, test_size=0.1, random_state=47)

            for x_test in X_test:
                dataTest.write(x_test)
            dataTest.write('\n')
            for y_test in Y_test:
                labelTest.write(str(y_test) + '\n')
            labelTest.write('\n')

a,b=reshape('/home/hadoop/Desktop/2.txt')
newDateSet(a,b,'/home/hadoop/Desktop/666.txt','/home/hadoop/Desktop/777.txt')

























def StratifiedSampling(self,sampling_type,scale):
# 分层抽取样本
# Args:sampling_type: 随机类型，仅支持 rs，rrs，ss，分别是随机抽样，重复随机抽样，系统抽样
# scale：抽取样本比例，值域为 (0,1)
    df_choice = None
    df_values = list(set(self.df_col[0].values))
    for i in range(len(df_values)):
        df_index = self.df_col[self.df_col[0]==df_values[i]].index
        if sampling_type == 'rs':
            df_choice_index = self.__randomSampling(df_index,scale)
        elif sampling_type == 'rrs':
            df_choice_index = self.__repetitionRandomSampling(df_index,scale)
        elif sampling_type == 'ss':
            df_choice_index = self.__systematicSampling(df_index,scale)
        else :
            raise Exception('不支持的随机类型。')
        if df_choice is None:
           df_choice = self.df.iloc[df_choice_index]
        else:
            df_temp = self.df.iloc[df_choice_index]
            df_choice=df_choice.append(df_temp)


    df_not_choice = self.df.iloc[-(self.df.index.isin(df_choice.index))]
    return (df_choice,df_not_choice)


