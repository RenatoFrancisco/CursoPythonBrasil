class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido!')

    def cep_eh_valido(self, cep):
        return len(cep) == 8

    def format_cep(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])