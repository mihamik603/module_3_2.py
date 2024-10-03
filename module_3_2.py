def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email("Привет", "qwerty.@gmail.com")
send_email("Как дела?", "qwerty@mail.com", sender="university@mail.com")
send_email("Выходи гулять", "qwerty@mail.inbox")
send_email("Чё так долго?", "qwerty@mail.com", sender="qwerty@mail.com")
