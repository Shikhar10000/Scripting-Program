file=open("C:/Users\shikh/Desktop/Scripting-Program-master/Scripting-Program-master/scripting lab/Python/for_file/read.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
file.close();