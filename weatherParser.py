from bs4 import BeautifulSoup

def parse_XML():
    weather_text_data =  open('./yahooWeather/weatherText.txt', 'rb')
    soup = BeautifulSoup(weather_text_data, 'html.parser')

    # print (soup.prettify())
    result = [[],[]]
    for row in soup.find_all("code"):
        description = row.get("description")
        number = row.get("number")
        result[0].append(description)
        result[1].append(number)

    with open("./yahooWeather/cleanedWeatherText.txt", "w") as output_file:
        for i, des in enumerate(result[0]):
            output_file.writelines(des + "\n")
    print (result)

def weather_category():
    cleaned_weather_text_data = open("./yahooWeather/cleanedWeatherText.txt", "rb")
    cleaned_weather_text_data.readline()

    # weather in 4 categories : overcast = [], rain = [], snow = [], sunny = []
    weather = [[], [], [],[]]
    current_cat = 0
    for line in cleaned_weather_text_data:
        weather_str = line.strip().decode('utf-8')
        if weather_str == ",":
            current_cat += 1
        else:
            weather[current_cat].append(weather_str)
    return weather

# print (weather_category())
