# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Подготовка данных

- Скачайте код
- Создайте виртуальное окружение venv для изоляции зависимостей.

```bash
python -m venv .venv
```

Активация виртуального окружения:
- На Windows:
```bash
.venv\Scripts\activate
```
- На MacOS и Linux:
```bash
source .venv/bin/activate
```

Выполните команду:
```bash
pip install -r requirements.txt
```



Для корректной работы приложения необходимо создать Excel-файл (`wine.xlsx`) со следующими требованиями к структуре:

1. **Формат файла**: Excel (.xlsx)
2. **Столбцы в таблице**:
   - **Категория**: Категория продукта, например, "Белые вина" или "Красные вина".
   - **Название**: Название вина.
   - **Сорт**: Сорт винограда или основной ингредиент. Может быть пустым.
   - **Цена**: Цена в рублях.
   - **Картинка**: Имя файла изображения продукта. Изображения должны находиться в каталоге `images/`.
   - **Акция**: Описание акции, например, "Выгодное предложение". Может быть пустым.

### Пример таблицы

Ниже приведен пример того, как могут быть организованы данные в `wine.xlsx`. Используйте эту таблицу как шаблон:

| Категория    | Название           | Сорт          | Цена | Картинка                | Акция                 |
|--------------|--------------------|---------------|------|-------------------------|-----------------------|
| Белые вина   | Белая леди         | Дамский пальчик | 399  | belaya_ledi.png        | Выгодное предложение  |
| Напитки      | Коньяк классический|               | 350  | konyak_klassicheskyi.png |                       |
| Белые вина   | Ркацители          | Ркацители     | 499  | rkaciteli.png           |                       |
| Красные вина | Черный лекарь      | Качич         | 399  | chernyi_lekar.png       |                       |
| Красные вина | Хванчкара          | Александраули | 550  | hvanchkara.png          |                       |
| Белые вина   | Кокур              | Кокур         | 450  | kokur.png               |                       |
| Красные вина | Киндзмараули       | Саперави      | 550  | kindzmarauli.png        |                       |
| Напитки      | Чача               |               | 299  | chacha.png              | Выгодное предложение  |
| Напитки      | Коньяк кизиловый   |               | 350  | konyak_kizilovyi.png    |                       |

### Образец для данных

Файл `wine.xlsx`, используемый в проекте, может служить образцом. Скачайте его и заполните своими данными, чтобы обеспечить корректную работу приложения.

## Запуск
В `excel_path.env` прописан путь `wine.xlsx`. Для указания другого файла, укажите свой путь:
```
data-path=wine.xlsx
```

- Запустите сайт командой
```
python3 main.py
```
Или пропишите свой путь файла:
```
python main.py --data-path=./another_wine_data.xlsx
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
