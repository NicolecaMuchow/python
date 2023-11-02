""" Description: Topic challenge 7B Web Scraping
    Author: Nicole Muchow
    Date: October 21, 2023       
    Usage: Using HTML parser to scrape data from site."""

from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    """Parses through html to find a piece of information."""

    def __init__(self):
        """Initializes the MyHTMLParser class."""
        super().__init__()
        self.table = False
        self.colour = False
        self.colours = {}
        self.colour_names = ""

    def handle_starttag(self, tag, attrs):
        """Handles html start"""
        try:
            if tag == "td":
                self.table = True
            if attrs[0][1].startswith('background-color'):
                self.colour = True
        except:
            pass

    def handle_data(self, data):
        """Handles data within html tags"""
        if self.table and self.colour:
            self.colour_names = data
            print(data)

        if self.table and data.startswith("#"):
            self.colours[self.colour_names] = data
            print(data)

    def handle_endtag(self, tag):
        """Handles html end tags"""
        if tag == "td" and self.table:
            self.table = False
            self.colour = False



def main():
    """A Method to run the main MyHTMLParser class"""
    myparser = MyHTMLParser()

    with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
        html = str(response.read())
        myparser.feed(html)

    for colour_name, hex_number in myparser.colours.items():
        print(f"{colour_name} {hex_number}")

    print(f"Total colors: {len(myparser.colours)}")
    input("Press enter to exit")


if __name__ == "__main__":
    main()
