import requests
from bs4 import BeautifulSoup
import pandas as pd
import time



url= "https://www.flipkart.com/search?q=mobiles+under+10000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+10000&requestId=578ce714-9566-42f7-98d9-e843aa09b73b&as-backfill=on"
st_link="https://www.flipkart.com"

# method to check access for the url page and get content
def fetch_content(url):
    # try to accees the page for 3 times if the page not loaded
    for i in range(3):
        # Checking for the page is accesable or not
        try:
            req= requests.get(url)
            req.raise_for_status()
            req.encoding
            return req.text
        # if any rror occure it will try again after 5 seconds
        except requests.RequestException as e:
            print(f"Request Failed : {e}")
            print("\n\nWait For few seconds ..........!\n")
            time.sleep(5)
    return None



# method to extract the content in website
def extract_data(req):
    # Intializing lists 
    names=[]
    ratings=[]
    descriptions=[]
    prices=[]


    soup=BeautifulSoup(req,'html.parser')

    # accessing next page link tag
    a_tag= soup.find('a', class_="_9QVEpD").get('href')
    page=st_link+a_tag[0:-1]
    
    pg_num=2

    while pg_num<=10:
        # keep tracking of previous elements length
        prev_names=len(names)
        prev_descps=len(descriptions)
        prev_prices= len(prices)
        prev_ratings=len(ratings)


        soup=BeautifulSoup(req,'html.parser')

    # creating a box div for Fetching only ratings
        main_box_tag=soup.find("div",class_="DOjaWF gdgoEp")



    # fetching product names 
        all_name_tags= soup.find_all("div",class_="KzDlHZ")
        for i in all_name_tags:
            names.append(i.text.strip())


    # fetching product Description Data 
        all_descp_tags= soup.find_all("ul",class_="G4BRas")
        for j in all_descp_tags:
            descriptions.append(j.text.strip())


    # fetching product prices Data 
        all_price_tags= soup.find_all("div",class_="Nx9bqj _4b5DiR")
        for k in all_price_tags:
            prices.append(k.text.strip())


    # fetching product Rating Data using box div 
        all_rating_tags=main_box_tag.find_all("div",class_="XQDdHH")
        for l in all_rating_tags:
            ratings.append(l.text.strip())
        print("page scraping",pg_num)


        # print(len(names))
        # print(len(descriptions))
        # print(len(prices))
        # print(len(ratings))


        # checking for all values are consistent means all values in each column are same
        if len(names)==len(descriptions)==len(prices)==len(ratings):
            
            nxt_page=page+str(pg_num)
            pg_num+=1
        # if the values or not same it will fetch again the same page and remove wrong values
        else:
            names=names[:prev_names]
            prices=prices[:prev_prices]
            descriptions=descriptions[:prev_descps]
            ratings=ratings[:prev_ratings]
            nxt_page=page+str(pg_num)
        

        # calling fetch method with next page url
        req=fetch_content(nxt_page)

       

        if req:
            pass
        else:
            break
    
    # store all data in a dictionary 
    data= {
        "Product Name": names,
        "Product Decription" : descriptions,
        "Price" : prices,
        "Rating" :ratings
    }
    
# Create a DataFrame and store data init 
    df= pd.DataFrame(data)
    print(df)

# save the file 
    file_name="D:\\Abk code\\Python Mini Projects\\products_data.csv"
    df.to_csv(file_name,index=False)
    print("file saved")


req=fetch_content(url)
if req:
    extract_data(req)
else:
    print("The page has no content")












