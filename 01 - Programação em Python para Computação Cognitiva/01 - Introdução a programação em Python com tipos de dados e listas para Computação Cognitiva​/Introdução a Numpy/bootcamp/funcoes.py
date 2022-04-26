import numpy as np

def menu():
    print("\nO que gostaria de ver? ")
    x = int(input("1 - exemplos de matriz."
                  "\n2 - dimensão da matriz(a.ndim)"
                  "\n3 - tamanho em bytes(a.itemsize)"
                  "\n4 - Tipo de dado(a.dtype)"
                  "\n5 - Tamanho e forma da matriz(a.size e a.shape)"
                  "\n6 - Criar matriz 0 ou 1(np.zeros e np.ones)"
                  "\n7 - array padronizados(np.arange)"
                  "\n8 - Remodelar(np.reshape)"
                  "\n9 - linspace(np.linspace)"
                  "\n10 - max / min(a.min, a.max. a.sum)"
                  "\n11 - Raiz quadrada e desvio padrão(np.sqrt e np.std)"
                  "\n12 - Operação aritmética"
                  "\nResposta: "))
    if (x == 1):
        exemplos_de_matriz()
    elif (x == 2):
        dimensao_matriz()
    elif(x == 3):
        tamanho_em_bytes()
    elif (x == 4):
        tipo_de_dados()
    elif (x == 5):
        analise_tamanho_forma()
    elif (x == 6):
        zero_um()
    elif (x == 7):
        padronizado()
    elif (x == 8):
        remodelar()
    elif (x == 9):
        linspace()
    elif (x == 10):
        max_min()
    elif (x == 11):
        raiz_desvio()
    elif (x == 12):
        print("Deseja ver:"
              "\n 1-Operações aritméticas"
              "\n 2-concatenar"
              "\n 3-Converter matriz em única coluna")
        pergunta = int(input("resposta: "))
        if pergunta == 1:
            operacao_aritmetica()
        elif pergunta == 2:
            concatenar()
        elif pergunta == 3:
            unica_coluna()

def exemplos_de_matriz():
    print("="*50)
    print("\nEssa é uma Matriz unidimensional")
    a = np.array([1,2,3])
    print(a)
    print("podemos obtela com o seguinte codigo: ")
    print("a = np.array([1,2,3])")

    print("\nEssa é uma Matriz bidimensional")
    b = np.array([(1,2,3),(4,5,6),(7,8,9)])
    print(b)
    print("podemos obtela com o seguinte codigo: ")
    print("b = np.array([(1,2,3),(4,5,6),(7,8,9)])")

    print("\nEssa é uma Matriz tridimensional")
    c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(c)
    print("podemos obtela com o seguinte codigo: ")
    print("c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])\n")
    print("=" * 50)

    voltar_menu()

def dimensao_matriz():
    print("\nPodemos encontrar a dimensão de uma matriz com o comando (nome da matriz).ndim"
          "\npor exemplo: "
          " \na matriz: a = np.array([(1,2,3),(4,5,6),(7,8,9)]) retorna: ")
    a = np.array([(1,2,3),(4,5,6),(7,8,9)])
    print(a)
    print("com o comando print(a.ndim) podemos saber quantas dimensões ela tem:")
    print("print(a.ndim) nesse caso retorna '{}' o que significa que é uma matriz bidimensional".format(a.ndim))

    voltar_menu()

def tamanho_em_bytes():
    print("\n.itemsize retorna o tamanho (em bytes) de cada elemento de um array NumPy"
          "\n Por exemplo, para a array a = np.array([(1,2,3)]) que tem retorno:")
    a = np.array([(1,2,3)])
    print(a)
    print("O comando a.itemsize tem retorno como: {}".format((a.itemsize)))

    voltar_menu()

def tipo_de_dados():
    a = np.array([(1, 2, 3)])
    print("\nVocê pode encontrar o tipo de dados dos elementos armazenados em uma matriz."
          "\n Então, se você quiser saber o tipo de dados de um elemento em particular,"
          "\n você pode usar a função 'dtype' que irá imprimir o tipo de dados junto com o tamanho."
          "\n No código a seguir, defini uma matriz em que usei a mesma função. "
          "\n no exemplo: a = np.array([(1,2,3)]) temos: {} utilizando o comando (a.dtype)".format(a.dtype))

    voltar_menu()


def analise_tamanho_forma():
    print(f"\nPodemos análisar o tamanho e forma das funções:"
          "\ncom o comando a.size podemos descobrir a quantidade de itens"
          "\nE com o a.shape podemos ter dois tipos: "
          "\ntipo 1: (n de linhas, n de colunas)"
          "\ntipo 2: (n de matrizes, n de linha de cada uma, n de colunas de cada"
          "\nEX: "
          "\nA matriz a = np.array([(1,22,3,41,5,60)])"
          "\ncom retorno:")
    a = np.array([(1, 22, 3, 41, 5, 60)])
    print(a,
          "\nTem seu a.size = {} (indicando 6 itens)"
          "\nE seu a.shape = {} (indicando 1 linha e 6 colunas)".format(a.size, a.shape))

    print("Outro exemplo:"
          "matriz: b = np.array([(1,2,3),(4,5,6)])")
    b = np.array([(1, 2, 3), (4, 5, 6)])
    print(b,
          "\nTem seu a.size = {} (indicando 6 itens)"
          "\nE seu a.shape = {} (indicando 2 linha e 3 colunas)".format(b.size, b.shape))

    print("Outro exemplo:"
          "matriz: c = np.array([[(1,2,3)],[(3,4,7)]])")
    c = np.array([[(1, 2, 3)], [(3, 4, 7)]])
    print(c,
          "\nTem seu a.size = {} (indicando 6 itens)"
          "\nE seu a.shape = {} (indicando 2 matriz de 1 linha e 3 colunas)".format(c.size, c.shape))

    voltar_menu()

