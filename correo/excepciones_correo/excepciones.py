class CorreoException(Exception):
    __msj = "Imposible enviar el correo electronico"

    def __init__(self, message: str = __msj, add:str = ''):
        self.final_msg = f'{message}\n{add}'
        super(CorreoException, self, ).__init__(self.final_msg)