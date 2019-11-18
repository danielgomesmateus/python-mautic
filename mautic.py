import requests
import json


def create_contact_mautic(email, firstname, lastname):
    headers = ""
    params = {"email": email}
    params.update({"firstname": firstname})
    params.update({"lastname": lastname})
    url = 'http://localhost/mautic/api/contacts/new'
    response = requests.request('POST', url, data=json.dumps(params), headers=headers, auth=('admin', '123456'))
    return response.text


start = create_contact_mautic('contato@giftbiscuit.com.br', "Carla", "Figueredo Gomes Mateus")
print(start)