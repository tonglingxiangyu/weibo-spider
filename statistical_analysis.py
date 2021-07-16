import os, codecs
import jieba
import re

def get_words(txt,string1):
    txt=re.sub('\d+\.?\d?\w{0,1}','',txt)
    seg_list = jieba.lcut(txt)
    #seg_list=seg_sentence(seg_list)
    excludes = ('排名','话题','类别','阅读','阅读量','量','：','#',' ','','1','\r\n','的','被','一','是','了','能','无','什么','如何','给')
    # for word in excludes:  # 删除之前所规定的词语
    #     seg_list.remove(word)
    counts = {}
    for x in seg_list:
        counts[x] = counts.get(x, 0) + 1
    for word in excludes:
        if counts.get(word,0)!=0:
            del counts[word]
    #print('常用词频度统计结果')
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)# 排序，从大到小
    with open('微博热点/统计分析.txt','a') as fp:
        fp.write(string1+'\n')

        for i in range(10):
            word, count = items[i]
            fp.write('{0:<6}:{1:>3}'.format(word, count)+'\n')
            print('{0:<6}:{1:>3}'.format(word, count))
        fp.write('\n')
        # for (k, v) in counts.most_common(100):
        #     print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * int(v / 3), v))

def seg_sentence(sentence):
    #with open('文件/微博热点/停用词.txt','r','gbk').readline() as fi:  # 这里加载停用词的路径
    fi=[line.strip() for line in codecs.open('微博热点/停用词.txt', 'r','utf-8').readlines()]
    outstr = ''
    for word in sentence:
        if word not in fi:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr
if __name__ == '__main__':
    i=21
    j=22
    date='2020-10-20'
    for flag in range(10):
        if j>=60:
            j=j-60
            i+=1
        string1=date+'_'+str(('%02d')%i)+'-'+str(('%02d')%j)
        with codecs.open('微博热点/'+date+'_'+str(('%02d')%i)+'-'+str(('%02d')%j)+'.txt', 'r', 'gbk') as f:
            txt = f.read()
        j+=10
        get_words(txt,string1)