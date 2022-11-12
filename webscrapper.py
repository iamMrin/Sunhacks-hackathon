import requests
from bs4 import BeautifulSoup as bs
#take input as string from name
name=input("Enter Place: ") 


req = requests.get("https://en.wikipedia.org/wiki/"+name).text
req1=requests.get("https://simple.wikipedia.org/wiki/"+name).text
req2=requests.get("https://
soup = bs(req, 'html.parser')
soup1 = bs(req1, 'html.parser')
latitude = soup.find("span", {"class": "latitude"})
longitude = soup.find("span", {"class": "longitude"})

#coordinates=name.split(" latitude")

lat = latitude.text #latitude
long = longitude.text #longitude
#first paragraph and second paragraph to be displayed 

#remove all numbers and special characters and brackets from the paragraph 0 and print
para=soup1.find_all('p')
newLat = lat.replace("°", ".").replace("′", "").replace("″", "").replace(" ", "").replace("N", "").replace("W", "").replace("E", "").replace("S", "")

newLong = long.replace("°", ".").replace("′", "").replace("″", "").replace(" ", "").replace("N", "").replace("W", "").replace("E", "").replace("S", "")

print(newLat)
#o=int(longitude.text)
print(newLong)
print(para[1].text)



dict = {
    name: {
        "short_desc": para[1].text,
        "longitude": newLong,
        "latitude": newLat,
    "id":1,
    }
}

# print(dict[name])
# print(dict)

#print(n,o)






