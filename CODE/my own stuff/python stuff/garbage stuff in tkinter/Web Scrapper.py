import tkinter as tk
from tkinter import Scrollbar
import requests 
from bs4 import BeautifulSoup 


# the function to scrape and print out the given websites HTML code and text content.

def scrapper():
    url = url_entry.get() # gets the url from the Entry widget
    
    try: 
        
        # send an HTTP GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status() # check for HTTP request errors
        
        # get the HTML code of the page
        html = response.text
        
        # parse  the html using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        text_content = soup.get_text() # get the text content of the page
        
        # clear existing content inside of the text widgets
        html_text.delete("1.0", "end")
        text_content_text.delete("1.0", "end")
        
        # insert the HTML code and text content into the text widgets
        html_text.insert("1.0", html)
        text_content_text.insert("1.0", text_content)
        
    except requests.exceptions.RequestException as e: 
        html_text.delete("1.0", "end")
        text_content_text.delete("1.0", "end")
        html_text.insert("end", f"Error: {e}")
        text_content_text.insert("end", f"Error: {e}")
    except Exception as e:
        html_text.delete("1.0", "end")
        text_content_text.delete("1.0", "end")
        html_text.insert("end", f"An error occured: {e}")
        text_content_text.insert("end", f"An error occured: {e}")
    

# create the main window for the application
root = tk.Tk()
root.title("Web Scrapper")
root.geometry("1000x1000")
root.configure(background = "light pink")
    
# create and place widgets in the window 
url = tk.Label(root, text = "Enter the url of the website you want to devour: ")
url.pack(pady = 10)
    
url_entry = tk.Entry(root)
url_entry.pack(pady = 100)
    
submit_button = tk.Button(root, text = "Enter", command = scrapper)
submit_button.pack()
    
    
# creates and configures scrollbars for the text widgets
html_scrollbar = Scrollbar(root)
html_scrollbar.pack(side = "right", fill = "y")
text_content_scrollbar = Scrollbar(root)
text_content_scrollbar.pack(side = "right", fill = "y")

# creates the text widgets
html_text = tk.Text(root, wrap = "word", height = 20, width = 200, yscrollcommand = html_scrollbar.set)
html_text.pack()
text_content_text = tk.Text(root, wrap = "word", height = 20, width = 200, yscrollcommand = text_content_scrollbar.set)
text_content_text.pack()
    
#start the tkinter mainloop
root.mainloop()
