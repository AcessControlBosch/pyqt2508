import requests
from datetime import datetime
from socket import gethostname
import socket
def getData():
    # print('hostname:', socket.gethostbyname(socket.gethostname()))

    # print(socket.SocketType)
    #
    # url = requests.get('http://localhost:8000/users/')
    # print(url)
    # json_response = dict(url)
    # print(type(json_response))
    # print(json_response['name'])
    #
    # urll = 'http://localhost:8000/users/'
    # urll2 = 'http://localhost:8000/users/11/'
    #
    # body = [{
    #         "name": "Testee teste",
    #         "EDV": "5478134",
    #         "id_card": "554546"
    # }]
    #
    #
    # url2 = requests.post(urll, json = body )
    #
    # print(url2.status_code)
    #
    # put = {
    #     "name": "Teste",
    #     "EDV": "8748545"
    # }
    # #
    # url3 = requests.put(urll2, json = put)
    # print(url3.status_code)
    #
    # print(datetime.today().strftime('%Y-%m-%d'))
    # data = datetime.today().strftime('%Y-%m-%d')
    # hora = datetime.today().strftime('%H:%M:%S')
    # print(datetime.today().strftime('%H:%M:%S'))

    # url = 'http://localhost:8000/releasemachines/'
    #
    # body = [{
    #     "date": data,
    #     "hour": hora,
    #     "idMachineFK": "1",
    #     "idAssociateFK": "11"
    # }]
    #
    # url2 = requests.post(url, json = body )

    # urlMachine = 'http://lo' \
    #              'calhost:8000/machines/2/'
    # false = False
    # put = {
    #     "name": "teste",
    #     "description": "tesete",
    #     "status": false,
    #     "ipaddress": "12"
    # }
    #
    # urlPut = requests.put(urlMachine, json=put)
    #
    # print(urlPut.status_code)
    # urlMachine = 'http://localhost:8000/machines/1/'
    #
    # put = {
    #     "name": "teste",
    #     "description": "tesete",
    #     "status": True,
    #     "ipaddress": "12",
    #     "statusmaint": True
    # }
    #
    # urlPut = requests.put(urlMachine, json=put)
    #
    # print(urlPut.status_code)
    #
    # data = datetime.today().strftime('%Y-%m-%d')
    # hora = datetime.today().strftime('%H:%M:%S:%f')
    #
    #
    # print(data,hora)
    # url = 'http://localhost:8000/releasemachines/'
    #
    # body = [{
    #     "date": data,
    #     "hour": hora,
    #     "hourFinish": None,
    #     "idMachineFK": "1",
    #     "idAssociateFK": 4
    # }]
    #
    # urlpost = requests.post(url, json=body)
    # print(urlpost.status_code)

    urlMachine = 'http://192.168.88.108:8000/machines/1/'

    patch2 = {
        "status": False,
    }

    urlPut = requests.patch(urlMachine, patch2)

    print('patch Desl', urlPut)


getData()