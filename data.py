headers = {
    "Content-Type": "application/json"
}

order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}


order_track = {"track": "{'701518'}"}


response_body = {
    "order": {
        "id": 2,
        "firstName": "Gaara",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06T00:00:00.000Z",
        "track": 805415,
        "color": [
            "BLACK"
        ],
        "comment": "Saske, come back to Konoha",
        "cancelled": "False",
        "finished": "False",
        "inDelivery": "False",
        "createdAt": "2023-11-12T21:11:07.932Z",
        "updatedAt": "2023-11-12T21:11:07.932Z",
        "status": 0
    }
}
