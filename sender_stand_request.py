# Параметры конфигурации: URL сервиса
import configuration

# Библиотека requests для HTTP-запросов
import requests

# Данные запроса: заголовки и тело
import data


# Определение функции для отправки POST-запроса для создания нового заказа
def post_new_order(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


# Вызов функции для создания нового пользователя

order_response = post_new_order(data.order_body)


# Запрос на получение заказа по треку
def get_order(track_order):
    return requests.get(configuration.URL_SERVICE+configuration.PUT_ORDER,
                        params=track_order)