import jieba  
txt = open("./x.txt", encoding="utf-8").read()    
stopwords = [line.strip() for line in open("./del.txt",encoding="utf-8").readlines()]  

words  = jieba.lcut(txt)  
counts = {}  
for word in words:  
    if word not in stopwords:  
        if len(word) == 1:  
            continue  
        else:  
            counts[word] = counts.get(word,0) + 1  
items = list(counts.items())  
items.sort(key=lambda x:x[1], reverse=True)   
for i in range(50):  
    word, count = items[i]  
    print ("{:<10}{:>7}".format(word, count))
