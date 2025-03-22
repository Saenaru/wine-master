import json
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd
from collections import defaultdict
import configargparse


def get_year_suffix(number: int) -> str:
    if 11 <= (number % 100) <= 14:
        return "лет"
    last_digit = number % 10
    if last_digit == 1:
        return "год"
    if 2 <= last_digit <= 4:
        return "года"
    return "лет"


def load_config(config_file='config.json'):
    with open(config_file, 'r', encoding='utf-8') as file:
        return json.load(file)


def main():
    config = load_config()
    parser = configargparse.ArgParser(default_config_files=['excel_path.env'])
    parser.add('--data-path', type=str, help='Путь к файлу с данными о вине (.xlsx)', env_var='EXCEL_PATH')
    options = parser.parse_args()
    excel_path = options.data_path
    if not excel_path or not pd.io.common.file_exists(excel_path):
        raise FileNotFoundError(f"Файл с данными {excel_path} не найден.")
    data_frame = pd.read_excel(excel_path, engine='openpyxl', keep_default_na=False)
    wine_data = data_frame.where(data_frame.notna(), None)
    products = defaultdict(list)
    for _, row in wine_data.iterrows():
        category = row['Категория']
        wine_entry = row.drop('Категория').to_dict()
        products[category].append(wine_entry)
    foundation_year = 1920
    current_year = datetime.now().year
    age = current_year - foundation_year
    suffix = get_year_suffix(age)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        age=f"Уже {age} {suffix} с вами",
        products=products,
        special_offer_label=config['special_offer_label']
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
