class DomException(Exception):
    __msj = "Imposible tratar los elementos indicados"

    def __init__(self, message: str = __msj, add:str = ''):
        self.final_msg = f'{message}\n{add}'
        super(DomException, self, ).__init__(self.final_msg)