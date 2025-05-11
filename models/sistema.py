class usuario:
    def __init__(self, id, email, senha):
        self.id     = id
        self.email  = email
        self.senha  = senha

class alunos:
    def __init__(self, id, nm_aluno, kg, observacao, user, dt_insert):
        self.id          = id
        self.nm_aluno    = nm_aluno
        self.kg          = kg
        self.observacao  = observacao
        self.user        = user
        self.dt_insert   = dt_insert