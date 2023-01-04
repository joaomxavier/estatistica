import pandas as pd
import numpy as np
import random
from sklearn.model_selection import StratifiedShuffleSplit


# Função para amostragem aleatória simples
def amostragem_aleatoria_simples(dataset, amostras, tipo:str):
    """
    Função que retorna o dataframe com os elementos selecionados após a amostragem aleatoria simples
    dataset: dataframe que representa a população
    amostras: nro de elementos da amostra
    tipo: "valor_numerico" ou "percentual"
    """

    if tipo == 'valor_numerico':
        return dataset.sample(n=amostras, random_state=1)
    elif tipo == 'percentual':
        return dataset.sample(frac = amostras, random_state=1) 
    else:
        return "Verifique o valor de tipo (valor_numerico ou percentual)" 


def amostragem_sistematica(dataset, amostras):
    """
    Função que retorna o dataframe com os elementos selecionados após a amostragem sistemática
    dataset: dataframe que representa a população
    amostras: nro de elementos da amostra
    """
    
    # Obtendo o valor do intervalo fixo
    intervalo = len(dataset) // amostras
    # Setando random seed = 1 para retornar sempre a mesma amostra
    random.seed(1)
    # Obtendo o índice do primeiro elemento da amostra
    indice_primeiro = random.randint(0, intervalo)
    # Construção do vetor que contém todos os índices que serão selecionados para fazer parte da amostra
    indices = np.arange(indice_primeiro, len(dataset), step = intervalo)
    # Seleção da amostra com base nos índices obtidos
    amostra_sistematica = dataset.iloc[indices, :]

    return amostra_sistematica


def amostragem_conglomerada(dataset, numero_de_grupos):
    """
    Função que retorna o dataframe com os elementos selecionados após a amostragem por grupos (conglomerada)
    dataset: dataframe que representa a população
    numero_de_grupos: nro de grupos a serem formados
    """
    
    # Obtendo o valor do intervalo (qtde de elementos por grupo)
    intervalo = len(dataset) // numero_de_grupos

    # Contrução do vetor que irá armazenar o grupo de cada elemento
    # Este vetor possuirá valores entre 0 e (numero_de_grupo - 1)
    grupos = []
    id_grupo = 0
    contagem = 0
    
    for _ in dataset.iterrows():
        grupos.append(id_grupo)
        contagem += 1
        if contagem > intervalo:
            contagem = 0
            id_grupo += 1
    
    # Contrução da coluna 'grupo' no dataframe
    dataset['grupo'] = grupos
    random.seed(1)  # setando random seed para retornar a mesma amostra
    grupo_selecionado = random.randint(0, numero_de_grupos)

    # Filtrando somente o grupo selecionado aleatoriamente
    amostra_conglomerada = dataset[dataset['grupo'] == grupo_selecionado]

    return amostra_conglomerada


def amostragem_estratificada(dataset, percentual: float, atributo: str):
    """
    Função que retorna o dataframe com os elementos selecionados após a amostragem estratificada
    dataset: dataframe que representa a população
    percentual: Valor entre 0 e 1 que representa o % de elementos da população (tamanho da amostra)
    atributo: nome da coluna que será utilizada como base para divisão dos grupos
    """
    
    # O parâmetro test_size vai indicar o tamanho da amostra.
    split = StratifiedShuffleSplit(test_size=percentual, random_state=1)

    # Construção do dataframe contendo a amostra estratificada
    for _, y in split.split(dataset, dataset[atributo]):
        amostra_estratificada = dataset.iloc[y]

    return amostra_estratificada