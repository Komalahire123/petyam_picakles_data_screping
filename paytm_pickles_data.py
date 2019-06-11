import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import os

url= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
url1 = requests.get(url)
soup = BeautifulSoup(url1.text,"html.parser")
main_data = soup.find("div",class_="_1LZ3")
# print main_data
pikal_product = main_data.find("div",class_="_3RA-")
# print pikal_product
product = main_data.find("div",class_="_1EI9").span.get_text()
# print product
index=product.split()
index_data=index[1]
product_number = int(index_data)//32+1

def pikel_product_data():
    number = 1
    pickl_list = []
    for i in range(1,product_number+1):

        pikal_url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(i)
        url_data = requests.get(pikal_url)
        soup1 = BeautifulSoup(url_data.text,"html.parser")
        main_data1=soup1.find("div",class_="_1LZ3")
        pikal_product1=soup1.find("div",class_="_3RA-")
        data1 = pikal_product1.find_all("div",class_="_3WhJ")
        for j in data1:
            pickl_dic = {}
            link = j.find("div",class_="_3nWP").get_text()
            name = j.find("div",class_="_2apC").get_text()
            price = j.find("div",class_="_1kMS").get_text()
            pickl_dic["pikal_name"]= name
            pickl_dic["pikal_url"]= url
            pickl_dic["pikal_price"]= price
            pickl_dic["pikal_position"]= number
            number=number+1
            pickl_list.append(pickl_dic)
    return pickl_list
pprint(pikel_product_data())       
