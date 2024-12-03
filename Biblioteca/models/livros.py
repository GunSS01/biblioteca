class Livros():
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro
        self.__name__="Livros"
        self.status = "Disponivel"
        self.usuario = None

    def create(self):
        return f'insert into Livros(titulo, autor, genero, status, codigo) values("{self.titulo}", "{self.autor}", "{self.genero}", "{self.status}", {self.cod_livro});'

    def read(self):
        return f'select * from Livros where codigo = {self.cod_livro};'
    
    def update(self): 
        return f'update status = {self.status}'

@staticmethod
def delete(cod_livro):
    return f'delete from Livros where codigo={cod_livro}' 

Livros.__name__="Livros"





    
