import pandas as pd
import os
import numpy as np
import wordMeans

def read():
    data=pd.read_csv('C:/Users/User/Desktop/extra/test1.csv',encoding='gbk')
    # print(len(data['题干']))
    dict_data ={}
    for d in range(len(data)):
        dict_data[data['题干'][d]] = [data['答案列'][d],data[]]
    return dict_data

error_data=[]
my_library={}

def open_libary(url):
    global error_data
    global my_library
    libary=[]
    with open(url,'r',encoding='gbk') as f:
        for line in f:
            # print(line.replace('\n','').split()[-1])
            libary.append(line.replace('\n','').split()[-1])
        my_library[url.split('\\')[-1]]=list(set(libary))

def open_txt(url):
    global error_data
    with open(url,'r',encoding='gbk') as f:
        for line in f:
            error_data.append(line)

def open_dir():
    for root, dirs, files in os.walk("C:\\Users\\User\\Desktop\\extra\\error_word", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            open_txt(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))
    for root, dirs, files in os.walk("C:\\Users\\User\\Desktop\\extra\\word_libray\\", topdown=False):
        for name in files:
            if name.split('.')[-1] == 'txt':
                print(os.path.join(root, name))
                open_libary(os.path.join(root, name))

def cut_error_word():
    global error_data
    dict_qa={}
    dict_data=read()
    print(len(dict_data))
    for k in dict_data.keys():
        for e in error_data:
            if e in k:
                print(k)
            else:
                dict_qa[k]=dict_data[k]
    print(len(dict_qa))
    words_lirary(dict_qa)

true_qa=[]

def words_lirary(dict_qa):
    for q in dict_qa.keys():
        for k in my_library:
            if dict_qa[q] in my_library[k]:
                x = my_library[k].index(dict_qa[q])
                true_qa.append([q,dict_qa[q],dict_qa[q],my_library[k][x+1],my_library[k][x-1]])
                print([q,dict_qa[q],dict_qa[q],my_library[k][x+1],my_library[k][x-1]])
                break


    print(len(true_qa))

if __name__ == '__main__':
    open_dir()

    cut_error_word()