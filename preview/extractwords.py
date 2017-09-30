from operator import itemgetter
import re

def extractwords(content, topK=10):
    """
    统计出现频率最高的topK个「二元词组」和其频率
    :param content: 统计内容字符串
    :param topK: 统计出现频率最高个数，默认值10
    :return: content出现频率最高的前 topK 个「二元词组」
    """

    # 将内容分词为列表
    words = content.split(" ")
    # 用于统计二元词组个数
    freq = {}
    for i in range(len(words) - 1):
        # 连续词汇一
        w1 = removePunctuation(words[i])
        # 连续词汇二
        w2 = removePunctuation(words[i + 1])
        # 判断两个词汇是否都是词组，长度大于或等于两个
        if len(w1) > 0 and len(w2) > 0:
            w = w1 +" "+w2
            freq[w] = freq.get(w, 0) + 1
    # 按出现频率倒序
    tags = sorted(freq.items(), key=itemgetter(1), reverse=True)
    # 返回前最高topK个字组
    return tags[:topK]

def removePunctuation(word):
    """
    去掉标点符号和空格
    :param word: 
    :return: 
    """

    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+|[+――！，。？、~@#￥%……&*（）]+'
    string = re.sub(r, '', word)
    return string.strip()



fileName = "happiness_seg.txt"
bytes = open(fileName, "rb").read()
content = str(bytes, encoding="utf-8")
words = extractwords(content, topK=10)

print("出现频率最高的前 10 个「二元词组」:")
for word in words:
    print("%s  %s " % (word[0], word[1]))


