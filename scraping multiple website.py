import httpx
from selectolax.parser import HTMLParser


def get_data(store, url, selector):
    resp = httpx.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        },
    )
    html = HTMLParser(resp.text)
    price = html.css_first(selector).text().strip()
    return {"store": store, "price": price}


def main():
    results = [
        get_data("Amazon", "https://www.amazon.com/dp/B07P6Y7954/", "span.a-offscreen")
    ]

    print(results)


if __name__ == "__main__":
    main()
 