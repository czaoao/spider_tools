from bs4 import BeautifulSoup
import requests
from flask_mail import Message
from plugins import mail
from redis import Redis


def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_movie_list():
    soup = get_soup("http://www.dysfz.vip/")
    movie_list = soup.select(".movie-list li")
    for movie in movie_list[6:]:
        href = movie.select("h2 a")[0].attrs.get("href")
        title = movie.select("h2 a")[0].get_text()
        try:
            score = movie.select(".des .dbscore b")[0].get_text()
        except:
            score = "暂无评分"
        conn = Redis(host='localhost', port=6379, db=10)
        if not conn.get(href):
            message = Message(subject="New Movie", recipients=['717842816@qq.com'], body="%s \r %s \r %s"%(title, href, score))
            mail.send(message)
            conn.set(href, title)




