# coding=utf-8
import xml.etree.ElementTree as ET
import os
import sys

w = open('E:\\seedWords\\seedWords.txt', 'w', encoding='utf-8')
w1 = open('F:\\LDC2005E18\\LTP词林\\词林.txt', 'rt', encoding='utf-8')

arr = {}
arrword = []
synonym = []
path = 'F:\\LDC2005E18\\trainData'


def getSeedWords():
    dirs = os.listdir(path)
    for dir in dirs:
        # print(dir)
        # 打开xml文档
        f = open(path + '\\' + dir, 'rt', encoding='utf-8')
        # 得到文档元素对象
        tree = ET.parse(f)
        root = tree.getroot()
        document = root[0]
        for event in document.iter('event'):
            for event_mention in event.iter('event_mention'):
                for anchor in event_mention.iter('anchor'):
                    seedWord = anchor[0].text.replace("\n", "")
                    item = seedWord + '+' + event.get('TYPE') + '+' + event.get('SUBTYPE')
                    if (seedWord not in arr):
                        arrword.append(seedWord)
                        arr[seedWord] = event.get('TYPE') + '+' + event.get('SUBTYPE')
                        w.write(item + '\n')
        f.close()
    w.close()


getSeedWords()
#
dict = {}
devcodes = {}

def getSynonymWords():
    global count
    count = 0
    for line in w1.readlines():
        line = line.strip('\n')
        words = line.split(' ')
        code = words[0]
        code = code[0:5]
        if code not in dict:
            dict[code] = words[1:]
        else:
            # print("'key is %s,value is %s'"%(code,dict[code]))
            dict[code] = dict[code]+words[1:]
    # for code in dict:
    #     print("'key is %s,value is %s'" % (code, dict[code]))

    for seedword in arrword:
        for code in dict:
            if seedword in dict[code]:
                existword = ""
                for synword in dict[code]:
                    if synword in arrword:
                        count = count+1
                        existword = existword +" " + synword
                if count > 4:
                    devcode = code
                    devcodes[devcode] = arr[seedword]
                    count = 0
                else:
                    count = 0
    for i in devcodes:
        print("'key is %s,value is %s'" % (i, devcodes[i]))

def writeDevWords():
    w2 = open('E:\\seedWords\\devWords.txt', 'w', encoding='utf-8')
    for i in devcodes:
        for word in dict[i]:
            if word not in arrword:
                w2.write(word + "+"+devcodes[i]+"\n")


getSynonymWords()
writeDevWords()
# def getDevWords():







