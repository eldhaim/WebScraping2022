from scrap_bs4.qhubo_cali.comunes.comunes import Comunes
from scrap_bs4.qhubo_cali.excepciones.excepciones import DomException
from scrap_bs4.qhubo_cali.seccion import Seccion


class QHubo:
    __dict_ultimas = 'UltimasNoticias'
    __dict_especiales = 'Especiales'
    __fila_column = 'row three-col-row'
    __columna_interna = 'col-33'
    __bloque = 'thumb-block'
    __url = 'https://www.qhubocali.com/'

    def __init__(self):
        self.__ultimas_noticias = []
        self.__noticias_especiales = []
        self.__noticias_recolectadas = {}
        self.__errores_noticias = {}
        self.__errores_especiales = {}
        self.__errores = {}
        self.__dom = Comunes.carga_html(self.__url)
        self.cargar_datos()

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

    def cargar_noticias_especiales(self):  # DE LA MISMA FORMA QUE cargar_ultimas_noticias DEBE OBTENERSE LAS ESPECIALES
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

    def cargar_datos(self):
        ultimas = []
        especiales = []
        self.cargar_ultimas_noticias()
        self.cargar_noticias_especiales()
        for link in self.__ultimas_noticias:
            try:
                seccion = Seccion(link)
                ultimas.append(seccion.noticia)
            except Exception as e:
                print(e)
                self.__errores_noticias[link] = str(e)
        for link in self.__noticias_especiales:
            try:
                seccion_especial = Seccion(link)
                especiales.append(seccion_especial.noticia)
            except Exception as e:
                print(e)
                self.__errores_especiales[link] = str(e)
        self.__errores[self.__dict_ultimas] = self.__errores_noticias
        self.__errores[self.__dict_especiales] = self.__errores_especiales
        self.__noticias_recolectadas[self.__dict_ultimas] = ultimas
        self.__noticias_recolectadas[self.__dict_especiales] = especiales
        print(self.__noticias_recolectadas)
        print(self.__errores)

    @property
    def ultimas_noticias(self):
        return self.__ultimas_noticias

    @property
    def noticias_especiales(self):
        return self.__noticias_especiales

    @property
    def errores(self):
        return self.__errores


if __name__ == '__main__':
    qhubo = QHubo()
