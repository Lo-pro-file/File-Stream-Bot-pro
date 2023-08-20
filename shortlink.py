import os
import asyncio
from os import getenv, environ
from asyncio import TimeoutError
from shortzy import Shortzy
from Adarsh.vars import Var

SHORTENER_API = str(getenv('SHORTENER_API', 'e0867ce24e2238645541bf7651be2217b4cd5dd1'))
SHORTENER_WEBSITE = str(getenv('SHORTENER_WEBSITE', 'shorturllink.in'))


shortzy = Shortzy(SHORTENER_API, SHORTENER_WEBSITE)

async def get_shortlink(link):
    if not SHORTENER_API or not SHORTENER_WEBSITE:
        return link

    try:
        x = await shortzy.convert(link, silently_fail=True)
    except Exception:
        x = await get_shortlink_sub(link)
    return x


async def get_shortlink_sub(link):
    url = f'https://{SHORTENER_WEBSITE}/api'
    params = {'api': SHORTENER_API, 'url': link}
    scraper = cloudscraper.create_scraper() 
    r = scraper.get(url, params=params)
    return r.json()["shortenedUrl"]
