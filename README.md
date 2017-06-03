# Train_Test_Split
业务需求：
数据集为很多条sentence，label为注音（包括音调）
每一条sentence可能包含不同的注音（多音字），在不改动原数据集的情况下，分出trainSet和testSet，
并且让每一个label的trainSet和testSet的比例趋近于需求的9:1或者其他。

参数：数据源，生成文本的path，分割比例（9:1默认）
