'''
Created on 21/09/2011

@author: Evaldo
'''

from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
import os


class HtmlTotxt(HTMLParser):
    def __init__(self,Loteria):
        HTMLParser.__init__(self)
        self.__text = []
        self._Loteria = Loteria

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text)

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            pass#self.__text.append('|')
        elif tag == 'tr':
            self.__text.append('\n')
        elif tag == 'th':
            pass 

    def handle_endtag(self, tag):       
        if tag == 'td':
            self.__text.append('|')

    def text(self):
        return ''.join(self.__text).strip()


    def _GeraTxtMatriz(self,fileNameMatriz):
        
        if os.path.isfile(fileNameMatriz): 
            os.remove(fileNameMatriz)
                      
        
        arqMatriz = open(fileNameMatriz, 'a')
               
        try:
            for linha in self.text().split('\n'):
                colunas = linha.split('|')
                if len(colunas) > 1:
                    e = colunas[0:1] + colunas[2:self._Loteria.getNumeroBolas()+2]                    
                    for x in e:
                        arqMatriz.write(str(x)+'|')                   
                    
                    arqMatriz.write('\n')
        finally:            
            arqMatriz.close() 


    def ProcessarArquivo(self, fileName,arquivotxt):    
          
        try:
            f = open(fileName, 'r')
            text = f.read()
            f.close()              
            
            self.feed(text)
            self.close()
            
            self._GeraTxtMatriz(arquivotxt)   
            
            return arquivotxt
        except:
            print_exc(file=stderr)            
                     
       

if __name__ == '__main__':
    h = HtmlTotxt()
    print 'processando arquivo'
    h.ProcessarArquivo('D_MEGA.HTM')
    print 'concluido'
    
