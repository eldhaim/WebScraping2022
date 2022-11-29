import pandas as pd


class Archivos:

    def generar_archivo(self, extension: str, nombre_archivo: str, lista_siniestros: list, lista_columnas: list):
        lista_columnas = lista_columnas
        csv = pd.DataFrame(lista_siniestros, columns=lista_columnas)
        if extension == 'csv':
            csv.to_csv(f'{nombre_archivo}.{extension}', index=False, sep=';')
        elif extension == 'xlsx':
            csv.to_excel(f'{nombre_archivo}.{extension}', index=False)
