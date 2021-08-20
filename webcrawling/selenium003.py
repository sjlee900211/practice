import pandas as pd
import requests
from selenium import webdriver
import time


driver = webdriver.Chrome("C:/Myexam/chromedriver/chromedriver.exe")
url = "http://corners.gmarket.co.kr/Bestsellers"
driver.get(url)

items = driver.find_elements_by_css_selector(".best-list:nth-child(3) > ul > li")
len(items)

dict_list = []
for item in items:
    title = item.find_element_by_css_selector(".itemname").text
    link = item.find_element_by_css_selector(".itemname").get_attribute("href")
    o_price = item.find_element_by_css_selector(".o-price").text[:-1]
    s_price = item.find_element_by_css_selector(".s-price").text.split(" ")[0][:-1]
    
    data = {
        "title": title,
        "link": link,
        "o_price": o_price,
        "s_price": s_price,
    }
    
    dict_list.append(data)
df = pd.DataFrame(dict_list)
df.tail()
nodata_indexs = df["o_price"] == ""
df["o_price"][nodata_indexs].tail()
df["s_price"][nodata_indexs].tail()
df[nodata_indexs].tail()
df["o_price"][nodata_indexs] = df["s_price"][nodata_indexs]
df.loc[nodata_indexs].tail()
df.tail()
df["o_price"] = df["o_price"].apply(
    lambda price: price.replace(".", "")).astype("int")
df["s_price"] = df["s_price"].apply(
    lambda price: price.replace(".", "")).astype("int")
df["sale_rate"] = round((1-df["s_price"]/df["o_price"]) * 100, 2)
df.tail()
# df[df["sale_rate"] > 50].sort_values("sale_rate", ascending=False).reset_index(drop=True).head()
driver.quit()