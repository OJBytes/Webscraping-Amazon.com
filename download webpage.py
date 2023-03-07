import requests

# URL of the webpage
url = "http://books.toscrape.com/"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the HTML content of the webpage
    html_content = response.content.decode("utf-8")

    # Loop through the links in the HTML content and download each page
    for link in html_content.split('href="')[1:]:
        link = link.split('"')[0]
        if "http" not in link:
            link = url + link

        # Make a GET request to the link
        response = requests.get(link)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the HTML content of the webpage
            html_content = response.content.decode("utf-8")

            # Save the HTML content to a file
            with open(link.split("/")[-1], "w") as file:
                file.write(html_content)
else:
    print("Error: Could not download webpage")
