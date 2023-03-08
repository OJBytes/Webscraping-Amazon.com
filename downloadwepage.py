import requests

url = input("Inpute the url:")
# "https://www.amazon.com/s?k=acer+nitro+5&sprefix=acer+n%2Caps%2C668&ref=nb_sb_ss_ts-doa-p_1_6"


def download_webpage(url, page):
    response = requests.get(url)
    if response.status_code == 200:
        with open(page, "w") as f:
            f.write(response.text)
        return True
    else:
        return False
