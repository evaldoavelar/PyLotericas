'''
Created on 22/09/2011

@author: Evaldo
'''
import random

class ConcursoCalculos(object):
    '''
     Gera uma _matriz com os sorteios
    '''    
       
    def getTotaisSorteios(self,MatrizConcursos,Loterias, ultimosSorteios=0):
        ''' Retorna uma _matriz com os totais das dezenas em todos os sorteios '''
        matrizTotais = {}
        if ultimosSorteios > 0:
            ultimosSorteios =len(MatrizConcursos)- ultimosSorteios
        
        '''inicializar a _matriz'''
        for i in  Loterias.getNumeroDezenasIter():
            matrizTotais[i] = 0
        '''pecorrer as linhas'''      
        for linha in MatrizConcursos:
            '''elementos na linha'''
            for idx in linha[1:]:
                if int(linha[0]) >= ultimosSorteios:
                    '''transformar elementos em inidice'''
                    idx = int(idx)
                    '''contabilizar elemento'''
                    matrizTotais[idx] += 1
                else:
                    break                
        
        return matrizTotais
    
    
    '''def enumerate(sequence, start=0):
        n = start
        for elem in sequence:
            yield n, elem
            n += 1
    '''
    def getTotaisPorDezena(self,MatrizConcursos,Loterias, ultimosSorteios=0):
                
        ''' Retorna uma _matriz com os totais das dezenas no sorteios '''
        matrizTotais = {}
        
        if ultimosSorteios > 0:
            ultimosSorteios = len(MatrizConcursos) - ultimosSorteios
        
        '''inicializar a _matriz'''        
        for i in  Loterias.getNumeroBolasIter():
            for j in Loterias.getNumeroDezenasIter():
                matrizTotais[(i, j)] = 0
        
        for linha in MatrizConcursos:
            '''Zera a coluna'''
            
            for i,item in enumerate(linha[1:],Loterias.getDezenaInicial()):                
                if int(linha[0]) >= ultimosSorteios:
                    j = int(item)                    
                    matrizTotais[(i,j)] += 1
                else:
                    i = 0
                    break
        
        return matrizTotais
    
   
    
    def _rand(self,numerodezenas):
        return random.randint(1, numerodezenas )
             
    def SortearDezenas(self,Loteria, numJogos):
        '''Sortear numeros '''
        jogo = []        
        for i in range(0, numJogos ):
            numeros = []            
            for j in  Loteria.getNumeroBolasIter():
                x = self._rand(Loteria.getNumeroDezenas())                
                while x in numeros:
                    x = self._rand(Loteria.getNumeroDezenas()) 
                numeros.append(x)
            jogo.append(numeros)
    
        return jogo       
            
    
    def __init__(self):       
        pass 
       

