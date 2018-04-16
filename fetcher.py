import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

class bcolors:
        green = "\033[92m"
        end = "\033[0m"

webpage = urlopen(sys.argv[1])
soup = BeautifulSoup(webpage.read(), "lxml")

url = soup.find("meta", property="og:url")

if url:
        print(bcolors.green + "FETCHED URL:\n" + bcolors.end + url["content"])
else:
        print("No meta url given")
