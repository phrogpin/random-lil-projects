import requests
from bs4 import BeautifulSoup

# Function to scrape and print HTML code and text content
def scrapper(url):
    
    try:
        # Send an HTTP GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        # Get the HTML content of the page
        html = response.text

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Print the HTML code
        print("-------- HTML Code --------")
        print(html)

        # Print the text content
        print("-------- Text Content --------")
        text = soup.get_text()
        print(text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    user_url = input("Enter the URL of the website you want to scrape: ")
    scrapper(user_url)