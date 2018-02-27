from aip import AipNlp
import json
import connSql
import mulKMeans
import numpy as np
import random
import pandas as pd
import synonyms

def baiduAPI():
    APP_ID = '10811567'
    API_KEY = 'iaSle87iAXynm6L1DYyRif0Z'
    SECRET_KEY = 'psZE9wAyBYtA4qPSzDuAlIHyr9XiqoKN'
    return AipNlp(APP_ID, API_KEY, SECRET_KEY)

def openTxt(path):
    data=[]
    with open(path,'r',encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def partData(data):

    partdata=[part['answer'][0] for part in data[29000:]]
    return partdata

def partWordVec(partdata):
    datavec=[]
    # clients={}
    i=0
    for word in partdata:
        # clients['id']=str(uuid.uuid1())
        i+=1
        vec=baiduAPI().wordEmbedding(word)
        if 'vec' in vec.keys():
            datavec.append(str(vec['vec']))
            # clients['vec']=vec['vec']
        else:
            # clients['vec']=vec['error_msg']
            datavec.append(vec['error_msg'])
        print("API--------%s/%s"%(i,len(partdata)))



    return datavec

def saveWordVec(partdata):
    datavec=partWordVec(partdata)

    with open('C:\\Users\\User\\Desktop\\extra\\wordvec.txt','a',encoding='utf-8') as f:
        for da in datavec:
            # txt=json.dumps(da)
            f.write(da+'\n')


def inputWordVec(path):
    wordvec=[]
    with open(path,encoding='utf-8') as f:
        for line in f:
            wordvec.append(line)
    return wordvec

def initWordVec(path):
    wordvec = inputWordVec(path)
    word2vec= []
    for vec in wordvec:
        if vec not in 'error_msg':
            vec=vec.replace('[','')
            vec=vec.replace(']','')
            word2vec.append(vec)
        else:
            word2vec.append(vec)
    # print(len(word2vec))
    return word2vec

def dict_wordVec(wordvec,data):
    dict_word_vec={}
    for i in range(len(wordvec)):
        if 'word' not in wordvec[i]:
            dict_word_vec[data[i]]=wordvec[i]
    # print(len(dict_word_vec))
    return dict_word_vec

def muldata(dict_word_vec):
    arr_list=[]
    for k in dict_word_vec.keys():
        # print(dict_word_vec[k])
        data_list=dict_word_vec[k].replace('\n','').replace(' ','').split(',')
        data_list=[float(d) for d in data_list]
        arr_list.append(data_list)
    # print(len(arr_list))
    return np.array(arr_list)

def mulkey(dict_word_vec):
    data_dict={}
    for k in dict_word_vec.keys():
        data_list=dict_word_vec[k].replace('\n','').split(',')
        data_list=[float(d) for d in data_list]
        data_dict[k]=data_list
    return data_dict

def str_to_list(d):
    arr_list = []
    data_list = d.replace('\n','').split(',')
    data_list = [float(d) for d in data_list]
    arr_list.append(data_list)
    # print(len(arr_list))
    return np.array(arr_list)

def classfiy(result,dict_word_vec):
    classfies={}
    i = 0
    for k in dict_word_vec.keys():
        classfies[k]=result[i]
        i=i+1
    return classfies


word=[]

classfies={}

def set_classfies(value):
    global classfies
    classfies=value

def bool_value(d):
    l = sorted(d.items(), key=lambda v: v[1])
    global word
    s = set()
    value = 0
    for k, v in l:
        if value == v:
            s.add(k)
        else:
            value = v
            word.append(list(s))
            s = set()
            s.add(k)

    # for w in word:
    #     print(w)

def question(data):
    questions=[]
    for di in data:
        questions.append(di['question'])
    return questions

def per_answer(data):
    answer=[]
    for d in data:
        answers(d['answer'][0])
        answer.append(d['answer'][0])
    return answer

b=[]
c=[]
def answers(w):
    global b
    global c
    global word
    for l in word:
        if len(l) >=3:
            if w in l:
                x=np.random.randint(0,len(l)-1,2)
                # print(l[x[0]])
                b.append(l[x[0]])
                c.append(l[x[1]])

        else:
            b.append('')
            c.append('')

def submit(questions,answer):
    global b
    global c
    list_qa=[]
    dict_qa={}
    # print(len(questions))
    # print(len(answer))
    # print(len(b))
    # print(len(c))
    # for i in b:
    #     if i is not '':
    #         print(i)
    for i in range(len(answer)):
        if b[i] !='' and c[i] !='':
            # dict_qa['question']=questions[i]
            # dict_qa['answer']=answer[i]
            # dict_qa['a']=answer[i]
            # dict_qa['b']=b[i]
            # dict_qa['c']=c[i]
            list_qa.append([questions[i],answer[i],answer[i],b[i],c[i]])
    return list_qa

def re_qa(list_qa):
    da1=[]
    da2=[]
    da3=[]
    da4=[]
    da5=[]
    da6=[]
    a=[2,3,4]
    print(list_qa)
    for qad in list_qa:
        da1.append(qad[0].replace("'",''))
        da6.append(qad[1])
        x=random.sample(a,3)
        # print(x)
        a1=qad[x[0]]
        a2=qad[x[1]]
        a3=qad[x[2]]
        da3.append(qad[x[0]])
        da4.append(qad[x[1]])
        da5.append(qad[x[2]])
        if qad[2] == a1:
            da2.append('A')
        elif qad[2] == a2:
            da2.append('B')
        elif qad[2] == a3:
            da2.append('c')
    # print(len(da1))
    # print(len(da2))
    # print(len(da3))
    # print(len(da4))
    # print(len(da5))
    save_csv(da1,da2,da3,da4,da5,da6)

def synon(answer):
    b=[]
    c=[]
    for a in answer:
        a = a.replace('、','')
        temp = synonyms.nearby(a.replace('\xa0',''))
        if len(temp[0]):
            b.append(temp[0][0])
            c.append(temp[0][1])
        else:
            b.append("")
            c.append("")
    return b,c

def creatSelect():
    list_qa=[]
    data=openTxt('C:\\Users\\User\\Desktop\\extra\\qa1.txt')
    questions = [d['question']for d in data]

    only_question,answer=similarity(data)

    # answer = find_answer(only_question,data)
    b,c=synon(answer)
    for i in range(len(only_question)):
        list_qa.append([only_question[i],answer[i],answer[i],b[i],c[i]])
    re_qa(list_qa)

def creat_aq(data):
    dict_qa={}
    for d in data:
        if d['answer'][0] !='':
            dict_qa[d['question'].replace('\xa0','').replace('、','')
                .replace('"','').replace('*','').replace('(','“').replace(')','“')
                .replace('!','').replace('＂','“').replace('，','').replace('：','')
                .replace('＜＜', '《').replace('＞＞', '》').replace('＜', '《').replace('＞', '》').replace('＞', '》')
                ]=d['answer'][0].replace('\xa0','').replace('、','').replace('？','')
    return dict_qa


# def find_answer(question,data):
#     an=[]
#     for q in question:
#         for d in creat_aq(data):
#             if q in d[0]:
#                 an.append(d['answer'][0].replace('\xa0','').replace('"',''))
#     return an

def similarity(data):
    dict_qa = creat_aq(data)
    list_qa=[k+"@"+dict_qa[k]for k in dict_qa.keys()]
    only_question=[]
    only_answer=[]
    # for k in dict_qa.keys():
    #     if dict_qa[k]=='':
    #         print(k)
        # only_question.append(k)
        # only_answer.append(dict_qa[k])
    questions=sorted(list_qa)

    questions=[q.split('@')for q in questions]
    # print(questions)
    # print(len(questions))
    for qa in range(len(questions)):
        if questions[qa][1] =='':
            print(questions[qa][0])

    # print(len(questions))
    for qu in range(len(questions)):
        if qu ==len(questions)-1:
            only_question.append(questions[qu][0].replace('╮(￣▽￣)╭','').replace('.','').replace('','“'))
            only_answer.append(questions[qu][1])
        elif len(questions[qu+1][0]):
            if count_similarity(questions[qu][0],questions[qu+1][0]) < 0.8:
                only_question.append(questions[qu][0].replace('╮(￣▽￣)╭','').replace('','').replace('.','').replace('’','“'))
                only_answer.append(questions[qu][1])
    return only_question,only_answer

def count_similarity(s1,s2):
    count=0
    for w in s1:
        if w in s2:
            count+=1
    return float(count/len(s1))

def open_word_txt(url):
    with open(url,'r',encoding='utf-8')as f:
        data=[line.split()[-1]for line in f]
    return data

def save_csv(qa1,qa2,qa3,qa4,qa5,qa6):

    result = pd.DataFrame({'题干': qa1, '选项A': qa3, '选项B': qa4, '选项C': qa5, '正确答案': qa2, '答案列':qa6 })
    head = ['题干', '选项A', '选项B', '选项C', '选项D','答案列', '正确答案', '难易程度', '题目解释']
    result.to_csv("C:\\Users\\User\\Desktop\\extra\\demo6.csv", columns=head, index=False)

if __name__ == '__main__':
    # client = baiduAPI().wordEmbedding('张飞')
    # if 'vec' in client.keys():
    #     print(client['vec'])
    # else:
    #     print(client['error_msg'])
    # data=openTxt('C:\\Users\\User\\Desktop\\extra\\qa1.txt')
    # partdata=partData(data)
    # # # print(len(partdata))
    # saveWordVec(partdata)
    # # #9000个
    # word2vec=initWordVec('C:\\Users\\User\\Desktop\\extra\\wordvec.txt')
    # print(word2vec)
    # #获得词对应的词向量   word->vec
    # dict_word_vec=dict_wordVec(word2vec,partdata)
    # # for k in dict_word_vec.keys():
    # #     print(k)
    # # print(len(dict_word_vec))
    # word_keys=mulkey(dict_word_vec)
    # # for k in word_keys.keys():
    # #     print(k)
    # mulword = muldata(dict_word_vec)
    # # valide = str_to_list(dict_word_vec['中国'])
    # valide = np.array([word_keys[k]for k in word_keys])
    # # print(len(valide))
    # result = mulKMeans.train(mulword,valide)
    # # print(len(result))
    # classfies = classfiy(result,dict_word_vec)
    # # print(classfies)
    # set_classfies(classfies)
    # bool_value(classfies)
    # #所有问题
    # questions = question(data)
    # #所有答案
    # # print(partdata)
    # answer=per_answer(data)
    # # print(b)
    # # print(c)
    # # print(len(b))
    # # print(len(c))
    # list_qa=submit(questions,answer)
    # # print(len(list_qa))
    # re_qa(list_qa)
    # for qa in list_qa:
    #     print(qa)
    creatSelect()
    # temp=(synonyms.nearby('黄石国家公园'))
    # if len(temp[0]):
    #     print('ok')
    # else:
    #     print('error')
    # print(count_similarity('鲁迅的原名是什么？','鲁迅的原名是什么？'))
