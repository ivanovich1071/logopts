import os
from dotenv import load_dotenv

# Загрузка переменных из .env
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Загруженные данные
iam_token = os.getenv("YANDEX_IAM_TOKEN")
catalog_id = os.getenv("YANDEX_CATALOG_ID")
url_1 = os.getenv("YANDEX_URL_1")
url_2 = os.getenv("YANDEX_URL_2")

# Проверка значений
if not all([iam_token, catalog_id, url_1, url_2]):
    raise ValueError("Некоторые значения из .env не были загружены. Проверьте содержание файла .env.")
