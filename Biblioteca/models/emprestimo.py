class Emprestimo():
    def __init__(self, cpf, cod_livro, dt_emprestimo, dt_devolucao, status):
        self.cpf = cpf
        self.cod_livro = cod_livro
        self.dt_emprestimo = dt_emprestimo
        self.dt_devolucao = dt_devolucao
        self.status = status 

    def create(self):
        return f'insert into Emprestimo (cpf, cod_livro, dt_emprestimo, dt_devolucao, status)'
    
    def read (self): 
        return f'select * from Emprestimo where'
    
    def update (self): 
        return f'update status = {self.status}'
