import requests

TOKEN = 'y0_AgAAAAARcpy_AADLWwAAAAEXdM8IAACZZAaGflRJjZuRnN9f19t35axlmQ'

class YADiskClient:
    """
    Класс YADiskClient
    Поля класса:
    token - токен API Yandex disc
    """
    def __init__(self, token):
        self.token = token

    def make_dir(self, folder_name) -> None:
        """
        Метод класса создает на яндекс диске папку для хранения фото
        """
        DIR_URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {
            'Authorization': self.token
        }

        self.params = {
            'path': f'/{folder_name}'
        }

        response = requests.put(DIR_URL, params=self.params, headers=self.headers)


if __name__ == '__main__':
    client = YADiskClient(TOKEN)
    client.make_dir('Some')