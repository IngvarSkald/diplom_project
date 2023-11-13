# Игорь Беспалов, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import main
import data
import configuration
import requests

# Получение и сохранение трека заказа
def get_new_order_track():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)


response_track = get_new_order_track()
data.order_track["track"] = response_track.json()["track"]


# Тест на проверку получение заказа по треку
def test_get_order_track_get_success_response():
    # В переменную order_body сохраняется обновленное тело запроса с треком "805415"
    order_body = get_order_body("805415")
    # В переменную order_response сохраняется результат запроса на получение заказа
    user_response = main.get_order(order_body)


    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 201
    # Проверяется, что в ответе есть поле order_track, и оно не пустое
    assert order_response.json()["track"] != ""
