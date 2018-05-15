import sys

import requests
from bs4 import BeautifulSoup
from collections import namedtuple

weatherReport = namedtuple('WeatherReport', 'location, cond, temp, unit')


def print_headers() -> None:
    print('------------------------------')
    print('         Weather app')
    print('------------------------------')


def ask_for_zipcode() -> str:
    return input('What zip code do you want the weather for ? (00000) ')


def cleanup_text(text: str) -> str:
    if not text:
        return text

    text = text.strip()
    return text


def extract_data_from_html(html: str) -> weatherReport:
    try:
        soup = BeautifulSoup(html, 'html.parser')
        city_header = soup.find('city-header')
        location = city_header.find('h1').get_text()
        cond = soup.find(class_='condition-icon').find('p').get_text()
        temp = soup.find(class_='wu-value wu-value-to').get_text()
        unit = soup.find('display-unit').find(class_='wu-label').get_text()

        location = cleanup_text(location)
        cond = cleanup_text(cond)
        temp = cleanup_text(temp)
        unit = cleanup_text(unit)

        return weatherReport(location, cond, temp, unit)
    except Exception:
        print('> Error append. Try again later')
        sys.exit()


def print_weather(weather: weatherReport) -> None:
    print('The weather in {} is {} {} and {}'.format(
        weather.location, weather.temp, weather.unit, weather.cond
    ))


def main():
    print_headers()
    zipcode = ask_for_zipcode()
    html = get_html_from_web(zipcode)
    weather = extract_data_from_html(html)
    print_weather(weather)


def get_html_from_web(zipcode: str) -> str:
    url = 'https://www.wunderground.com/weather/{}'.format(
        zipcode)
    source = requests.get(url)
    return source.text


if __name__ == '__main__':
    main()
