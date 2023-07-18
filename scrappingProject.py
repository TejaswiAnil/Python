import requests
from bs4 import BeautifulSoup
import pprint # for a cleaner print of the output

res = requests.get('https://news.ycombinator.com/news')
soupObj = BeautifulSoup(res.text,'html.parser')
titles = soupObj.select(".titleline")
scores_td = soupObj.select(".subtext")
#print(f"titles....{titles}")
#print(f"scores_td......{scores_td}")

#sorting the list based on scores
def sort_hacker_news_list(hacker_news_list):
    return sorted(hacker_news_list,key=lambda k: k['scores'],reverse=True)
    #whenever we want to sort a dict this is the way, pass key using lambda
    #reverse: default is false, if we want is descending order make it True


def custom_hacker_news(titles, scores_td):
   # pprint.pprint(scores_td)
    hacker_news=[]
    for index,item in enumerate(titles):
        # title = titles[index].getText()
        title = item.getText()
        #print(title)
        # href = titles[index].a.get('href') we can use item as per the enumerate written
        href = item.a.get('href')
        #print(href)
        points_data = scores_td[index].select(".score")
        if len(points_data):
            points = int(points_data[0].getText().replace(" points",""))
            #print(points)
            if points > 100: #scores above 100 should be dislayed
                hacker_news.append({'title':title, 'link':href, 'scores': points})
    return sort_hacker_news_list(hacker_news)

pprint.pprint(custom_hacker_news(titles,scores_td))

