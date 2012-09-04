'''
Created on 20/09/2011

@author: Evaldo
'''
import cookielib,urllib2,urllib,pdb

class Downloads(object):
    '''
    classdocs
    '''
 
    def FileFromUrl(self,url, localFileName = None):        
        #post = urllib.urlencode({"security" : "false"})
        request = urllib2.Request( url)
        response = urllib2.urlopen( request )
       
        '''self._cookies.extract_cookies( response, request )
        for cookie in self._cookies:
            if cookie.name.startswith('security'):
                self._logged_in = True
                break    
        '''
        
        '''
             Salvar o arquivo
        '''
        output = open(localFileName,'wb')
        output.write(response.read())
        output.close()


    def __init__(self):
        '''
        Constructor
        '''
        self._logged_in = False
        self._cookies = cookielib.CookieJar()
        self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._cookies))
        urllib2.install_opener(self._opener)
      
if __name__ == '__main__':
    #pdb.set_trace()
    try:
        print 'Baixando' 
        d = Downloads()
        d.FileFromUrl('http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip','m.zip')
        print 'Concluido'
    except Exception as e:
        print 'Erro' , e
