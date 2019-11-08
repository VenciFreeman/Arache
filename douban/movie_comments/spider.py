from bs4 import BeautifulSoup
import re
from time import sleep
import random
import urllib
import requests
 
url = "https://douban.com/accounts/login"
formData = {
  "redir": "https://www.douban.com",
  "form_email": "**************",
  "form_password": "**************",
  "login": u'登录',
  'source': 'None',
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/26.0.1656.60 Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
     "Referer": "https://douban.com/accounts/login",
     "Host": "accounts.douban.com",
     "Connection": "Keep-Alive",
     "Content-Type": "application/x-www-form-urlencoded"
     }
s = requests.session()

r_ = s.post(url, data=formData, headers=headers)
page_ = r_.text

"""---------------------------------------------------------------------------------"""

"""---------------------------------------------------------------------------------"""
target = "https://movie.douban.com/subject/1292052/comments"
"""------------------------------------------------------------------------ params"""
number = 0
href = "?start=220&limit=20&sort=new_score&status=P&percent_type="
count = 0

def process_h3(soup, fp):
  global number
  h3s = soup.findAll("h3")
  for i in h3s:
    aa = i.span.next_siblings
    bb = aa.__next__().next()
    number += 1
    if number % 100 == 0:
      print (number)
    if len(bb) == 4:
      fp.write(bb[2].attrs["class"][0][-2:-1].encode("utf8"))
      fp.write(" ".encode("utf8"))
      cc = i.next_siblings
      cc.__next__()
      dd = cc.__next__().get_text().strip()
      ee = dd.replace('\n', " ")
      fp.write(ee.encode("utf8"))
      fp.write('\n'.encode("utf8"))

def find_next(soup):
  global target
  global href
  line = soup.findAll("a", {"class", "next"})
  if len(line) == 0:
    return None
  else:
    href = line[0].attrs["href"]
    print(href)
    return target + href

def main():
  global href
  global target
  global headers
  global count
  movie = s.get(target)
  page_movie = movie.text
  soupMovie = BeautifulSoup(page_movie, "html.parser")
  numb_ = soupMovie.findAll("ul", {"class": "fleft"})
  print ("total:", re.findall('(\d+)', numb_[0].text)[0])
  movieName = soupMovie.find("title").get_text()[2:-3]
  print (movieName)
  with open("x" + ".txt", 'wb+') as fp:
    process_h3(soupMovie, fp)
    while True:
      inter = random.gauss(9, 2)
      time = inter if inter > 2.1 else 2.1
      sleep(time)
      next_ = find_next(soupMovie)
      if next_ is None:
        print ("Paused.")
        count = count + 1
        sleep(1000)
        if count:
          break
      try:
        soupMovie = BeautifulSoup(s.get(next_, timeout=10).text)
        process_h3(soupMovie, fp)
      except:
        sleep(100)
        try:
          soupMovie = BeautifulSoup(s.get(next_, timeout=10).text)
          process_h3(soupMovie, fp)
        except:
          break
main()

        
