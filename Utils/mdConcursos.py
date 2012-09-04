'''
Created on 30/09/2011

@author: Evaldo
'''

import os

class MatrizConcursos(object):
    '''
     Gera uma _matriz com os sorteios
    '''     
    def count(self):
        return self._cont
    
    def getMatriz(self):
        return self._matriz
    
    def updateMatriz(self):
        if os.path.exists(self._fileName):
            f = open(self._fileName)
            #zerar a _matriz       
            self._matriz = [] 
            self._cont = 0 
                   
            try:
                for linha in f:
                    if len(linha) > 0:                   
                        self._matriz.append(linha.split('|')[0:-1])
                        self._cont = self._cont +1                     
            finally:
                f.close()
        else:
            print 'Arquivo nao encontrado',self._fileName
            
    def __init__(self,fileName):
        self._matriz = []
        self._fileName = fileName
        self._cont =0
       
        