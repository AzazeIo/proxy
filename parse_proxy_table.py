from requests import Response
from bs4 import BeautifulSoup
from requesters import get_hidemy_page_request


def parse_proxy_table() -> list:
    hidemy_response: Response = get_hidemy_page_request()
    proxy_table: BeautifulSoup = BeautifulSoup(hidemy_response, "lxml").find('table').find('tbody').find_all('tr')

    proxies: list = []
    for row in proxy_table:
        columns: str = row.find_all('td')
        columns: str = [element.text.strip() for element in columns]
        proxies.append([element for element in columns if element])
    return proxies