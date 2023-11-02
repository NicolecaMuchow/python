""" Description: Topic challenge 8A Distributing Code Modules
    Author: Nicole Muchow
    Date: October 28, 2023
    Usage: Generate a source distribution file of the IP address checking app from module 7A"""

from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):
    """Parses through html to find a piece of information."""
    def __init__(self):
        """initializes the MyHTMLParser class."""
        super().__init__()
        HTMLParser.__init__(self)
        self.ip_address = ""

    def handle_data(self, data):
        """Handles the html data and finds IP address."""
        if "Current IP Address: " in data:
            self.ip_address = data.split(":")[1].strip()

def get_ip():
    """A Method to run the main MyHTMLParser class"""
    myparser = MyHTMLParser()
    with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
        html = str(response.read())

    myparser.feed(html)

    return myparser.ip_address

if __name__ == "__main__":
    """Runs get_ip   """
    print(get_ip())

