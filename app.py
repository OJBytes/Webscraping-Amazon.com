import json
from bs4 import BeautifulSoup


'''
html= download_webpage("examplesite.com"):
    if html is None:
print('error getting Html')'''


# Read index.html file
with open('index.html', 'r', encoding="utf-8") as f:
    html = f.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

divs = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')

# Extract data from each div
data = []
for div in divs:
    # Find img with class="s-image" and get link=img.src
    img = div.find('img', class_='s-image')
    link = img['src'] if img else ''

    # Find span with class="a-size-medium a-color-base a-text-normal" and get title=span.text
    span_title = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    title = span_title.text.strip() if span_title else ''

    # Find span with class="a-size-base" and get rating=span.text
    span_rating = div.find('span', class_='a-size-base')
    rating = span_rating.text.strip() if span_rating else ''

    # Find span with class="a-price-whole" and get price=span.text
    span_price = div.find('span', class_='a-price-whole')
    price = span_price.text.strip() if span_price else ''

    # Find span with class="a-size-base s-underline-text" and get sales=span.text
    span_sales = div.find('span', class_='a-size-base s-underline-text')
    sales = span_sales.text.strip() if span_sales else ''

    # Append data to list
    data.append({
        'link': link,
        'title': title,
        'rating': rating,
        'price': price,
        'sales': sales
    })

# Open data.json and store data
with open('data.json', 'w') as f:
    json.dump(data, f)
