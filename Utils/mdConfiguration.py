'''
Created on 22/09/2011

@author: Evaldo
'''
import ConfigParser
import sys, os
from mdParametrosLoterica import *

class Config(object):
    '''
    classdocs
    '''    
    def setConfig(self,section,parserResultado):

        config = ConfigParser.ConfigParser() 
        config.read(self._fileName)       
        
        if not config.has_section(section):
            config.add_section(section)
        
        config.set(section, "url", parserResultado.url)
        config.set(section, "arqZip", parserResultado.arqZip)
        config.set(section, "arqHtml", parserResultado.arqHtml)
        config.set(section, "arqMatriz", parserResultado.arqMatriz)       
               
        f = open(self._fileName, "w")
        config.write(f)
        f.close()
        
    def getConfig(self,section):
        config = ConfigParser.ConfigParser()
        config.read(self._fileName)
        
        arquivos = ParametrosLoterias()        
       
        arquivos.url = config.get(section, "url")
        arquivos.arqZip = config.get(section, "arqZip")
        arquivos.arqHtml = config.get(section, "arqHtml") 
        arquivos.arqMatriz = config.get(section, "arqMatriz")
        
        return arquivos        
       
        
    def __init__(self, fileName):
        '''
        Constructor
        '''        
        self._fileName = fileName                      
             
        
if __name__ == '__main__':
    path = sys.path[0] + os.sep + 'Arquivo' + os.sep
    
    a = Config('loterias.ini')
    
    megaSena= ParametrosLoterias()        
   
    megaSena.arqZip = 'mega.zip'
    megaSena.arqHtml = 'D_MEGA.HTM'
    megaSena.arqMatriz = 'MatrizMegaSena.txt'    
    megaSena.url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
    
    a.setConfig('MegaSena', megaSena)
    
    LotoFacil = ParametrosLoterias()  
    LotoFacil.url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip'
    LotoFacil.arqZip = 'LotoFacil.zip'
    LotoFacil.arqHtml = 'D_LOTFAC.HTM'
    LotoFacil.arqMatriz = 'MatrizLotoFacil.txt' 
    a.setConfig('LotoFacil', LotoFacil)
    
    quina=ParametrosLoterias()      
    quina.url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_quina.zip'
    quina.arqZip = 'quina.zip'
    quina.arqHtml = 'D_QUINA.HTM'
    quina.arqMatriz = 'MatrizQuina.txt' 
      
    a.setConfig('Quina', quina)

    LotoMania=ParametrosLoterias()      
    LotoMania.url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip'
    LotoMania.arqZip = 'LotoMania.zip'
    LotoMania.arqHtml = 'D_LOTMAN.HTM'
    LotoMania.arqMatriz = 'MatrizLotoMania.txt' 
      
    a.setConfig('LotoMania', LotoMania)
    
    Federal=ParametrosLoterias()     
    Federal.url = 'http://www1.caixa.gov.br/loterias/loterias/federal/federal_resultado.asp'
    Federal.arqZip = 'Federal.zip'
    Federal.arqHtml = 'D_LOTFED.HTM'
    Federal.arqMatriz = 'MatrizFederal.txt' 
      
    a.setConfig('Federal', Federal)
    
    
    DuplaSena = ParametrosLoterias()  
    DuplaSena.url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/d_dplsen.zip'
    DuplaSena.arqZip = 'DuplaSena.zip'
    DuplaSena.arqHtml = 'D_DPLSEN.HTM'
    DuplaSena.arqMatriz = 'MatrizDuplaSena.txt' 
      
    a.setConfig('DuplaSena', DuplaSena)
    
    
    TimeMania = ParametrosLoterias()  
    TimeMania.url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_timasc.zip'
    TimeMania.arqZip = 'TimeMania.zip'
    TimeMania.arqHtml = 'D_TIMASC.HTM'
    TimeMania.arqMatriz = 'MatrizTimeMania.txt' 
      
    a.setConfig('TimeMania', TimeMania) 