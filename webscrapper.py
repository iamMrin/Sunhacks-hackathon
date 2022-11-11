import requests
from bs4 import BeautifulSoup as bs
#take input as string from name
name=input("Enter Place: ") 


req = requests.get("https://en.wikipedia.org/wiki/"+name).text
soup = bs(req, 'html.parser')
latitude = soup.find("span", {"class": "latitude"})
longitude = soup.find("span", {"class": "longitude"})

#coordinates=name.split(" latitude")

lat = latitude.text #latitude
long = longitude.text #longitude
#first paragraph and second paragraph to be displayed 
para=soup.find_all('p')



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
#OPEN INDEX.HTML WITH FILE OPERATIONS AND ADD TEXT TO IT ACCORDING TO THE FORMAT
#ADD THE TEXT TO THE FILE
#SAVE THE FILE
f.open("index.html","w")
f.write(dict)
f.close()
#OPEN THE FILE IN BROWSER
import webbrowser
webbrowser.open("index.html")

# f=open("./index.html")
# f.write(dict[id+1])
# f.close()
print(dict[name])
print(dict)

#print(n,o)






