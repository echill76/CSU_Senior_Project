import os

# Directory for outputs
output_dir = "/mnt/data/sql_output"
os.makedirs(output_dir, exist_ok=True)

# Static fallback data
careers_data = [
    ("No College", 2500.00, 250.00, 0.00, 225.00),
    ("Certificate", 3333.33, 333.33, 0.00, 300.00),
    ("Undergraduate", 5416.67, 541.67, 310.00, 487.50),
    ("Graduate", 6666.67, 666.67, 440.00, 600.00),
    ("Doctoral", 8333.33, 833.33, 1280.00, 750.00)
]

housing_data = [
    ("Apartment", 800),
    ("Townhouse", 1200),
    ("Single Family Home", 1600)
]

transport_data = [
    ("Hand-me-down", 100),
    ("Used", 300),
    ("New", 500),
    ("Bus", 50)
]

tech_data = [
    ("Cell Phone Bill", 45),
    ("High Speed Internet", 60),
    ("Cable TV", 70),
    ("Streaming Services", 20)
]

food_data = [
    ("Cook at Home", 200),
    ("Mix of Home and Takeout", 600),
    ("Eat Out Often", 1000)
]

def write_sql_file(filename, table, columns, data):
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w") as f:
        for row in data:
            values = []
            for value in row:
                if isinstance(value, str):
                    values.append(f"'{value}'")
                else:
                    values.append(str(value))
            values_string = ", ".join(values)
            insert_stmt = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({values_string});\n"
            f.write(insert_stmt)
    return filepath

def generate_all_sql():
    paths = []
    paths.append(write_sql_file('careers.sql', 'CAREERS', ['NAME', 'INCOME', 'TAXES', 'LOAN', 'TITHING'], careers_data))
    paths.append(write_sql_file('housing_options.sql', 'HOUSING_OPTIONS', ['DESCRIPTION', 'MONTHLY_COST'], housing_data))
    paths.append(write_sql_file('transport_options.sql', 'TRANSPORT_OPTIONS', ['DESCRIPTION', 'MONTHLY_COST'], transport_data))
    paths.append(write_sql_file('tech_options.sql', 'TECH_OPTIONS', ['DESCRIPTION', 'MONTHLY_COST'], tech_data))
    paths.append(write_sql_file('food_options.sql', 'FOOD_OPTIONS', ['DESCRIPTION', 'MONTHLY_COST'], food_data))
    return paths

# Run generator
sql_files = generate_all_sql()
print("SQL files generated:", sql_files)