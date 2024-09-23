import pytest
from projeto.models.pessoa import Pessoa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Pedro", 19)
    return pessoa

def test_pessoa_alterar_nome_valido(pessoa_valida):
    #Alterando o nome da pessoa 'Pedro' para 'Helena'
    pessoa_valida.nome = "Helena"
    assert pessoa_valida.nome == "Helena"

def test_pessoa_valido(pessoa_valida):
    assert pessoa_valida.nome == "Pedro"

def test_pessoa_idade_valido(pessoa_valida):
    assert pessoa_valida.idade == 19

def test_pessoa_idade_negativa_retorna_mensagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match="Idade não pode ser negativa."):
        Pessoa("Pedro", -1)
    
