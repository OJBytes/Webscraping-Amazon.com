import requests
import validators
import time
from pathlib import Path


def download_webpage(url, filename, chunk_size=8192, max_retries=5, retry_delay=10):
    if not validators.url(url):
        raise ValueError("Invalid URL")

    retries = 0
    while retries < max_retries:
        try:
            with requests.get(url, stream=True) as response:
                response.raise_for_status()

                with open(filename, "wb") as f:
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        f.write(chunk)

                print(f"Downloaded webpage from {url} to {filename}")
                return True

        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}. Retrying...")
            retries += 1
            time.sleep(retry_delay)

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
