import requests
from bs4 import BeautifulSoup

# URLs
SALARY_URL = 'https://www.bls.gov/emp/tables/unemployment-earnings-education.htm'
HOUSING_URL = 'https://www.rentcafe.com/average-rent-market-trends/us/tn/'
TRANSPORT_URL = 'https://www.nerdwallet.com/article/loans/auto-loans/average-monthly-car-payment'
CLOTHING_URL = 'https://jinfengapparel.com/what-is-the-typical-price-range-for-clothing-in-the-usa/'
FOOD_URL = 'https://www.nerdwallet.com/article/finance/how-much-should-i-spend-on-groceries'

def scrape_salaries():
    response = requests.get(SALARY_URL)
    soup = BeautifulSoup(response.content, features="html.parser")
    #print(soup)
    return soup

def scrape_housing_data():
    response = requests.get(HOUSING_URL)
    soup = BeautifulSoup(response.text, features="html.parser")
    #print(soup)
    return soup

def scrape_transportation_data():
    response = requests.get(TRANSPORT_URL)
    soup = BeautifulSoup(response.text, features="html.parser")
    #print(soup)
    return soup

def scrape_clothing_data():
    response = requests.get(CLOTHING_URL)
    soup = BeautifulSoup(response.text, features="html.parser")
    #print(soup)
    return soup

def scrape_food_data():
    response = requests.get(FOOD_URL)
    soup = BeautifulSoup(response.text, features="html.parser")
    #print(soup)
    return soup

def write_html(output_filename, html_input):
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(str(html_input))

def main():
    # Scrape housing
    housing_data = scrape_housing_data()
    write_html('housing_options.html', housing_data)

    # Scrape transportation
    transport_data = scrape_transportation_data()
    write_html('transport_options.html', transport_data)

    # Scrape clothing
    clothing_data = scrape_clothing_data()
    write_html('clothing_options.html', clothing_data)

    # Scrape food
    food_data = scrape_food_data()
    write_html('food_options.html', food_data)

    # Scrape salary/careers
    career_data = scrape_salaries()
    write_html('careers.html', career_data)

    print("Scraping complete. HTML files are ready.")


if __name__ == "__main__":
        main()