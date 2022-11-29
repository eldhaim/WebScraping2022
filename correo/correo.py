import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import remove


class Generador:
    __asunto_auto = 'REPORTE WebScraping'
    __remitente = 'aromantinjaca@gmail.com'
    __destinatarios = ['angelrt9619@gmail.com']
    __cuerpo = 'REPORTE GENERADO'
    __password = 'uzwolfnaqdxvbyss'

    def envia_correo(self, extension: str = 'csv', asunto: str = __asunto_auto,
                     remitente: str = __remitente, destinatarios: list = None,
                     cuerpo: str = __cuerpo, nombre_archivo: str = 'data',
                     envia_archivo: bool = False):
        # Iniciamos los parámetros del script
        if destinatarios is None:
            destinatarios = self.__destinatarios
        ruta_adjunto = f'{nombre_archivo}.{extension}'

        try:
            # Creamos el objeto mensaje
            mensaje = MIMEMultipart()

            # Establecemos los atributos del mensaje
            mensaje['From'] = remitente
            mensaje['To'] = ", ".join(destinatarios)
            mensaje['Subject'] = asunto

            # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
            mensaje.attach(MIMEText(cuerpo, 'plain'))
            if envia_archivo:
                # Abrimos el archivo que vamos a adjuntar
                archivo_adjunto = open(ruta_adjunto, 'rb')

                # Creamos un objeto MIME base
                adjunto_MIME = MIMEBase('application', 'octet-stream')
                # Y le cargamos el archivo adjunto
                adjunto_MIME.set_payload((archivo_adjunto).read())
                # Codificamos el objeto en BASE64
                encoders.encode_base64(adjunto_MIME)
                # Agregamos una cabecera al objeto
                adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % ruta_adjunto)
                # Y finalmente lo agregamos al mensaje
                mensaje.attach(adjunto_MIME)

            # Creamos la conexión con el servidor
            sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

            # Ciframos la conexión
            sesion_smtp.starttls()

            # Iniciamos sesión en el servidor
            sesion_smtp.login(self.__remitente, self.__password)

            # Convertimos el objeto mensaje a texto
            texto = mensaje.as_string()

            # Enviamos el mensaje
            sesion_smtp.sendmail(remitente, destinatarios, texto)

            # Cerramos la conexión
            sesion_smtp.quit()

            # eliminamos archivo
            remove(f'{ruta_adjunto}')
        except Exception as e:
            print(e)
            # eliminamos archivo
            remove(f'{ruta_adjunto}')
