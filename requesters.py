from fake_useragent import UserAgent
from requests import Response
from bs4 import BeautifulSoup
from loguru import logger
import requests


def headers() -> dict:
    user_agent: UserAgent = UserAgent()
    return {
        "User-Agent": user_agent.random,
        "Content-Type": "application/json"
    }


def get_hidemy_page_request() -> Response:
    request_url: str = "https://hidemy.name/ru/proxy-list/"
    response: Response = requests.get(url=request_url, headers=headers()).content
    logger.info(f"Got page with proxy table")
    return response


def check_work_proxy_request(proxy: dict) -> int:
    session = requests.Session()
    request_url: str = 'https://www.google.com/'
    try:
        response = session.get(url=request_url, headers=headers(), proxies=proxy)
        logger.info(f"Checked proxy '{proxy.get('http')}'. Status code: {response.status_code} ")
    except ConnectionError as e:
        logger.info(f'Connection error: {e}')
    return response.status_code