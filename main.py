# Получение трекеров заказов из бд
track = database.get_track()


# Итерация по каждому трекеру
for track in track:
    # проверка поля finished
    if track.finished:
        status = 2
    else:
        # проверка поля cancelled
        if track.cancelled:
            status = -1
        else:
            # проверка поля inDelivery
            if track.inDelivery:
                status = 1
            else:
                status = 0
    # Вывод трекера заказа и его статуса
    print('Трекер заказа:', track.track_id)
    print('Статус заказа:', status)
