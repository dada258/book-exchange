
import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
class HTTP:
    @classmethod
    def get(cls,url,return_json=True):
        r = requests.get(url,headers=headers)
        if r.status_code != 200:
            return {} if return_json else ''
        rj = r.json()

        rj['image'] = cls.get_image(rj['image'])


        return rj if return_json else r.text
    @staticmethod
    def get_image(image):
        id_start = image.find('public/') + 7
        id_end = image.find('.jpg')
        image = image[id_start:id_end]
        url = 'https://img1.doubanio.com/lpic/{}.jpg'.format(image)
        return url
