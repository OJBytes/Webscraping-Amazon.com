import requests
import validators
import time
from pathlib import Path
import sys


def download_webpage(url, filename, chunk_size=8192, max_retries=5, retry_delay=10):
    if not validators.url(url):
        raise ValueError("Invalid URL")
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 Edge/16.16299",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    ]

    retries = 0
    while retries < max_retries:
        try:
            headers = {"User-Agent": user_agents[retries % len(user_agents)]}
            with requests.get(url, stream=True, headers=headers) as response:
                response.raise_for_status()

                with open(filename, "wb") as f:
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        f.write(chunk)

                print(f"Downloaded webpage from {url} to {filename}")
                return True

        except requests.exceptions.RequestException as e:
            choice = input(f"Error downloading {url}: {e}. Retry? (Y/N/C)")
            if choice.upper() == "Y":
                retries += 1
                time.sleep(retry_delay)
            elif choice.upper() == "C":
                sys.exit(0)
            else:
                raise RuntimeError("User chose to stop retrying")

    raise RuntimeError(
        f"Failed to download webpage from {url} after {max_retries} attempts"
    )


def main():
    url = input("Enter the URL: ")
    filename = input("Enter the filename: ")

    try:
        download_webpage(url, Path(filename))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
