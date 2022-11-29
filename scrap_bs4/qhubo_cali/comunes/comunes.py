import requests
from lxml import etree

from scrap_bs4.qhubo_cali.excepciones.excepciones_comunes import ComunesException
from bs4 import BeautifulSoup


class Comunes:
    __a_link = './a/@href'
    __todo_doc = './'
    __slash = '/'
    __double_slash = '//'
    __ruta = ''

    @classmethod
    def carga_html(cls, ruta:str):
        request = requests.get(ruta)
        soup = BeautifulSoup(request.text, 'lxml')
        return etree.HTML(str(soup))

    @classmethod
    def h1_class(cls, class_name: str):
        return f'h1[@class="{class_name}"]'

    @classmethod
    def span_class(cls, class_name: str):
        return f'span[@class="{class_name}"]'

    @classmethod
    def div_class(cls, class_name: str):
        return f'div[@class="{class_name}"]'

    @classmethod
    def double_slash(cls):
        return cls.__double_slash

    @classmethod
    def slash(cls):
        return cls.__slash

    @classmethod
    def a_link(cls):
        return cls.__a_link

    @classmethod
    def todo_doc(cls):
        return cls.__todo_doc

    @classmethod
    def ruta_div(cls, class_names: list[str]):
        cls.__ruta = ''
        if len(class_names) == 0:
            raise ComunesException
        else:
            try:
                for class_name in class_names:
                    cls.__ruta = f'{cls.__ruta}{cls.__slash}{cls.div_class(class_name)}'
            except Exception as e:
                raise ComunesException(add=str(e))
        return f'{cls.__todo_doc}{cls.__ruta}'


if __name__ == '__main__':
    bloque_noticias = 'wp-block-lazyblock-categoria lazyblock-categoria-ZDYAMx'
    contenedor_interno = 'cate-block container todas layout-2'
    fila_column = 'row three-col-row'
    columna_interna = 'col-33'
    bloque = 'thumb-block'
    cla = []
    class_names = [bloque_noticias, contenedor_interno, fila_column, columna_interna, bloque]
    print(Comunes.ruta_div(class_names))
