# Crawler/douban/movie_comments
> A words-analyze tool for the comments on www.douban.com. Written by Python 3.7.
>
> If the runtime prompts for missing librarys, type pip install <library name> directly in the terminal and run.
> Place all files in the same folder.
> Ignore all the warnings.

> ** Still need to improve, especially about anti-crawl. ** 

## spider.py

- A spider that crawls down the comments on the specified page (including ratings and short comments) into a file called x.txt.
  - Line 60 is the comment page URL which needs to be modified;

## form.py

- Segment the words in x.txt file, and the words in del.txt will be excluded.
    - The number in the parentheses in line 15 is the number of top words which can be modified;

## cloud.py

- Segment the x.txt file and generate a word cloud by frequency.
    - Don't forget add mask.jpg as background.
