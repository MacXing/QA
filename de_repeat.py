import numpy as np
import pandas as pd

def init_data():
    repeat_data=pd.read_csv('C:\\Users\\User\\Desktop\\extra\\10000.csv',encoding='gbk')
    my_data=pd.read_csv('C:\\Users\\User\\Desktop\\extra\\demo6.csv',encoding='gbk')
    repeat_data=p_data(repeat_data)
    # my_data=m_data(my_data)
    content=[]
    answer=[]
    a=[]
    b=[]
    c=[]
    d=[]
    # print(my_data)
    for md in range(len(my_data)):
        if my_data['题干'][md] not in repeat_data:
            # print(md)
            content.append(my_data['题干'][md].replace('．','').replace('！','').replace('“＿','').replace('（）',''))
            answer.append(my_data['正确答案'][md])
            a.append(my_data['选项A'][md])
            b.append(my_data['选项B'][md])
            c.append(my_data['选项C'][md])
            d.append(my_data['答案列'][md])
    submit(content,answer,a,b,c,d)

def submit(qa1,qa2,qa3,qa4,qa5,qa6):

    result = pd.DataFrame({'题干': qa1, '选项A': qa3, '选项B': qa4, '选项C': qa5, '正确答案': qa2,'答案列':qa6})
    head = ['题干', '选项A', '选项B', '选项C', '选项D','答案列', '正确答案', '难易程度', '题目解释']
    result.to_csv("C:\\Users\\User\\Desktop\\extra\\test.csv", columns=head, index=False)

def demo_csv():
    my_data = pd.read_csv('C:\\Users\\User\\Desktop\\extra\\test.csv', encoding='gbk')
    print(len(my_data))
    data=set([my_data['题干'][md] for md in range(len(my_data))])
    print(len(data))



def p_data(repeat_data):

    return [data for data in repeat_data['题干']]

# def m_data(my_data):
#
#     return [data for data in my_data['题干']]


if __name__ == '__main__':
    init_data()
    # demo_csv()