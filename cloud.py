import re
import collections
import numpy as np
import jieba
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt

fn = open('./x.txt',encoding = "utf-8") # Please modify the file name
stopwords = [line.strip() for line in open("./del.txt",encoding="utf-8").readlines()]  
string_data = fn.read()
fn.close()

pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
string_data = re.sub(pattern, '', string_data)

seg_list_exact = jieba.cut(string_data, cut_all = False)
object_list = []

for word in seg_list_exact:
    if word not in stopwords:  
        if len(word) == 1:  
            continue  
        else:  
          object_list.append(word)

word_counts = collections.Counter(object_list)
word_counts_top10 = word_counts.most_common(10) # Modify the parameter to change the top num of words

mask = np.array(Image.open('./mask.jpg')) # define background. You need a jpg image as background
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf', # Set font. Plz modify the path.
    mask=mask,
    max_words=100,
    max_font_size=100
)

wc.generate_from_frequencies(word_counts)
image_colors = wordcloud.ImageColorGenerator(mask)
wc.recolor(color_func=image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()
