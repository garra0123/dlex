from operator import itemgetter
import re

def extract_words(content, topK=10):
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
        # 连续词汇一,去掉标点符号
        w1 = remove_punctuation(words[i])
        # 连续词汇二，去掉标点符号
        w2 = remove_punctuation(words[i + 1])
        if len(w1) > 0 and len(w2) > 0:
            w = w1 +" "+w2
            freq[w] = freq.get(w, 0) + 1
    # 按出现频率倒序
    tags = sorted(freq.items(), key=itemgetter(1), reverse=True)
    # 返回前最高topK个字组
    return tags[:topK]

def remove_punctuation(word):
    """
    去掉标点符号和空格
    :param word: 
    :return: 
    """

    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+|[+――！，。？、~@#￥%……&*（）]+'
    string = re.sub(r, '', word)
    return string.strip()



with open("happiness_seg.txt", encoding='utf-8') as f:
    content = f.read()
    words = extract_words(content, 10)

    print("出现频率最高的前 10 个「二元词组」:")
    for word in words:
        print("%s  %s " % (word[0], word[1]))


