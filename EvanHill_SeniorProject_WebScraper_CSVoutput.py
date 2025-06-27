import requests
from bs4 import BeautifulSoup
import csv

# URLs
SALARY_URL = 'https://www.bls.gov/emp/tables/unemployment-earnings-education.htm'
HOUSING_URL = 'https://www.rentcafe.com/average-rent-market-trends/us/tn/'
TRANSPORT_URL = 'https://www.nerdwallet.com/article/loans/auto-loans/average-monthly-car-payment'
CLOTHING_URL = 'https://jinfengapparel.com/what-is-the-typical-price-range-for-clothing-in-the-usa/'
FOOD_URL = 'https://www.nerdwallet.com/article/finance/how-much-should-i-spend-on-groceries'

def scrape_salaries():
    response = requests.get(SALARY_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    salary_data = []

    # Find table or structured data (this is fragile; may need adjustments based on site changes)
    salary_section = soup.find('table')
    if salary_section:
        rows = salary_section.find_all('tr')[1:]
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 2:
                education_level = cells[0].get_text(strip=True)
                try:
                    avg_salary = float(cells[1].get_text(strip=True).replace('$', '').replace(',', ''))
                    salary_data.append((education_level, avg_salary))
                except ValueError:
                    continue
    else:
        print("No salary table found.")

def scrape_housing_data():
    response = requests.get(HOUSING_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    housing_data = []

    rent_table = soup.find('table')
    if rent_table:
        rows = rent_table.find_all('tr')[1:]
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 2:
                description = cells[0].get_text(strip=True)
                try:
                    monthly_cost = float(cells[1].get_text(strip=True).replace('$', '').replace(',', ''))
                    housing_data.append((description, monthly_cost))
                except ValueError:
                    continue
    else:
        print("No housing table found.")
    return housing_data

def scrape_transportation_data():
    response = requests.get(TRANSPORT_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    transport_data = []

    # Find table or structured data (this is fragile; may need adjustments based on site changes)
    transport_section = soup.find('table')
    if transport_section:
        rows = transport_section.find_all('tr')[1:]
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 2:
                education_level = cells[0].get_text(strip=True)
                try:
                    avg_salary = float(cells[1].get_text(strip=True).replace('$', '').replace(',', ''))
                    transport_data.append((education_level, avg_salary))
                except ValueError:
                    continue
    else:
        print("No salary table found.")
    return transport_data

def scrape_clothing_data():
    response = requests.get(CLOTHING_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    clothing_data = []
    
    clothing_section = soup.find('table')
    if clothing_section:
        rows = clothing_section.find_all('tr')[1:]
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 2:
                education_level = cells[0].get_text(strip=True)
                try:
                    avg_salary = float(cells[1].get_text(strip=True).replace('$', '').replace(',', ''))
                    clothing_data.append((education_level, avg_salary))
                except ValueError:
                    continue
    else:
        print("No salary table found.")
    return clothing_data

def scrape_food_data():
    response = requests.get(TRANSPORT_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    food_data = []
    
    food_section = soup.find('table')
    if food_section:
        rows = food_section.find_all('tr')[1:]
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 2:
                education_level = cells[0].get_text(strip=True)
                try:
                    avg_salary = float(cells[1].get_text(strip=True).replace('$', '').replace(',', ''))
                    food_data.append((education_level, avg_salary))
                except ValueError:
                    continue
    else:
        print("No salary table found.")
    return food_data

def write_csv(filename, data, headers):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

def main():
    # Scrape housing
    housing_data = scrape_housing_data()
    write_csv('housing_options.csv', housing_data, ['DESCRIPTION', 'MONTHLY_COST'])

    # Scrape transportation
    transport_data = scrape_transportation_data()
    write_csv('transport_options.csv', transport_data, ['DESCRIPTION', 'MONTHLY_COST'])

    # Scrape technology
    tech_data = scrape_clothing_data()
    write_csv('tech_options.csv', tech_data, ['DESCRIPTION', 'MONTHLY_COST'])

    # Scrape food
    food_data = scrape_food_data()
    write_csv('food_options.csv', food_data, ['DESCRIPTION', 'MONTHLY_COST'])

    # Scrape salary/careers
    career_data = scrape_salaries()
    write_csv('careers.csv', career_data, ['CAREER_NAME', 'INCOME'])

    print("Scraping complete. CSV files are ready.")
