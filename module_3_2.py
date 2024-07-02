
def end_check(end_word,word):
    f = False

    if end_word == word[(len(word)-len(end_word)):(len(word))]:
        f = True
    return (f)

def is_right(ots):
    f1 = 0
    if ('@' in ots or end_check('.com',ots) == True  or end_check('.ru',ots) == True
        or end_check('.net',ots) == True) :
        f1 = 1
    return (f1)

def send_email(message,recipient,sender='university.help@gmail.com'):
    print("Sent_email('",message,"','",recipient,"','",sender,"'")
    if ( is_right(sender) == 0 or is_right(recipient) == 0 ):
        print('Не возможно отправить письмо с адреса',sender,'на адрес',recipient)
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com' :
        print('Письмо успешно отправлено с адреса', sender,'на адрес',recipient,'.')
        return
    if sender != 'university.help@gmail.com' :
        print('Нестандартный отправитель! Письмо отправлено с адреса',sender,'на адрес',recipient,'.')

send_email('Зачет','student@mail.ru')
send_email('Привествую','university.help@gmail.com')
send_email('Добрый день','student.cj')
send_email('Добро пожаловать на вебинар','ivanov@mail.ru','university.urban@gmail.com')
send_email('Добро пожаловать на вебинар','ivanov@mail.ru','university.urban$gmail')

