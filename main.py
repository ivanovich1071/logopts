import requests
import time
import base64
import config as cfg  # Импортируем конфигурацию из config.py

# URL для асинхронной генерации изображения
url = cfg.url_1  # Загружаем URL из config.py

# Заголовки
headers = {
    "Authorization": f"Bearer {cfg.iam_token}",  # Загружаем IAM-токен из config.py
    "Content-Type": "application/json"
}

# Данные для запроса
data = {
    "modelUri": f"art://{cfg.catalog_id}/yandex-art/latest",  # Загружаем catalog_id из config.py
    "generationOptions": {
        "seed": 1863,
        "aspectRatio": {
            "widthRatio": 2,
            "heightRatio": 1
        }
    },
    "messages": [
        {
            "weight": 1,
            "text": """Автономная система хранения одежды GARDEROBOT: электроприводной конвейер с ячейками для хранения и выдачи спецодежды и личных вещей. Эффективная организация хранения для вахтовиков и крупных объектов: экономия времени, автоматическое управление, точная идентификация, минимизация ошибок, гигиеничность и комфорт. Изображение: HD full wallpaper, четкий фокус, сложные детали, глубина кадра."""
        }
    ]
}

# Отправка POST-запроса
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    request_id = response.json()['id']
    print(f"Request ID: {request_id}")

    # Ожидание обработки изображения
    print("Ожидание обработки изображения...")
    time.sleep(10)  # Пауза для обработки

    # URL для получения результата по ID операции
    result_url = f"{cfg.url_2}/{request_id}"  # Используем URL для операций из config.py

    # Повторный GET-запрос для получения изображения
    result_response = requests.get(result_url, headers=headers)

    if result_response.status_code == 200:
        result_data = result_response.json()

        # Проверка статуса операции
        if result_data.get("done", False):
            print("Обработка завершена.")

            # Получение base64-кодированного изображения
            image_base64 = result_data['response']['image']
            image_data = base64.b64decode(image_base64)

            # Сохранение изображения в файл
            with open("image.jpeg", "wb") as file:
                file.write(image_data)
            print("Изображение успешно сохранено как image.jpeg")
        else:
            print("Обработка ещё не завершена. Повторите запрос позже.")
    else:
        print(f"Ошибка получения результата: {result_response.status_code} - {result_response.text}")
else:
    print(f"Ошибка при отправке запроса: {response.status_code} - {response.text}")
