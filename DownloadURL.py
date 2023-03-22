import requests
import validators
from pathlib import Path


def download_webpage(url, filename, chunk_size=8192):
    if not validators.url(url):
        raise ValueError("Invalid URL")

    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()

            with open(filename, "wb") as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    f.write(chunk)

            print(f"Downloaded webpage from {url} to {filename}")
            return True

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to download webpage from {url}: {e}")


def main():
    url = input("Enter the URL: ")
    filename = input("Enter the filename: ")

    try:
        download_webpage(url, Path(filename))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
