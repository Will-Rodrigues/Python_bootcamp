import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

account_sid = ''
auth_token = ''

yesterday = datetime.now().date() - timedelta(days=1)
before_yesterday = yesterday - timedelta(days=1)
three_days_before = yesterday - timedelta(days=2)
four_days_before = yesterday - timedelta(days=3)

stock_parameters = {
    "function": 'TIME_SERIES_INTRADAY',
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "compact",
    "apikey": ''
}

stock_request = requests.get(
    url="https://www.alphavantage.co/query", params=stock_parameters)
stock_time = stock_request.json()['Time Series (60min)']

if datetime.now().date().weekday() == 0:
    last_stock = stock_time[str(three_days_before) + ' 20:00:00']
    before_last_stock = stock_time[str(four_days_before) + ' 20:00:00']
elif datetime.now().date().weekday() == 1:
    last_stock = stock_time[str(yesterday) + ' 20:00:00']
    before_last_stock = stock_time[str(four_days_before) + ' 20:00:00']
else:
    last_stock = stock_time[str(yesterday) + ' 20:00:00']
    before_last_stock = stock_time[str(before_yesterday) + ' 20:00:00']

last_stock_close = float(last_stock['4. close'])
before_last_stock_close = float(before_last_stock['4. close'])

percentage = (abs(before_last_stock_close - last_stock_close) /
              before_last_stock_close) * 100

if percentage >= 5 or percentage <= -5:
    news_parameters = {
        'q': COMPANY_NAME,
        'apiKey': ''
    }

    news_request = requests.get(
        url='https://newsapi.org/v2/everything', params=news_parameters)
    news = news_request.json()['articles']

    news_1 = f"Headline: {news[0]['title']}\nBrief: {news[0]['description']}"
    news_2 = f"Headline: {news[1]['title']}\nBrief: {news[1]['description']}"
    news_3 = f"Headline: {news[2]['title']}\nBrief: {news[2]['description']}"

    sending_news = [news_1, news_2, news_3]

    for article in sending_news:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"{percentage}%\n{article}",
                from_="",
                to=""
            )
        print(message.status)
