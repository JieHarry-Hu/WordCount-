import sys
# -c字符数  -s句子数  -w单词数  -l代码行  -b空白行  -m注释行
def count():
    num=0
    sen=0
    words=0
    line=1
    blank_line=0
    comment_line=0
    flag=1
    file=open(sys.argv[2],'r')
    for i in file.read():
        if i != ' ' and i !='\n':
            num += 1
            flag=0
        if i == '.':
            sen += 1
            words += 1
        elif i==',' or i == ' ':
            words += 1
        elif i=='\n' and flag == 0:
            line +=1
            flag=1
        elif i=='\n' and flag == 1:
            blank_line += 1
        if i=='#' or i=='%':
            line -=1
            comment_line += 1
    if sys.argv[1]=='-c':
        print('The number of characters is ',num)
    elif sys.argv[1]=='-s':
        print('The number of sentences is ',sen)
    elif sys.argv[1]=='-w':
        print('The number of words is ',words)
    elif sys.argv[1]=='-l':
        print('The number of lines is ',line)
    elif sys.argv[1]=='-b':
        print('The number of blank_lines is ',blank_line)
    elif sys.argv[1]=='-m':
        print('The number of comment_lines is ',comment_line)
    else:
        print('Your input did not conform to the normal or parameter error')
    file.close()
if __name__ == '__main__':
    count()