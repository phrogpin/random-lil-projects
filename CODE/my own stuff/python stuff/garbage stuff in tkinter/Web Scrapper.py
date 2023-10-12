import requests 
import tkinter as tk
from bs4 import BeautifulSoup 

# the function to scrape and print out the given websites HTML code and text content.

def scrapper(url):
    url = url_entry.get() # gets the url from the Entry widget
    
    try: 
        
        # send an HTTP GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status() # check for HTTP request errors
        
        # get the HTML code of the page
        html = response.text
        
        # parse  the html using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        quotes  = [quote.text for quote in soup.find_all('p')] #replace p with the tags/attirbutes you want to find
        for quote in quotes:
            output_text.insert("end", quote + "\n") # display quotes in the text widget
            
        output_text.delete("1.0", "end") # clears the previous text in the output_text widget
        
    except requests.exceptions.RequestException as e: 
        output_text.delete("1.0", "end")
        output_text.insert("end", "Error: " + str(e))
    except Exception as e:
        output_text.delete("1.0", "end")
        output_text.insert("end", "Error: " + str(e))
    
    
if __name__ == "__main__":

    # create the main window for the application
    root = tk.Tk()
    root.title("Web Scrapper")
    root.geometry("1000x1000")
    root.configure(background = "light pink")
    
    # create and place widgets in the window 
    url = tk.Label(root, text = "Enter the url of the website you want to devour: ")
    url.pack(pady = 10)
    
    url_entry = tk.Entry(root)
    url_entry.pack(pady = 10)
    
    submit_button = tk.Button(root, text = "Enter", command = scrapper)
    submit_button.pack()
    
    output_text = tk.Text(root, wrap = "word", height = 10, width = 50)
    output_text.pack()
    
    #start the tkinter mainloop
    root.mainloop()
