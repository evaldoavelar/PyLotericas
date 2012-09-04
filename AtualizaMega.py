from Download.DownloadFile import *
from Descompactar.ZIPFile import *
from Processar.HtmlToTxt import *  

from Tkinter import *

#from DataBase.MysqlDB import * 
import sys, os
from UI.FrmPrincipal import FrmPrincipal

def download(Url,ArqZip):
    print 'Baixando...' 
    d = Downloads()
    d.FileFromUrl(Url, ArqZip)
    print 'Concluido'

def descompactar(ArqZip,path):
    print ('Descompactando arquivo...')
    z = ZipLib()
    z.Descompactar(ArqZip, path)
    print 'Concluido'
    
def htmlTXT(ArqHTMl,ArqTxt):
    h = HtmlTotxt()
    print 'Processando arquivo...'
    h.ProcessarArquivo(ArqHTMl, ArqTxt)
    print 'Concluido'
    

def gravarBd(ArqSql):
    '''print 'Gravando no banco...'
    m = MysqlDataBase()
    m.executeScript(ArqSql)
    print 'Concluido'''

        


if __name__ == '__main__':

    path = sys.path[0] + os.sep + 'Arquivo' + os.sep
    
    if not os.path.exists(path):
        os.mkdir(path)
    
    ArqZip = path + 'm.zip'
    ArqHTMl = path + 'D_MEGA.HTM'
    ArqTxt = path + 'm.txt'
    ArqSql = path + 'm.sql'
    Url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
    
    #Url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip'
    #ArqHTMl = path + 'D_MEGAsc.HTM'
    
    try:       
               
      root = Tk()
      
      root.geometry("%dx%d%+d%+d" % (600, 400, 0, 0))
      
      app = FrmPrincipal(root)
            
      root.mainloop() 
        
    except Exception as e:
        print 'Erro' , e
