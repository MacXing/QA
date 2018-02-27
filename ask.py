
# encoding: utf-8

import re
import os
import pandas as pd

ask_answer = []


def readurl(url):
    f = open(url, 'r', 255,errors='ignore')
    for line in f.readlines():
        if '"text-content"' in line:
            analyzer(line)
            return line
    return None


def analyzer(data):
    regex = '(?<=<p>)(.*?)(?=</p>)'
    m = re.compile(regex)
    s = m.findall(data)
    for i in range(len(s)):
        r = re.match(r'(<strong>[0-9].)', s[i])
        if r:
            ask = s[i][8:-9]
            option = re.subn(r'(&.*?;)', " ", s[i + 1])
            answer = s[i + 2][8:-9]
            analysis = s[i + 3][20:s[i + 3].find('<p>')]
            tp = (ask, option[0][:-3], answer, analysis)
            ask_answer.append(tp)


def dirs(dir):
    for (root, _, file) in os.walk(dir):
        for f in file:
            readurl(root + os.path.sep + f)

def creat_list():
    questions=[t[0] for t in ask_answer]
    selections=[t[1] for t in ask_answer]
    answers=[t[2] for t in ask_answer]
    # print(len(list(set(questions))))
    # print(len(selections))
    # print(answers)
    qa_dict={}
    for i in range(len(questions)):
        qa_dict[questions[i]]=[selections[i],answers[i]]
    print(qa_dict)
    compete_answer(qa_dict)
def compete_answer(qa_dict):
    true_questions=[]
    true_answers=[]
    true_a=[]
    true_b=[]
    true_c=[]
    for k in qa_dict.keys():
        if len(qa_dict[k][0].split()) == 3:
            true_questions.append(k.split('.')[-1])
            true_a.append(qa_dict[k][0].split()[0].replace('A.',''))
            true_b.append(qa_dict[k][0].split()[1].replace('B.', ''))
            true_c.append(qa_dict[k][0].split()[2].replace('C.', ''))
            # print(qa_dict[k][1].replace('正确答案：','').split('.')[0])
            true_answers.append(qa_dict[k][1].replace('正确答案：','').split('.')[0])
    # print(len(true_questions))
    # print(len(true_answers))
    # print(len(true_a))
    # print(len(true_b))
    # print(len(true_c))
    # print(true_questions[2])
    # print(true_answers[2])
    # print(true_a[2])
    # print(true_b[2])
    # print(true_c[2])
    submit(true_questions,true_answers,true_a,true_b,true_c)

def submit(qa1,qa2,qa3,qa4,qa5):

    result = pd.DataFrame({'题干': qa1, '选项A': qa3, '选项B': qa4, '选项C': qa5, '正确答案': qa2})
    head = ['题干', '选项A', '选项B', '选项C', '选项D','答案列', '正确答案', '难易程度', '题目解释']
    result.to_csv("C:\\Users\\User\\Desktop\\extra\\20180227.csv", columns=head, index=False)

if __name__ == '__main__':
    dirs('D:\\baiduQA_new')
    creat_list()
    # data = readurl('D:\\baiduQA_new\\view_id=f2165a24626975510000.html')
    # analyzer(data)
    # print(len(ask_answer))
    # for t in ask_answer:
    #     print(t)
