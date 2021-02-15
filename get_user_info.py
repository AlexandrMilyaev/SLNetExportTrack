
import argparse
import logging

import requests


def get_user_info(user_id, slnet_token):
    """
    Получение списка устройств принадлежиших пользователю или устройств, доступ к которым предоставлен пользователю
     другими пользователями. Ответ содержит полное состояние устройств.
    :param user_id: user identifier
    :param slnet_token: StarLineAPI Token
    :return: Код, необходимый для получения токена приложения
    """
    url = "https://developer.starline.ru/json/v2/user/{}/user_info".format(user_id)
    logging.info('execute request: {}'.format(url))
    cookies = "slnet={}".format(slnet_token)

    r = requests.get(url, headers={"Cookie": "slnet=" + slnet_token})
    response = r.json()
    logging.info('cookies: {}'.format(cookies))
    logging.info('response info: {}'.format(response))



def get_args():
    parser = argparse.ArgumentParser()
    #для получения userId можно воспользоваться скриптом get_user_id.py
    parser.add_argument("-u", "--userId", dest="userId", help="user identifier", default="", required=True)
    parser.add_argument("-s", "--slnetToken", dest="slnetToken", help="StarLineAPI Token", default="", required=True)
    args = parser.parse_args()
    logging.info('userId {}, slnetToken: {}'.format(args.userId, args.slnetToken))
    return args


def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    args = get_args()
    get_user_info(args.userId, args.slnetToken)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(e)