def zero_um():
    a = np.zeros((2, 3, 4))
    b = np.ones((2, 3, 4))
    print("\nPodemos fazer uma matriz/array de zeros ou 1,"
          "\nnp.zeros cria um conjunto de zeros"
          "\n\na = np.zeros((2, 3, 4))"
          "\n{}"
          "\n\nnp.ones cria um conjunto com 1"
          "\n\nb = np.ones((2, 3, 4))"
          "\n{}"
          "\n Assim temos: (n de matriz, n de linha, n de coluna)".format(a,b))
    voltar_menu()

def padronizado():
    x = np.arange(0, 10, 1)
    y = x ** 2
    print("\nPodemos criar padrões nas arrays com o comando: "
          "\nnp.arange(valor inicial, valor final(n incluso), contador)"
          "\nEX:"
          "\n\nx = np.arange(0, 10, 1)"
          "\n{}"
          "\n\nPodemos ver que começa no 0, vai até o 10 somando +1"
          "\n\nOutro EX:"
          "\nY = x ** 2"
          "\n\nIsso retorna: "
          "\n{}".format(x,y))
    voltar_menu()

def remodelar():
    a = np.array([(8, 9, 10), (11, 12, 13)])
    b = a.reshape(3, 2)
    print("\nPodemos trocar linhas por colunas"
          "\nex: "
          "\na = np.array([(8,9,10),(11,12,13)]) "
          "\n\n{}"
          "\n\na=a.reshape(3,2)"
          "\n\n{}".format(a,b))
    voltar_menu()

def linspace():
    a = np.linspace(1, 3, 10)
    print("\nEsta é outra operação em python numpy que retorna"
          "\nnúmeros uniformemente espaçados em um intervalo especificado."
          "\nConsidere o exemplo abaixo:  "
          "\na = np.linspace(1,3,10)"
          "\n{}".format(a))
    voltar_menu()

def max_min():
    a = np.array([1, 2, 3,55])
    print("\nUsando os comandos:"
          "\na.min(), retornamos o menor valor da array"
          "\na.max(), retornamos o maior valor da array"
          "\na.sum(), retornamos a soma dos valores da array"
          "\nno ex: {}"
          "\na.min({})"
          "\na.max({})"
          "\na.sum({})".format(a,a.min(),a.max(),a.sum() ))
    voltar_menu()

def raiz_desvio():
    a = np.array([(1, 2, 3), (3, 4, 5,)])
    print("Podemos descobrir a raiz quadrada e \n"
          "o desvio padrão de uma matriz"
          "\nnp.sqrt(a) para a raiz quadrada"
          "\nnp.std(a) para o desvio padrão"
          "\nNo ex: a = np.array([(1,2,3),(3,4,5,)]) "
          "\n{}"
          "\nRaiz quadrada:"
          "\n{}"
          "\nDesvio padrão:"
          "\n{}".format(a,np.sqrt(a),np.std(a)))
    voltar_menu()

def operacao_aritmetica():
    x = np.array([(1, 2, 3), (3, 4, 5)])
    y = np.array([(1, 2, 3), (3, 4, 5)])
    print("\nVocê pode realizar mais operações na matriz numpy,"
          "\n ou seja, adição, subtração, multiplicação e divisão"
          "\n das duas matrizes."
          "\ntemos as seguintes operações:"
          "\n\nx = np.array([(1, 2, 3), (3, 4, 5)])"
          "\ny = np.array([(1, 2, 3), (3, 4, 5)])"

          "\n\n(x + y) =\n\n {} \n+\n {} \n=\n {}".format(x, y, (x + y)))
    print("-" * 20)

    print("\n(x - y) =\n\n {} \n-\n {} \n=\n {}".format(x, y, (x - y)))
    print("-" * 20)

    print("\n(x * y) =\n\n {} \n*\n {} \n=\n {}".format(x, y, (x * y)))
    print("-" * 20)

    print("\n(x / y) =\n\n {} \n/\n {} \n=\n {}".format(x, y, (x / y)))
    print("-" * 20)

    voltar_menu()

def concatenar():
    x = np.array([(1, 2, 3), (3, 4, 5)])
    y = np.array([(1, 2, 3), (3, 4, 5)])
    print("\nse você deseja concatenar dois arrays e não apenas adicioná-los,"
          "\nvocê pode executar de duas maneiras -"
          "\nempilhamento vertical e empilhamento horizontal .")
    print("\nx = np.array([(1, 2, 3), (3, 4, 5)])\n",x,
          "\ny = np.array([(1, 2, 3), (3, 4, 5)])\n",y,
          "\n\nEmpilhando verticalmente: print(np.vstack((x, y)))"
          "\n{}"
          "\n\nEmpilhando Horizontalmente: print(np.hstack((x, y)))"
          "\n{}".format(np.vstack((x, y)),np.hstack((x, y))))
    voltar_menu()

def unica_coluna():
    x = np.array([(1, 2, 3), (3, 4, 5)])
    print("Esse comando converte uma matriz em uma única coluna: " \
    "\n x = np.array([(1, 2, 3), (3, 4, 5)])" \
    "\n print(x.ravel())\n")
    print(x)
    print("\nIra virar:\n")
    print(x.ravel())

    voltar_menu()


def voltar_menu():
    sair = input(("\nRetornar ao menu? (s)"))
    if sair == "s":
        menu()


