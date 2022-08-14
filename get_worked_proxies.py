from parse_proxy_table import parse_proxy_table
from requesters import check_work_proxy_request
from loguru import logger


def get_twenty_ms_worked_proxies() -> list:
    proxies: list = parse_proxy_table()

    worked_proxies: list = []
    for proxy in proxies:
        ms_to_num: int = int(proxy[3].split(' ')[0])
        if ms_to_num <= 20 and proxy[4] == 'HTTP':
            full_proxy: str = f"http://{proxy[0]}:{proxy[1]}"
            check_proxy: int = check_work_proxy_request(proxy={'http': full_proxy})
            if check_proxy == 200:
                worked_proxies.append(full_proxy)
                return worked_proxies
            else:
                logger.info("Finded proxy is not work. Check response status code in terminal")

start_script = get_twenty_ms_worked_proxies()
