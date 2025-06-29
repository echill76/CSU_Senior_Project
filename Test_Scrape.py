import requests
from bs4 import BeautifulSoup

SALARY_URL = 'https://www.nerdwallet.com/article/loans/auto-loans/average-monthly-car-payment/'

response = requests.get(SALARY_URL)
soup = BeautifulSoup(response.content, "html.parser")
print(soup)