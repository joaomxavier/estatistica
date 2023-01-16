# **População e amostra**

### População

* Representa um conjunto completo de elementos.

### Amostra

* Se trata de um grupo pequeno dentro da população, ou seja, é um subconjunto da população.
* A amostra precisa ser `randômica` e `representativa`.

### Tipos de amostragem

* Amostragem aleatória simples

* Amostragem sistemática

* Amostragem por grupos (conglomerada)

* Amostragem estratificada

### Subamostragem (undersampling) e sobreamostragem (oversampling)

* São técnicas utilizadas quando temos dados desbalanceados com o objetivo de ajustar a distribuição de classes de um conjunto de dados

!['Undersampling e oversampling']('imagens\undersampling_oversampling.png')

* Undersampling: são selecionadas amostras da classe majoritária para compor uma amostra menor.
    * Algoritmo TOMEK LINKS

!['Tomek']('imagens\tomek.png')

* Oversampling: os registros da classe minoritária são usados para criar registros sintéticas (geração de valores similares).
    * Algoritmo SMOTE

!['Smote']('imagens\smote.png')