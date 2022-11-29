class ComunesException(Exception):
    __msj = "Imposible generar la cadena de texto"

    def __init__(self, message: str = __msj, add:str = ''):
        self.final_msg = f'{message}\n{add}'
        super(ComunesException, self, ).__init__(self.final_msg)
