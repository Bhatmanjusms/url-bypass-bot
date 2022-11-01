import time

import cloudscraper
import PyBypass as bypasser
from bot import GDTOT_CRYPT, app
from bs4 import BeautifulSoup
from pyrogram import filters


@app.on_message(filters.regex(r'https?://[^\s]+'))
def bypass(_, msg):
    url = msg.matches[0].group(0)
    nam = msg.text.split()[1] if len(msg.text.split()) == 2 else None
    x = msg.reply(f"Bypassing __`{url}`__...")
    try:
        if "htpmovies.lol" in url:
            bypassed = htpmovies_bypass(url)
        if "privatemoviez.buzz" in url:
            bypassed = privatemoviz_bypass(url)
        else:
            name = nam or None
            gdtot_crypt = (GDTOT_CRYPT or None) if "gdtot" in url else None
            bypassed = bypasser.bypass(url, name=name, gdtot_crypt=gdtot_crypt)
    except Exception as e:
        return msg.reply(e)
    x.delete()
    msg.reply_text(f"**BYPASSED URL:** `{bypassed}`")


def htpmovies_bypass(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    r = client.get(url, allow_redirects=True).text
    j = r.split('("')[-1]
    url = j.split('")')[0]
    param = url.split("/")[-1]
    DOMAIN = "https://go.theforyou.in"
    final_url = f"{DOMAIN}/{param}"
    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")
    try: inputs = soup.find(id="go-link").find_all(name="input")
    except: return "Incorrect Link"
    data = { input.get('name'): input.get('value') for input in inputs }
    h = { "x-requested-with": "XMLHttpRequest" }
    time.sleep(10)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except Exception:
        return "Something went wrong :("



def privatemoviz_bypass(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    r = client.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    test= soup.text
    param = test.split('console.log("')[-1]
    url = param.split('");')[0]
    param = url.split("/")[-1]
    DOMAIN = "https://go.kinemaster.cc"
    final_url = f"{DOMAIN}/{param}"
    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")
    try: inputs = soup.find(id="go-link").find_all(name="input")
    except: return "Incorrect Link"
    data = { input.get('name'): input.get('value') for input in inputs }
    h = { "x-requested-with": "XMLHttpRequest" }
    time.sleep(10)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except Exception:
        return "Something went wrong :("