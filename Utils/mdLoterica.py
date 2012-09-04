'''
Created on 29/09/2011

@author: Evaldo


Este modulo e contem operacoes para loterias

'''
import os
import sys
from mdConfiguration import Config
from mdParametrosLoterica import *
from mdExceptions import TipoLoteriaException

class Loterias(object):
    '''
    Classe Reponsavel por definir as Loterias 
    '''
    
    
    def getNumeroDezenas(self):        
        return  self._Loterias.get(self._TipoLoteria).get('dezenas')
   
    def getDezenaInicial(self):        
        return  self._Loterias.get(self._TipoLoteria).get('dezenaInicial') 
        
    def getNumeroDezenasIter(self):        
        return range(self.getDezenaInicial(), self.getNumeroDezenas()+1)            
        
    def getNumeroBolas(self):
        return  self._Loterias.get(self._TipoLoteria).get('bolas')    
     
    def getNumeroBolasIter(self):
        return range(self.getDezenaInicial(), self.getNumeroBolas() +1)                     
    
    def setLoteria(self, TipoLoteria):
        if not TipoLoteria in self._Loterias.keys():
            raise TipoLoteriaException('Tipo loteria invalido!')
        
        root = sys.path[0] 
        fileName = os.path.join(root, 'loterias.ini')                       
        config = Config(fileName)
        self.Parametros = config.getConfig(TipoLoteria)
        self._TipoLoteria = TipoLoteria        
        
        
    def getLoteria(self):
        return self._TipoLoteria
    
    
    def getLoteriasImplementadas(self):
        '''
            retorna todas as loterias implementadas na classe
        '''
        return self._Loterias.keys()
                
    
    def getLotericaDescricao(self):        
        return  self._Loterias.get(self._TipoLoteria).get('descricao')
        

    def __init__(self):
        '''
        Constructor
        '''       
        self._TipoLoteria = ''
        self.Parametros = ParametrosLoterias()
        self._Loterias = {}
        self._Loterias['MegaSena'] = {'descricao':'Mega Sena', 'dezenas':60,'dezenaInicial':1, 'bolas':6} 
        self._Loterias['LotoFacil'] = {'descricao':'Loto Facil', 'dezenas':5,'dezenaInicial':1, 'bolas':15}
        self._Loterias['LotoMania'] = {'descricao':'Loto Mania', 'dezenas':100,'dezenaInicial':0, 'bolas':20}
        self._Loterias['Quina'] = {'descricao':'Quina', 'dezenas':80,'dezenaInicial':1, 'bolas':5}
        self._Loterias['Federal'] = {'descricao':'Federal', 'dezenas':1,'dezenaInicial':1, 'bolas':5}
        self._Loterias['DuplaSena'] = {'descricao':'Dupla Sena', 'dezenas':50,'dezenaInicial':1, 'bolas':6}       
        self._Loterias['TimeMania'] = {'descricao': 'Time Mania', 'dezenas':80,'dezenaInicial':1, 'bolas':7}
          
