import requests
import configuration
import data


# Запрос документов через requests
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


response = get_docs()
print(response.status_code)


# Запрос логов через requests
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)


# Запрос данных из таблицы заказов
def post_order_table():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH)


response = post_order_table()
print(response.status_code)


# Запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


response = post_new_order(data.order_body)
print(response.status_code)
# Вывод ответа в формате словаря
print(response.json())


# Запрос на получение заказа по треку заказа
def get_order(order_body, order_track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=order_track)


response = get_order(data.order_body, data.order_track)
print(response.status_code)
print(response.json())
