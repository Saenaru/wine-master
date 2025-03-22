from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd
from collections import defaultdict


def get_year_suffix(number: int) -> str:
    if 11 <= (number % 100) <= 14:
        return "лет"
    last_digit = number % 10
    if last_digit == 1:
        return "год"
    if 2 <= last_digit <= 4:
        return "года"
    return "лет"


def main():
    excel_path = 'wine3.xlsx'
    df_wine = pd.read_excel(excel_path, engine='openpyxl', keep_default_na=False)
    wine_data = df_wine.where(df_wine.notna(), None)
    product_dict = defaultdict(list)
    for _, row in wine_data.iterrows():
        category = row['Категория']
        wine_entry = row.drop('Категория').to_dict()
        product_dict[category].append(wine_entry)
    foundation_date = datetime(1920, 1, 1)
    current_date = datetime.now()
    age = current_date.year - foundation_date.year
    suffix = get_year_suffix(age)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        age=f"Уже {age} {suffix} с вами",
        product_dict=product_dict
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
