#Mars Photo Viewer
#The following code will return photos from Mars taken from NASAs Curiosity, Opportunity, and Spirit rovers

#Visit this page for the API calls from NASA. Browse APIs, then select Mars Rover Photos
#https://api.nasa.gov/

#in the space below, create your code that reaches the desired outcome. You may use old code of yours to accomplish this task as you see fit

#YOU MAY NOT USE MORE THAN 35 LINES OF CODE. COMMENTS AND BLANK LINES DO NOT COUNT TOWARDS THIS REQUIRMENT
#YOU MUST HAVE AT LEAST 1 COMMENT LINE FOR EVERY 4 LINES OF CODE

#IMPORTS

#requests is a library we will use to make HTTP requests
import requests
#PIL stands for "Photo Imaging Library". We will use it to display our image
from PIL import Image
#io means Input/Output. BytesIO allows us to store information and recall it. It is like an advanced variable.
from io import BytesIO

def fetch_apod(mars_url, api_key):
    url = mars_url+api_key
    print(url)
    response = requests.get(url)
    data = response.json()
    return data

mars_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key="
api_key = "jBrPSQpKkp9DVNAqvmZWd1dBPF2NQ1q4tFgqzSrM"
mars_data = fetch_apod(mars_url,api_key)
print(mars_data)

if 'url' in mars_data:
    print("Title:", mars_data['title'])
    print("Date:", mars_data['date'])
    print("Explanation:", mars_data['explanation'])
    print("HD URL:", mars_data.get('hdurl', "Not available"))
    print("URL:", mars_data['url'])

    # Open and display the image
    response = requests.get(mars_data['url'])
    image = Image.open(BytesIO(response.content))
    image.show()
#otherwise, if it did not have a url...
else:
    print("Error:", mars_data.get('msg', 'Unknown error'))
