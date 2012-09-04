'''
Created on 26/09/2011

@author: Evaldo
'''

from Download.DownloadFile import *
from Descompactar.ZIPFile import *
from Processar.HtmlToTxt import *  
from Utils.mdConfiguration import *
from Tkinter import *
import ttk
from Utils.mdLoterica import Loterias
from Utils.mdConcursos import MatrizConcursos
from Utils.mdCalculos import ConcursoCalculos


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        self.configure(yscrollcommand=self._autoscroll(vsb),
            xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (took from ScrolledText.py)
        methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class FrmPrincipal():
    '''
    classdocs
    '''
    def __adicionarColunas(self):
        bolas = ['Dezenas']
        for x in range(1, self._Loteria.getNumeroBolas() + 1):  
            bolas.append('Bola{0}'.format(x))
        bolas.append('Total')        
        
        self.Scrolledtreeview1['columns'] = bolas#('Dezena','Dezena1', 'Dezena2', 'Dezena3', 'Dezena4', 'Dezena5', 'Dezena6','Total')    
        
        for x in bolas:
            self.Scrolledtreeview1.column(x, width=45 , anchor='center')
            self.Scrolledtreeview1.heading(x, text=x)  
        
        self.Scrolledtreeview1.column('#0', width=45 , anchor='center')
    
    def _deleteWidgets(self):
        try:
            self.Scrolledtreeview1.delete('widgets')
        except:
            pass
        
        try:
            self.Scrolledtreeview1.delete('Totais')
        except:
            pass
            
    def _atualizar(self): 
        print 'Baixando...' 
        d = Downloads()
        d.FileFromUrl(self._Loteria.Parametros.url, self._path + self._Loteria.Parametros.arqZip)
        print 'Concluido'

        print ('Descompactando arquivo...')
        z = ZipLib()
        z.Descompactar(self._path + self._Loteria.Parametros.arqZip, self._path)
        print 'Concluido'
    
        print 'Processando arquivo...'
        h = HtmlTotxt(self._Loteria)        
        h.ProcessarArquivo(self._path + self._Loteria.Parametros.arqHtml, self._path + self._Loteria.Parametros.arqMatriz)
        print 'Concluido'
        
        self.MatrizConcursos.updateMatriz()
        
    def __listarSorteioPorDezenas(self):
        self._deleteWidgets()
        
        id = self.Scrolledtreeview1.insert('', 'end', 'widgets', text='Sorteio Por Dezenas')
        
        self.__adicionarColunas()
        
        self.Scrolledtreeview1.column('#0', width=80 , anchor='center') 
               
        concurso = ConcursoCalculos()
               
        TotaisSorteios =  concurso.getTotaisPorDezena(self.MatrizConcursos.getMatriz(), self._Loteria)
              
        for i in range(0, self._Loteria.getNumeroDezenas() + 1): 
            total = 0
            l = []
            l.append(i)
            for j in range(1, self._Loteria.getNumeroBolas() + 1):
                total = total + TotaisSorteios[(i, j)]
                l.append(TotaisSorteios[(i, j)])
            l.append(total)            
            self.Scrolledtreeview1.insert(id, 'end', text='', values=l)
        
        self.Scrolledtreeview1.item('widgets', open=TRUE)
        self._TotaisTotaisPorDezenas(TotaisSorteios)
    
    def __listarSorteios(self):      
        self._deleteWidgets()            
        # Inserted at the root, program chooses id:
        id = self.Scrolledtreeview1.insert('', 'end', 'widgets', text='Sorteios')
        
        self.__adicionarColunas()               
              
        for i in self.MatrizConcursos.getMatriz():
            total = 0
            l = []    
            l.append(i[:1][0])
                     
            for num in i[1:]:
                l.append(num)
                total = total + int(num)
            l.append(total)         
            
            self.Scrolledtreeview1.insert(id, 'end', text='', values=l)
        
        self.Scrolledtreeview1.item('widgets', open=TRUE)
        self._TotaisTotaisPorDezenas(self.MatrizConcursos.getMatriz())
        
    def _TotaisTotaisPorDezenas(self,matriz):
        id = self.Scrolledtreeview1.insert('', 'end', 'Totais', text='Totais por dezenas')
        
        self.__adicionarColunas()
        
        concurso = ConcursoCalculos()
               
        TotaisSorteios =  concurso.getTotaisSorteios(matriz, self._Loteria)
            
        l = []
         
        for i,j in TotaisSorteios.items():
            l.append(i)
            l.append(j) 
            self.Scrolledtreeview1.insert(id, 'end', text='', values=l)
            l = []
    
    def sortearDezenas(self):
        self._deleteWidgets()            
        # Inserted at the root, program chooses id:
        id = self.Scrolledtreeview1.insert('', 'end', 'widgets', text='Sorteios')
        
        self.__adicionarColunas()
        
        concurso = ConcursoCalculos()
        
        dezenasSoteadas =  concurso.SortearDezenas(self._Loteria,10)
        for x in dezenasSoteadas:
            total = 0
            l = [] 
             
            for num in x:
                l.append(num)
                total = total + int(num)
            l.append(total)         
            
            self.Scrolledtreeview1.insert(id, 'end', text='', values=l)
                        
        self._TotaisTotaisPorDezenas(dezenasSoteadas)
          
    
    def listarSorteiosMegaSena(self):
        self._setLoteria('MegaSena')
        self.__listarSorteios()
        
    def listarSorteiosLotoFacil(self):
        self._setLoteria('LotoFacil')
        self.__listarSorteios()
        
    def listarSorteiosQuina(self):
        self._setLoteria('Quina')
        self.__listarSorteios()
        
    def listarSorteiosLotoMania(self):
        self._setLoteria('LotoMania')
        self.__listarSorteios()
    
    def listarSorteiosDuplaSena(self):
        self._setLoteria('DuplaSena')
        self.__listarSorteios()
    
    def listarSorteiosTimeMania(self):
        self._setLoteria('TimeMania')
        self.__listarSorteios()  
        
    def sortearDezenasMegaSena(self):
        self._setLoteria('MegaSena')
        self.sortearDezenas()
        
    def sortearDezenasLotoFacil(self):
        self._setLoteria('LotoFacil')
        self.sortearDezenas()
        
    def sortearDezenasQuina(self):
        self._setLoteria('Quina')
        self.sortearDezenas()
        
    def sortearDezenasLotoMania(self):
        self._setLoteria('LotoMania')
        self.sortearDezenas()
        
    def sortearDezenasDuplaSena(self):
        self._setLoteria('DuplaSena')
        self.sortearDezenas()
        
    def sortearDezenasTimeMania(self):
        self._setLoteria('TimeMania')
        self.sortearDezenas()
            
    def listarSorteioPorDezenasMegaSena(self):
        self._setLoteria('MegaSena')
        self.__listarSorteioPorDezenas()
        
    def listarSorteioPorDezenasLotoFacil(self):
        self._setLoteria('LotoFacil')
        self.__listarSorteioPorDezenas()
        
    def listarSorteioPorDezenasQuina(self):
        self._setLoteria('Quina')
        self.__listarSorteioPorDezenas()
    
    def listarSorteioPorDezenasLotoMania(self):
        self._setLoteria('LotoMania')
        self.__listarSorteioPorDezenas()
        
    def listarSorteioPorDezenasDuplaSena(self):
        self._setLoteria('DuplaSena')
        self.__listarSorteioPorDezenas()
        
    def listarSorteioPorDezenasTimeMania(self):
        self._setLoteria('TimeMania')
        self.__listarSorteioPorDezenas()    
    
    def atualizaMegaSena(self):
        self._setLoteria('MegaSena')
        self._atualizar()
    
    def atualizaLotoFacil(self):
        self._setLoteria('LotoFacil')
        self._atualizar() 
        
    def atualizaQuina(self):
        self._setLoteria('Quina')
        self._atualizar() 
        
    def atualizaLotoMania(self):
        self._setLoteria('LotoMania')
        self._atualizar() 
        
    def atualizaDuplaSena(self):
        self._setLoteria('DuplaSena')
        self._atualizar() 
        
    def atualizaTimeMania(self):
        self._setLoteria('TimeMania')
        self._atualizar()         
    
     
    def _setLoteria(self, loteria):        
        self._Loteria.setLoteria(loteria) 
        self.MatrizConcursos = MatrizConcursos(os.path.join(self._path , self._Loteria.Parametros.arqMatriz))
        self.MatrizConcursos.updateMatriz()  
         
    def __init__(self, master):
        '''
        Constructor
        '''        
        self._path = sys.path[0] + os.sep + 'Arquivo' + os.sep
        #self._path = os.path.join(sys.path[0],'Arquivo',os.sep)
        self._Loteria = Loterias()
        
        self._setLoteria('MegaSena')
        self._master = master 
        
        # Set background of toplevel window to match
        # current style
        style = ttk.Style()
        theme = style.theme_use()
        default = style.lookup(theme, 'background')
        master.configure(background=default)
      
       
        menubar = Menu(master)
        menuMegaSena = Menu(menubar, tearoff=0)
        menuMegaSena.add_command(label="Atualizar", command=self.atualizaMegaSena)
        menuMegaSena.add_command(label="Resultado Sorteios", command=self.listarSorteiosMegaSena)
        menuMegaSena.add_command(label="Sorteio Por Dezenas", command=self.listarSorteioPorDezenasMegaSena)
        menuMegaSena.add_command(label="Sortear Dezenas", command=self.sortearDezenasMegaSena)
        menubar.add_cascade(label="Mega Sena", menu=menuMegaSena)
        
        menuLotoFacil = Menu(menubar, tearoff=0)
        menuLotoFacil.add_command(label="Atualizar", command=self.atualizaLotoFacil)
        menuLotoFacil.add_command(label="Resultado Sorteios", command=self.listarSorteiosLotoFacil)
        menuLotoFacil.add_command(label="Sorteio Por Dezenas", command=self.listarSorteioPorDezenasLotoFacil)
        menuLotoFacil.add_command(label="Sortear Dezenas", command=self.sortearDezenasLotoFacil)
        menubar.add_cascade(label="Loto Facil", menu=menuLotoFacil)
        
        menuQuina = Menu(menubar, tearoff=0)
        menuQuina.add_command(label="Atualizar", command=self.atualizaQuina)
        menuQuina.add_command(label="Resultado Sorteios", command=self.listarSorteiosQuina)
        menuQuina.add_command(label="Sorteio Por Dezenas", command=self.listarSorteioPorDezenasQuina)
        menuQuina.add_command(label="Sortear Dezenas", command=self.sortearDezenasQuina)
        menubar.add_cascade(label="Quina", menu=menuQuina)
        
        menuLotoMania = Menu(menubar, tearoff=0)
        menuLotoMania.add_command(label="Atualizar", command=self.atualizaLotoMania)
        menuLotoMania.add_command(label="Resultado Sorteios", command=self.listarSorteiosLotoMania)
        menuLotoMania.add_command(label="Sorteio Por Dezenas", command=self.listarSorteioPorDezenasLotoMania)
        menuLotoMania.add_command(label="Sortear Dezenas", command=self.sortearDezenasLotoMania)
        menubar.add_cascade(label="Loto Mania", menu=menuLotoMania)
        
        
        menuDuplaSena = Menu(menubar, tearoff=0)
        menuDuplaSena.add_command(label="Atualizar", command=self.atualizaDuplaSena)
        menuDuplaSena.add_command(label="Resultado Sorteios", command=self.listarSorteiosDuplaSena)
        menuDuplaSena.add_command(label="Sorteio Por Dezenas", command=self.listarSorteioPorDezenasDuplaSena)
        menuDuplaSena.add_command(label="Sortear Dezenas", command=self.sortearDezenasDuplaSena)
        menubar.add_cascade(label="Dupla Sena", menu=menuDuplaSena)
        
        menuTimeMania = Menu(menubar, tearoff=0)
        menuTimeMania.add_command(label="Atualizar", command=self.atualizaTimeMania)
        menuTimeMania.add_command(label="Resultado Sorteios", command=self.listarSorteiosTimeMania)
        menuTimeMania.add_command(label="Sorteio Por Dezenas", command=self.listarSorteioPorDezenasTimeMania)
        menuTimeMania.add_command(label="Sortear Dezenas", command=self.sortearDezenasTimeMania)
        menubar.add_cascade(label="Time Mania", menu=menuTimeMania)
        
        
        master.config(menu=menubar)



        self.Scrolledtreeview1 = ScrolledTreeView (master)
        self.Scrolledtreeview1.place(relx=0.01, rely=0.06, relheight=0.87
                , relwidth=0.97)
