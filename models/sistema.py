class usuario:
    def __init__(self, id, email, senha):
        self.id     = id
        self.email  = email
        self.senha  = senha

class alunos:
    def __init__(self, id, nm_aluno, telefone, observacao, user, dt_insert):
        self.id          = id
        self.nm_aluno    = nm_aluno
        self.telefone    = telefone
        self.observacao  = observacao
        self.user        = user
        self.dt_insert   = dt_insert

class agendamentos:
    def __init__(self, id, nm_aluno, dia_semana_aula, horario_inicio, horario_fim, observacao, user, dt_insert):
        self.id                 = id
        self.nm_aluno           = nm_aluno
        self.dia_semana_aula    = dia_semana_aula
        self.horario_inicio     = horario_inicio
        self.horario_fim        = horario_fim
        self.observacao         = observacao
        self.user               = user
        self.dt_insert          = dt_insert

class treinos:
    def __init__(self, id, nm_treino, nm_grupo_membro, observacao, user, dt_insert):
        self.id                 = id
        self.nm_treino          = nm_treino
        self.nm_grupo_membro    = nm_grupo_membro
        self.observacao         = observacao
        self.user               = user
        self.dt_insert          = dt_insert