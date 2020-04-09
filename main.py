"""
A notification system for COVID-19 (Coronavirus) status
"""

from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="icon_path/icon.ico",
        timeout=10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    while True:
        # notifyMe("Rohit", "Let's stop this virus spread.!!")
        myHtmlData = getData('https://www.mohfw.gov.in/')
        # print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]

        itemList = myDataStr.split('\n\n')
        states = ['Bihar', 'Maharashtra', 'Delhi']
        for item in itemList[0:31]:
            dataList = (item.split('\n'))[1:]
            if dataList[1] in states:
                nTitle = 'Cases of Covid-19'
                nText = f"State : {dataList[1]}\nTotal Confirmed Cases : {dataList[2]}\nCured/Discharged : {dataList[3]}\nDeath : {dataList[4]}"
                notifyMe(nTitle, nText)
                time.sleep(4)
        time.sleep(3600)
