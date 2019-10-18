import sys
# -c字符数  -s句子数  -w单词数  -l代码行  -b空白行  -m注释行
def count():
    num=0
    sen=0
    words=0
    file=open(sys.argv[2],'r')
    for i in file.read():
        if i != ' ' and i !='\n':
            num += 1
        if i == '.':
            sen += 1
            words += 1
        elif i==',' or i == ' ':
            words += 1
    if sys.argv[1]=='-c':
        print('The number of characters is ',num)
    elif sys.argv[1]=='-s':
        print('The number of sentences is ',sen)
    elif sys.argv[1]=='-w':
        print('The number of words is ',words)
    else:
        print('Your input did not conform to the normal or parameter error')
    file.close()
if __name__ == '__main__':
    count()