from sys import argv, exit
import requests

def main():
	try:
		print(argv)
		api_key = argv[1]
	except IndexError:
		print("Please pass in an API key")
		exit(0)

	city = input("For which city do you need weather?")
	country = input("What is the country?")
	location = city,country.lower()

	payload = {
		"appid": api_key,
		"q": location,
		"units": "imperial",
	}

	r = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)

	print(r.url)
	weather = r.json()
	print("Current Temp: {}".format(weather["main"]["temp"]))

if __name__ == '__main__':
	main()