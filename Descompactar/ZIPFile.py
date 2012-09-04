'''
Created on 21/09/2011

@author: Evaldo
'''

import zipfile
import os

class ZipLib(object):
    '''
    classdocs
    '''
    def Descompactar(self, fileName,path):
        #Abra o arquivo em modo de leitura
        Arquivos = zipfile.ZipFile(fileName, 'r')
    
        #Extract every file from it
        for arquivo in Arquivos.namelist():
            b = open(os.path.join(path,arquivo), 'wb')
            b.write(Arquivos.read(arquivo))
            b.close()
        #Fecha o aruqivo
        Arquivos.close() 

    def __init__(self):
        '''
        Constructor
        '''
        pass
        
if __name__ == '__main__':
        try:
            print ('Descompactando arquivo')
            z = ZipLib()
            z.Descompactar('m.zip')
            print 'Concluido'
        except Exception as e:
            print 'Erro: ',e