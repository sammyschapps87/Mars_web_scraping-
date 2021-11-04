import re
import pandas as pd
import requests
import datetime as dt
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **path, headless = False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    title = soup.find('div', class_ = 'content_title').get_text()
    print(title)
    paragraph = soup.find('div', class_ = 'article_teaser_body').get_text()
    print(paragraph)
    path = {'executable_path': 'chromedriver.exe'}


    browser = Browser('chrome', **path, headless = False)
    url_image = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    article = soup.find('img', class_='headerimage fade-in')
    print(article)

    full_path = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
    full_path


    url_facts = 'https://galaxyfacts-mars.com/'
    df_facts = pd.read_html(url_facts, header=0)[0]
    df_facts
    df_facts.set_index('Mars - Earth Comparison')


    df_facts.to_html()

    path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **path, headless = False)
    url_images_2 = 'https://marshemispheres.com/'
    browser.visit(url_images_2)
    html = browser.html
    soup = bs(html, 'html.parser')

    h3 = soup.find_all('h3')[0:-1]


    images_hemisphere = []



    for i in h3:
        titles = i.text
        browser.links.find_by_partial_text(titles).click()
        html_en = browser.html
        soup_en = bs(html_en, 'html.parser')
        title = soup_en.find('h2', class_='title').text.replace('Enhanced', '').strip()
        sample = soup_en.find('li')
        imgurl = sample.find('a')['href']
        imgurl = url + imgurl

        hemi_dict = {'title': title, 'img_url': imgurl}
        images_hemisphere.append(hemi_dict)
        browser.links.find_by_partial_text('Back').click()

    
    df = {
        'news_title': title,
        'news_paragraph': paragraph,
        'featured_image': imgurl,
        'facts': df_facts,
        'hemiospheres': images_hemisphere
    }

    browser.quit()
    return df

