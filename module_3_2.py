def send_email(message, recipient, *, sender='urban.teacher@mail.ru'):  # 1 "message" и "recipient" - позиционные
    # аргументы указываем при вызове функций. sender -  именнованный аргумент, который по умолчанию имеет зачение
    # "university.help@gmail.com". Символ * перед sender делает его обязательным именованным аргументом,
    # который можно указать только по имени.
    # 2. Проверка корректности e-mail адресов/ проверить, содержат ли строки recipient и sender
    if '@' not in recipient or not (
            recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return


    if '@' not in sender or not (sender.endswith('.com' or recipient.endswith('.ru') or sender.endswith('.net'))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    # 3. Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самоу себе!")
        return


    # 4. Проверка на отправителя по умолчанию
    if sender == 'university.help@gmail.com':
        print(f'"Письмо успешно отправлено с адреса {sender} на адрес {recipient}"')
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')