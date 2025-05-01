import requests
from bs4 import BeautifulSoup
import csv

# URLs (replace these with better target links if needed)
HOUSING_URL = 'https://www.rentcafe.com/average-rent-market-trends/us/tn/'
SALARY_URL = 'https://www.bls.gov/careeroutlook/2023/data-on-display/education-pays.htm'

def scrape_housing_prices():
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
    
    # Map the scraped names to your game levels manually if needed
    mapped_salary_data = []
    mappings = {
        "Less than a high school diploma": "No College",
        "High school diploma or equivalent": "Certificate",
        "Bachelor's degree": "Undergraduate",
        "Master's degree": "Graduate",
        "Doctoral degree": "Doctoral"
    }

    for education, salary in salary_data:
        for keyword, mapped in mappings.items():
            if keyword.lower() in education.lower():
                mapped_salary_data.append((mapped, salary))

    return mapped_salary_data

def scrape_transportation_data():
    # Fake some transportation options if needed or scrape from real URLs
    transport_data = [
        ("Hand-me-down", 100),
        ("Used Car", 300),
        ("New Car", 500),
        ("Public Bus", 50)
    ]
    return transport_data

def scrape_tech_data():
    tech_data = [
        ("Cell Phone Bill", 45),
        ("High Speed Internet", 60),
        ("Cable TV", 70),
        ("Streaming Services", 20)
    ]
    return tech_data

def scrape_food_data():
    food_data = [
        ("Cook at Home", 200),
        ("Mix of Home and Takeout", 600),
        ("Eat Out Often", 1000)
    ]
    return food_data

def write_csv(filename, data, headers):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

def main():
    # Scrape housing
    housing_data = scrape_housing_prices()
    write_csv('housing_options.csv', housing_data, ['DESCRIPTION', 'MONTHLY_COST'])

    # Scrape transportation
    transport_data = scrape_transportation_data()
    write_csv('transport_options.csv', transport_data, ['DESCRIPTION', 'MONTHLY_COST'])

    # Scrape technology
    tech_data = scrape_tech_data()
    write_csv('tech_options.csv', tech_data, ['DESCRIPTION', 'MONTHLY_COST'])

    # Scrape food
    food_data = scrape_food_data()
    write_csv('food_options.csv', food_data, ['DESCRIPTION', 'MONTHLY_COST'])

    # Scrape salary/careers
    career_data = scrape_salaries()
    write_csv('careers.csv', career_data, ['NAME', 'INCOME'])

    print("Scraping complete. CSV files are ready.")

if __name__ == "__main__":
    main()
