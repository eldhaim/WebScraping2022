from scrap_bs4.qhubo_cali.comunes.comunes import Comunes
from scrap_bs4.qhubo_cali.excepciones.excepciones import DomException


class Seccion:
    def __init__(self, link: str):
        self.__dict_link = 'Link'
        self.__dict_titulo = 'Titulo'
        self.__dict_fecha = 'Fecha'
        self.__dict_subtitulo = 'Subtitulo'
        self.__dict_descripcion = 'Descripcion'
        self.__desc_subtitulo = 'entry-content'
        self.__dom = Comunes.carga_html(link)
        self.__noticia = {self.__dict_link: link}
        self.generar_datos()


    def genera_titulo(self):
        titulo = 'entry-title'
        ruta = f'{Comunes.todo_doc()}{Comunes.slash()}{Comunes.h1_class(titulo)}'
        try:
            self.__noticia[self.__dict_titulo] = self.__dom.xpath(ruta)[0].text
        except Exception as e:
            raise DomException(add=str(e))

    def genera_fecha(self):
        fecha_div = 'entry-meta'
        fecha_span = 'posted-on'
        etiqueta_a = '/a/time'
        ruta = f'{Comunes.todo_doc()}' \
               f'{Comunes.slash()}{Comunes.div_class(fecha_div)}' \
               f'{Comunes.slash()}{Comunes.span_class(fecha_span)}{etiqueta_a}'
        try:
            self.__noticia[self.__dict_fecha] = self.__dom.xpath(ruta)[0].text
        except Exception as e:
            raise DomException(add=str(e))

    def genera_subtitulo(self):
        h2 = '/h2'
        ruta = f'{Comunes.todo_doc()}{Comunes.slash()}{Comunes.div_class(self.__desc_subtitulo)}{h2}'
        try:
            self.__noticia[self.__dict_subtitulo] = self.__dom.xpath(ruta)[0].text
        except Exception as e:
            raise DomException(add=str(e))

    def genera_descripcion(self):
        p = '/p'
        ruta = f'{Comunes.todo_doc()}{Comunes.slash()}{Comunes.div_class(self.__desc_subtitulo)}{p}'
        try:
            self.__noticia[self.__dict_descripcion] = self.__dom.xpath(ruta)[0].text
        except Exception as e:
            raise DomException(add=str(e))

    def generar_datos(self):
        self.genera_titulo()
        self.genera_fecha()
        self.genera_subtitulo()
        self.genera_descripcion()
        print(self.__noticia)

    @property
    def noticia(self):
        return self.__noticia


if __name__ == '__main__':
    seccion = Seccion(
        'https://www.qhubocali.com/deportes/mundial-qatar-2022/el-9-de-la-seleccion-de-corea-del-sur-se-roba-mas-de'
        '-una-mirada-en-qatar-2022/')
