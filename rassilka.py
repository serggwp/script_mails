import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl

# ЗАМЕНИТЬ НА СВОЕ!!! можно создать файл с именем и паролем
MY_ADDRESS = 'Ваша почта'
PASSWORD = 'Ваш пароль'

# Получает имена контактов и их почту, использовать для персонализации писем
# def get_contacts(filename):
#     names = []
#     emails = []
#     with open(filename, mode='r', encoding='utf-8') as contacts_file:
#         for a_contact in contacts_file:
#             names.append(a_contact.split()[0])
#             emails.append(a_contact.split()[1])
#     return names, emails

# Получает почту из списка contacts
def get_contacts(filename):
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.strip())
    return emails

# Обработка текста письма
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return template_file_content
# если надо персонализировать, то заменить на return Template(template_file_content)   

def main():
    # names, emails = get_contacts('contacts.txt') # чтение файла контактов, если нужны имена контактов
    emails = get_contacts('contacts.txt') # read contacts
    message_template = read_template('message.txt')
    # добавить свой хост и порт, для mail.ru -- smtp.mail.ru, порт такой же (465)
    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    s.login(MY_ADDRESS, PASSWORD)

    # Сама рассылка
    # for name, email in zip(names, emails): поставить это, если персонализировать
    for email in emails:
        msg = MIMEMultipart()       # создание сообщения

        # Этой строкой можно добавить в сообщение имя получателя, если в message.txt вписать ${PERSON_NAME}
        # message = message_template.substitute(PERSON_NAME=name.title())
        # print(message)

        # Параметры сообщения
        msg['From']=MY_ADDRESS
        msg['To']=email
        # Вручную написать тему сообщения
        msg['Subject']="Тестовая тема"
        
        # Добавление текста (из файла message)
        msg.attach(MIMEText(message_template, 'plain')) # Если надо персонализировать, заменить на msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
    s.quit()
    
if __name__ == '__main__':
    main()    