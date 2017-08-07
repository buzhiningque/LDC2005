import os
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse

Path = "F:\\LDC2005E18\\newtest\\"
w = open("E:\\seedWords\\sentence.txt", 'w', encoding='utf-8')
url_get_base = "http://api.ltp-cloud.com/analysis/?"
def changetoXml():

    files = os.listdir(Path)
    for filename in files:
        currentdir = os.path.join(Path, filename)
        print(filename)
        portion = os.path.splitext(filename)
        if portion[1] == '.sgm':
            newname = os.path.join(Path, portion[0] + '.xml')
            print(newname)
            os.rename(currentdir,newname)


def getXmlTurn():
    dirs = os.listdir(Path)
    for dir in dirs:
        filename =dir
        # print(dir)
        # 打开xml文档
        f = open(Path + '\\' + dir, 'rt', encoding='utf-8')
        # 得到文档元素对象
        tree = ET.parse(f)
        root = tree.getroot()
        document = root[3]
        for turn in document.iter('TURN'):
            text = turn.text.replace("\n","")
            arrsentence = text.split("。")
            for sentence in arrsentence:
                sentence = urllib.parse.quote(sentence + "。")
                w.write(sentence+"。"+"\n")
                format = 'plain'
                pattern = 'pos'
                api_key='C1h2I7m445iFXDLDElUkswCbrzLDbxLI9BOg7acm'
                url = (url_get_base
                       +"api_key=" + api_key + "&"
                       +"text="    + sentence + "&"
                       + "format=" + format + "&"
                       + "pattern=" + pattern)
                print(url)
                try:
                    reponse = urllib.request.urlopen(url)
                    content = reponse.read().strip()
                    w.write(str(content,encoding = "utf-8"))
                    w.write("\n")
                except urllib.request.HTTPError as e:
                    print(e.reason)
                    print(e.code)




if __name__ == "__main__":
    # changetoXml()
    getXmlTurn()
