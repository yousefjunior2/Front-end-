# from bs4 import BeautifulSoup
# import requests
# import pandas as pd


# with open('index.html','r') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# # print(soup.prettify())  

# # My_title= soup.title.text  
# # print(My_title)  
# my_div= soup.find('div',class_="footer")
# print(my_div)
from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://arc.dev/remote-jobs")

page_content = page.content

soup = BeautifulSoup(page_content,'lxml')
my_div = soup.find('div',class_="sc-d96f1889-1 jhNHn")
my_company = my_div.find('div',class_="company-name")
print(my_company)