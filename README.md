PyLotericas
===========

Pequeno aplicativo em Pyqt que busca as informações das Loterias da caixa e mostra os resultados em um Grid.
O objetivo desse aplicativo é o estudo do Python e do PyQt4.
Se for iniciante neste mundo do PyQt4, este projeto lhe ajudara um pouco.


Como Funciona
=============
O PyLoterias acessa o site da caixa por meio de um requisição HTTP e realiza o download de um arquivo zip com últimos resultados
das loterias. Este arquivo,no formato html, é processado e transformado em uma matriz que é gravada em um arquivo txt.
o arquivo é lido e o resultado final é exibido em um QtableWidget.

Requisitos
=============
PyQt4
QtDesigner
Python 2.7.2

