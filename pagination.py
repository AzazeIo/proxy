import requests
from requests import Response
from bs4 import BeautifulSoup
from requesters import headers

def pagination_request_page() -> str:
    request_url: str = 'https://hidemy.name/ru/proxy-list/'
    page: Response = requests.get(url=request_url, headers=headers()).content
    pagination = BeautifulSoup(page, "lxml").find_all("div", class_="pagination")[0]
    next_page: BeautifulSoup = pagination.find_all("li", class_="next_array")
    print(next_page)
pagination_request_page()