# -*- coding: iso-8859-1 -*-
'''
Created on 04/10/2011

@author: Evaldo
'''

import os
import sys
from PyQt4  import QtGui, QtCore, Qt
from QfrmPrincipal  import Ui_MainWindow
from Utils.mdLoterica import Loterias
from Utils.mdConcursos import MatrizConcursos
from Utils.mdCalculos import ConcursoCalculos
from Download.DownloadFile  import  Downloads
from Processar.HtmlToTxt    import HtmlTotxt
from Descompactar.ZIPFile   import ZipLib
from QQuantidadeIMP import QNumSorteioIMP


class QfrmPrincipalIMP(QtGui.QMainWindow, Ui_MainWindow):

    '''        
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''

        super(QfrmPrincipalIMP, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.action_sair, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.connect(self.action_mega_Sena, QtCore.SIGNAL('triggered()'), self.setMegaSena)
        self.connect(self.action_loto_facil, QtCore.SIGNAL('triggered()'), self.setLotoFacil)
        self.connect(self.action_quina, QtCore.SIGNAL('triggered()'), self.setQuina)
        self.connect(self.action_loto_mania, QtCore.SIGNAL('triggered()'), self.setLotoMania)
        self.connect(self.action_dupla_sena, QtCore.SIGNAL('triggered()'), self.setDuplaSena)
        self.connect(self.action_time_mania, QtCore.SIGNAL('triggered()'), self.setTimeMania)
        self.connect(self.action_sorteio_Por_Dezenas, QtCore.SIGNAL('triggered()'), self.__listarSorteioPorDezenas)
        self.connect(self.action_atualizar, QtCore.SIGNAL('triggered()'), self.__atualizarLoterica)
        self.connect(self.action_resultado_Sorteios, QtCore.SIGNAL('triggered()'), self.__listarSorteios)
        self.connect(self.action_sortear_Dezenas, QtCore.SIGNAL('triggered()'), self.__sortearDezenas)
        self.connect(self.tableWidget, QtCore.SIGNAL('cellClicked(int, int)'), self.__cellClick)
        self.connect(self.action_ajustar_colunas, QtCore.SIGNAL('triggered()'), self.__ajustaColunasTabela)
        self.connect(self.action_ajustar_linhas, QtCore.SIGNAL('triggered()'), self.__ajustaColunasLinhas)
        self.connect(self.tableWidget, QtCore.SIGNAL('itemSelectionChanged()'), self.__itemSelectionChanged)
        self.connect(self.btnAdicionar, QtCore.SIGNAL('clicked()'), self.__addSelecao)
        self.connect(self.btnRemover, QtCore.SIGNAL('clicked()'), self.__removeItemLista)
        self.connect(self.btnCopiar, QtCore.SIGNAL('clicked()'), self.__copiarLista)
        self.connect(self.tableWidget.horizontalHeader(), QtCore.SIGNAL('sectionClicked(int)'), self.__tableColumnClicked) #clicar na coluna da tabela
          
        rootDir = sys.path[0]
        self._Loterica = Loterias()
        self._Loterica.setLoteria('MegaSena')
        self.dirArquivos = os.path.join(rootDir, 'Arquivo')
        self.MatrizConcursos = MatrizConcursos(self._Loterica)
        self._selecao = {}
        #self.tableWidget.setStyleSheet("show-decoration-selected: 1;selection-color: #CCC;selection-background-color: white;");
        self.__centralizar()
        
    def __centralizar(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)        
        
    def __tableColumnClicked(self,pos):
        self.tableWidget.sortByColumn(pos)
    
    def __copiarLista(self):
        if self.listSelecionados.count():
            items = []
            for index in xrange(self.listSelecionados.count()):
                item = self.listSelecionados.item(index)
                items.append(str(item.text()))
            
            QtGui.QApplication.clipboard().setText( '\n'.join(items))
            print  'Seleção Copiado para clipboard'
    
    def __removeItemLista(self):
        if self.listSelecionados.count():
            reply = QtGui.QMessageBox.question(self, 'Pergunta',"Remover a Seleção?", QtGui.QMessageBox.Yes |QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:            
                self.listSelecionados.removeItemWidget(self.listSelecionados.takeItem(self.listSelecionados.currentRow()))
        
    def __addSelecao(self):  
        if not self.tableWidget.isSortingEnabled():      
            if self._selecao:
                if len(self._selecao) <> self._Loterica.getNumeroBolas():
                    msg = "A aposta esta incorreta! Numero de bolas sorteadas para esta loteria: %s" % self._Loterica.getNumeroBolas()
                    QtGui.QMessageBox.warning(self, 'Aviso',msg)
                else:                
                    msg = '%s: %s' % (self._Loterica.getLotericaDescricao(), ''.join(', '.join([x for x in self._selecao.values()])).rjust(5,' '))
                    item = QtGui.QListWidgetItem()
                    item.setText(QtGui.QApplication.translate("MainWindow", msg  , None, QtGui.QApplication.UnicodeUTF8))        
                    self.listSelecionados.addItem(item)       
                    print msg 
                    self.__resetCellColor()
                    self._selecao.clear()
                    self.statusBar().showMessage(QtCore.QString('')) 
                    
    def __resetCellColor(self):
        color = QtGui.QColor(255,255,255)
        brush = QtGui.QBrush(color)
        
        for i,j in  self._selecao.keys():
            self.tableWidget.item(i,j).setBackground(brush)
                 
    
    def __itemSelectionChanged (self):
             
        #self.__resetCellColor()
        '''        
        color = QtGui.QColor(247,241, 45)
        brush = QtGui.QBrush(color)
        
        lst = self.tableWidget.selectedIndexes()
        self._selecao = []
        for i in lst:                        
            if  self._selecao:
                self._selecao.append(', ')
            self._selecao.append(str(i.data().toString()))            
            self.tableWidget.itemFromIndex(i).setBackground(brush)
            
        msg = ' %d Selecionado(s) : %s' % (len(lst), ''.join(self._selecao))
        self.lblStatus.clear()
        #self.lblStatus.setText( '%d Selecionado(s) : %s' %( len(lst), ''.join( self._selecao) )  )
        self.statusBar().showMessage(QtCore.QString(msg)) 
        '''
        
    def __cellClick(self, row, col):
        
        item = self.tableWidget.item(row, col)
        valor = str(item.data(0).toString())
        key = (row,col)        
        
        '''Chave ja existe, remove a selecao'''
        if  self._selecao.has_key(key):
            color = QtGui.QColor(255,255, 255)
            brush = QtGui.QBrush(color)
            item.setBackground(brush)
            self._selecao.pop(key)
        elif valor in self._selecao.values() :
            '''Valor ja existe'''
            pass      
        else:        
            self._selecao[key] = valor            
            color = QtGui.QColor(247,241, 45)
            brush = QtGui.QBrush(color)
            item.setBackground(brush)
        sorted(self._selecao.items())         
        msg = ' %d Selecionado(s) : %s' % (len( self._selecao), ', '.join([x for x in self._selecao.values()]))
        self.lblStatus.clear()        
        self.statusBar().showMessage(QtCore.QString(msg)) 
        

    def __ajustaColunasTabela(self):
        self.tableWidget.resizeColumnsToContents()
        
    
    def __ajustaColunasLinhas(self):
        self.tableWidget.resizeRowsToContents()
        
        
    def setMegaSena(self):
        self.__setLoterica('MegaSena')
        

    def setLotoFacil(self):
        self.__setLoterica('LotoFacil')


    def setQuina(self):
        self.__setLoterica('Quina')


    def setLotoMania(self):
        self.__setLoterica('LotoMania')


    def setDuplaSena(self):
        self.__setLoterica('DuplaSena')


    def setTimeMania(self):
        self.__setLoterica('TimeMania')        
        
    
    def __setLoterica(self, loterica):
        self._Loterica.setLoteria(loterica)
        self.__showMessageStatus(self._Loterica.getLotericaDescricao())
        titulo = 'Loteria: %s - %s Bolas e %s Dezenas' % ( self._Loterica.getLotericaDescricao(), self._Loterica.getNumeroBolas(),self._Loterica.getNumeroDezenas())
        self.label.setText(QtCore.QString(titulo ) )
        self.__listarSorteios()
        self._selecao.clear()
        
    
    def __showMessageStatus(self, msg):
        self.statusBar().showMessage(QtCore.QString(msg))            
        print msg

    def __atualizarLoterica(self):
        try:
            self.__showMessageStatus('Baixando...')
            
            d = Downloads()
            d.FileFromUrl(self._Loterica.Parametros.url, os.path.join(self.dirArquivos, self._Loterica.Parametros.arqZip))
            self.__showMessageStatus('Concluido.')            
            

            self.__showMessageStatus('Descompactando arquivo...')
            
            z = ZipLib()
            z.Descompactar(os.path.join(self.dirArquivos, self._Loterica.Parametros.arqZip), self.dirArquivos)
            
            self.__showMessageStatus('Concluido')
            
            self.__showMessageStatus('Processando arquivo...')
            
            h = HtmlTotxt(self._Loterica)
            h.ProcessarArquivo(os.path.join(self.dirArquivos, self._Loterica.Parametros.arqHtml), os.path.join(self.dirArquivos, self._Loterica.Parametros.arqMatriz))

            self.__showMessageStatus('Atualizacao Concluida')
            
            self.MatrizConcursos.updateMatriz()
            
            self.__listarSorteios()
            
            QtGui.QMessageBox.warning(self, 'Application', QtCore.QString('Atualizacao Concluida!'))
            self.statusBar().showMessage(QtCore.QString(self._Loterica.getLoteria()))                                  
            
        except Exception as e:
            print e
            QtGui.QMessageBox.critical(self, 'Erro encontrado', QtCore.QString(str(e)))


    def __AddItemLinhaTabela(self, row, col, valor):
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", valor, None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignCenter))
        self.tableWidget.setItem(row, col, item)


    def  __AddColunaTabelaHorizontalHeader(self, col, valor):
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", valor , None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(col, item)


    def __AddColunaTabelaVerticalHeaderItem(self, row, valor):
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", valor, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setVerticalHeaderItem(row, item)


    def __adicionarColunas(self, tam):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(tam)    #uma coluna a mais para o total

        for x in range(0, tam):
            self.__AddColunaTabelaHorizontalHeader(x, 'Bola {0}'.format(x + 1))
       

    def __listarSorteios(self):
        '''Lista os sorteios da loterica'''
        self.MatrizConcursos = MatrizConcursos(os.path.join(self.dirArquivos, self._Loterica.Parametros.arqMatriz))
        self.MatrizConcursos.updateMatriz()

        self.__adicionarColunas(self._Loterica.getNumeroBolas())
        self.tableWidget.setRowCount(self.MatrizConcursos.count())
        row = 0

        for i in self.MatrizConcursos.getMatriz():           
            col = 0            
            self.__AddColunaTabelaVerticalHeaderItem(row, i[:1][0])
            for num in i[1:]:
                self.__AddItemLinhaTabela(row, col, num)
                col = col + 1
            row = row + 1
        self.__calculaTotalRow()


    def __listarSorteioPorDezenas(self):
        '''Exibe sorteios agrupados por dezenas'''
        concurso = ConcursoCalculos()
        TotaisSorteios = concurso.getTotaisPorDezena(self.MatrizConcursos.getMatriz(), self._Loterica, self.__IformaQuantidade(0))

        self.__adicionarColunas(self._Loterica.getNumeroBolas())
        self.tableWidget.setRowCount(self._Loterica.getNumeroDezenas()) #Adicionar coluna a mais para o zero
       
    #    for r,v in enumerate(range(0,self._Loterica.getNumeroDezenas()),self._Loterica.getDezenaInicial()):
    #        self.__AddColunaTabelaVerticalHeaderItem(r,v)  
       
        for k, i in  TotaisSorteios.items():     
            if k == (60,5):
                pass                 
            self.__AddItemLinhaTabela(k[1]-1, k[0]-1, str(i))            
        
        self.__calculaTotalRow()
        
    
    def __sortearDezenas(self):
        '''Exibe a Lista de Dezenas Sorteadas '''
        
        numSorteio = self.__IformaQuantidade(10)
        self.__adicionarColunas(self._Loterica.getNumeroBolas() + 1)
        self.tableWidget.setRowCount(numSorteio)

        concurso = ConcursoCalculos()
        dezenasSoteadas = concurso.SortearDezenas(self._Loterica, numSorteio)

        for row , x in enumerate(dezenasSoteadas):
            total = 0
            for col, num in enumerate(x):
                self.__AddItemLinhaTabela(row, col, str(num))
                total = total + int(num)
        
        self.__calculaTotalRow()
        self.tableWidget.resizeColumnsToContents()

    
    def __calculaTotalRow(self):
        #Total
        col = self.tableWidget.columnCount() 
        self.tableWidget.setColumnCount(col + 1)
        self.__AddColunaTabelaHorizontalHeader(col, 'Total')
        
        for i in range(0, self.tableWidget.rowCount()):
            total = 0
            for j in range(0, self.tableWidget.columnCount() - 1):
                total += int(self.tableWidget.item(i, j).text())
            self.__AddItemLinhaTabela(i, col, str(total))
             

    def __IformaQuantidade(self, qtdedefault):
        ''' 
        Criar o dialogo e aguardar o seu retorno 
        '''        
        window = QNumSorteioIMP(self) 
        window.numeroSpinBox.setValue(qtdedefault)
        window.setWindowModality(QtCore.Qt.WindowModal)  
        window.exec_()
        
        return window.numeroSpinBox.value()
        
        
    
