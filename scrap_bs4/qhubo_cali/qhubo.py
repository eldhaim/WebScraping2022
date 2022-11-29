from scrap_bs4.qhubo_cali.comunes.comunes import Comunes
from scrap_bs4.qhubo_cali.excepciones.excepciones import DomException


class Inicio:
    def __init__(self):
        self.__dom = Comunes.carga_html('https://www.qhubocali.com/')
        self.__fila_column = 'row three-col-row'
        self.__columna_interna = 'col-33'
        self.__bloque = 'thumb-block'
        self.__ultimas_noticias = []
        self.__noticias_especiales = []

    def cargar_ultimas_noticias(self):
        bloque_noticias = 'wp-block-lazyblock-categoria lazyblock-categoria-ZDYAMx'
        contenedor_interno = 'cate-block container todas layout-2'
        lista_noticias = [bloque_noticias, contenedor_interno, self.__fila_column, self.__columna_interna]
        ruta = f'{Comunes.ruta_div(lista_noticias)}{Comunes.double_slash()}{Comunes.div_class(self.__bloque)}'
        noticias = self.__dom.xpath(ruta)
        if len(noticias) == 0:
            raise DomException('No se encuentran coincidencias para la ruta:', ruta)
        else:
            try:
                for link in noticias:
                    self.__ultimas_noticias.append(link.xpath(Comunes.a_link())[0])
            except Exception as e:
                raise DomException(add=str(e))

    def especiales(self):  # DE LA MISMA FORMA QUE cargar_ultimas_noticias DEBE OBTENERSE LAS ESPECIALES
        bloque_noticias = 'wp-block-lazyblock-categoria lazyblock-categoria-dplBO'
        contenedor_interno = 'cate-block container especiales layout-2'
        lista_especiales = [bloque_noticias, contenedor_interno, self.__fila_column, self.__columna_interna]
        ruta = f'{Comunes.ruta_div(lista_especiales)}{Comunes.double_slash()}{Comunes.div_class(self.__bloque)}'
        especiales = self.__dom.xpath(ruta)
        if len(especiales) == 0:
            raise DomException('No se encuentran coincidencias para la ruta:', ruta)
        else:
            try:
                for link in especiales:
                    self.__noticias_especiales.append(link.xpath(Comunes.a_link())[0])
            except Exception as e:
                raise DomException(add=str(e))

    @property
    def ultimas_noticias(self):
        return self.__ultimas_noticias

    @property
    def noticias_especiales(self):
        return self.__noticias_especiales


if __name__ == '__main__':
    inicio = Inicio()
    inicio.cargar_ultimas_noticias()
    print(inicio.ultimas_noticias)
    inicio.especiales()
    print(inicio.noticias_especiales)
