'''
Created on 21/09/2011

@author: Evaldo
'''
import os

class Txt2Sql(object):
    
    def _montaWhere(self, concurso, data, dezena1, dezena2, dezena3, dezena4, dezena5, dezena6):
        if self._dataBase == 'mysql':
            bdData = data[6:10]  + '/' + data[3:5] + '/' + data[0:2]
        else:
            bdData = data
            
        sql = "insert into sorteios (Concurso,DataSorteio,Dezena1,Dezena2,Dezena3,Dezena4,Dezena5,Dezena6) values ({0},'{1}',{2},{3},{4},{5},{6},{7});"
        return sql.format(concurso, bdData, dezena1, dezena2, dezena3, dezena4, dezena5, dezena6)     
    
    def GeraSql(self, fileName, rSql):
        
        if os.path.isfile(rSql): 
            os.remove(rSql)
        
        arqTXT = open(fileName)
        arqSQL = open(rSql, 'a')
        
        sql = 'delete from sorteios;'
        arqSQL.write(sql + '\n')
        
        try:
            for linha in arqTXT:
                colunas = linha.split('|')
                if len(colunas) > 1:
                    sql = self._montaWhere(colunas[0], colunas[1], colunas[2], colunas[3], colunas[4], colunas[5], colunas[6], colunas[7])
                    arqSQL.write(sql + '\n')
        finally:
            arqTXT.close() 
            arqSQL.close()         
            
    def __init__(self, database):
        self._dataBase = database
'''  
if  __name__ == '__main__':
    t = Txt2Sql('mysql')
    print 'gerando sql' 
    t.GeraSql('r.txt')
    print 'concluido' '''
