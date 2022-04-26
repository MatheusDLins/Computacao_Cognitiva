import numpy as np

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

raiz_desvio()