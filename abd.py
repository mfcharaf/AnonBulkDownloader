from lxml import html
from requests import get
import sys
import os
import calendar
import time



def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)
        print(file_name, " ---> Downloaded \n")


print(
"""
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗                ██████╗ ██╗   ██╗██╗     ██╗  ██╗            
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║                ██╔══██╗██║   ██║██║     ██║ ██╔╝            
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║                ██████╔╝██║   ██║██║     █████╔╝             
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║                ██╔══██╗██║   ██║██║     ██╔═██╗             
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║                ██████╔╝╚██████╔╝███████╗██║  ██╗            
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝                ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝            
                                                                                      
██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
Version 0.1
                                                                                      
Coded By OptimOS Prime
TG : @OptimOSPrime
"""
)

# default links file
f = "links.txt"

#check if links file is given in arguments
if len(sys.argv) == 2:
     f = sys.argv[1]

print("Reading links from " ,f)
my_file = open(f, "r")
links = my_file.readlines()
print("Links found in file : ", len(links), "\n\n")

for link in links:
     ts = calendar.timegm(time.gmtime())
     link = str.replace(link, "\n", "")
     print("Downloading " ,link)
     page = get(link)
     tree = html.fromstring(page.content)
     dlink = tree.xpath('//a[@class="btn btn-primary btn-block"]/@href')
     fname = str.replace(os.path.basename(dlink[0]), ".", "_" + str(ts) + ".")
     print("File name : ", fname)
     download(dlink[0], fname)
     

