from bs4 import BeautifulSoup

qadata=[]
def regex_data(path):
    soup = BeautifulSoup(open(path, encoding='utf-8', errors='ignore'), 'html.parser', from_encoding='utf-8')
    data=[link.get_text() for link in soup.find_all('p')]
    return data

def creatList(datalist):
    for data in datalist:
        qadata.append(data)

if __name__ == '__main__':
    data=regex_data('C:\\Users\\User\\Desktop\\[一站到底题库大全]《一站到底》最全的题库.html')
    # print(data[4])
    # print(data[len(data)-3])
    data=data[4:len(data)-3]
    # for i in range(len(data)):
    #     if '149、 奥林匹克运动会的发源地是' in data[i]:
    #         print(i)
    #     if '黄宗羲 顾炎武 王夫之 王充' in data[i]:
    #         print(i)
    #         print('----------------')
    #     if '301、大家都害怕猛兽，但猛兽也有致命的弱点如狼' in data[i]:
    #         print(i)
    #     if 'A、白居易B、王维C、刘禹锡D、李商隐' in data[i]:
    #         print(i)
    #         print('----------------')
    #     if '391、“人有悲欢离合，月有阴晴圆缺”' in data[i]:
    #         print(i)
    #     if 'A、杜甫B、李白C、陶渊明' in data[i]:
    #         print(i)
    #         print('----------------')
    #
    #     if '1012、《家》《春》《秋》' in data[i]:
    #         print(i)
    #     if 'A 30 B40 C50' in data[i]:
    #         print(i)
    #         print('----------------')
    creatList(data[401:629])
    creatList(data[668:706])
    creatList(data[777:784])
    creatList(data[1453:1610])
    print(len(qadata))