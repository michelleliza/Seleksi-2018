import bs4
import json
import copy
import os
import urllib.request
import time

#Scrape Data From A Restaurant's Webpage
def scrape_small_frame(url):
    result = []
    with urllib.request.urlopen(url) as response:
        page = response.read()
    soup = bs4.BeautifulSoup(page, 'html.parser')

    #get restaurant name and region
    name_and_region = soup.find("h2").text
    name_region = name_and_region.strip().split("[")
    name = name_region[0].strip()
    region1 = name_region[1].split("]")
    region2 = region1[0].strip()
    result.append(name)
    result.append(region2)

    #get restaurant cuisine
    cuisine_list = []
    cuisines = soup.find("span", itemprop="servesCuisine")
    if cuisines is None:
        cuisine_list.append("N/A")
    else:
        cuisines2 = cuisines.text.split(",")
        for cuisine in cuisines2:
            cuisine_list.append(cuisine)
    result.append(cuisine_list)

    #get restaurant overall rating
    overallRating = soup.find("span", itemprop="ratingValue").text
    result.append(overallRating)

    #get restaurant flavor rating
    flavorRating = soup.find("div", class_="rate-box-bottom best-rating")
    if flavorRating is None:
        result.append("N/A")
    else:
        flavor = flavorRating.text.strip()
        result.append(flavor)

    #get restaurant price range
    price = soup.find("span", itemprop="priceRange").text.strip().split(" /orang")
    result.append(price[0])

    return result

#Get Restaurant Page's URL From Search Page
def scrape_big_frame(scrape_result, i):
    restaurant_pages = []
    temp_url = 'https://pergikuliner.com'
    urlpage = 'https://pergikuliner.com/restoran/bandung/?page=' + str(i)
    with urllib.request.urlopen(urlpage) as response:
        page = response.read()
    soup = bs4.BeautifulSoup(page, 'html.parser')
    for a in soup.find_all("a", href=True):
        link = str(a['href'])
        if link.startswith("/restaurants/bandung"):
            if link not in restaurant_pages:
                restaurant_pages.append(link)
    for restaurant_page in restaurant_pages:
        new_url = temp_url + restaurant_page
        res = scrape_small_frame(new_url)
        scrape_result.append(res)

#Convert Data List to JSON Data and Write to JSON File
def list_to_json(restaurant_list):
    json_data = {}
    data = []
    #convert to json data
    for restaurant in restaurant_list:
        json_data['Name'] = restaurant[0]
        json_data['Region'] = restaurant[1]
        cuisines_list = restaurant[2]
        cuisines = []
        for cuisine in cuisines_list:
            cuisines.append({"Cuisine": cuisine})
        json_data['Cuisines'] = cuisines
        json_data['OverallRating'] = restaurant[3]
        json_data['FlavorRating'] = restaurant[4]
        json_data['PriceRange'] = restaurant[5]
        data.append(copy.deepcopy(json_data))
    #write file
    output_path = 'data/'
    json_filename = 'restaurant_data.json'
    with open(os.path.join(output_path, json_filename), 'w') as f_out:
        json.dump(data, f_out, indent=4)

#main
res = []
for i in range(1,61):
    scrape_big_frame(res, i)
    time.sleep(2)
list_to_json(res)