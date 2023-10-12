import requests 
import tkinter as tk
from bs4 import BeautifulSoup 



# the function to display the HTML code and text content of the given website.

def scrapper_input():
    user_input = entry.get() # get text from the entry widget 
    output_label.config(text = f"You entered: {user_input}") # display the text in the label widget
    processed_output = scrapper(user_input) # calls the scrapper def to process, scrape, and output the input 
    output_label.config(text = f"HTML code: {processed_output[0]} \n\n Text content: {processed_output[1]}") # display the processed output in the label widget

# the function to scrape and print out the given websites HTML code and text content.

def scrapper(url):
    
    try: 
        
        # send an HTTP GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status() # check for HTTP request errors
        
        # get the HTML code of the page
        html = response.text
        
        # parse  the html using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # get contents of the page 
        text = soup.get_text()
        
        # print the html code and page contents
        print("-----html code and page content-----")
        return html, text # return the html code and text content of the page
        
        
    except requests.exceptions.RequestException as e: 
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    
if __name__ == "__main__":

    # create the main window for the application
    root = tk.Tk()
    root.title("Web Scrapper")
    root.geometry("1000x1000")
    root.configure(background = "light pink")
    
    # scroll bar
    scrollbar = tk.Scrollbar(root, command = text_output.yview)
    scrollbar.pack(side = "right", fill = "y")
    text_output.config(yscrollcommand = scrollbar.set)
    
    # create and place widgets in the window 
    label = tk.Label(root, text = "Enter the url of the website you want to devour: ")
    label.pack(pady = 10)
    
    entry = tk.Entry(root)
    entry.pack(pady = 10)
    
    submit_button = tk.Button(root, text = "Enter", command = scrapper_input)
    submit_button.pack()
    
    output_label = tk.Label(root, text = "")
    output_label.pack(pady = 10)
    
    #start the tkinter mainloop
    root.mainloop()
    

'''
# the function to scrape and print out the given websites HTML code and text content.

def scrapper(url):
    
    try: 
        
        # send an HTTP GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status() # check for HTTP request errors
        
        # get the HTML code of the page
        html = response.text
        
        # parse  the html using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # print the html code 
        print("-----html code-----")
        print(html)
        
        # print the text content of the page 
        print("---text content---")
        text = soup.get_text()
        print(text)
        
        
    except requests.exceptions.RequestException as e: 
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
'''