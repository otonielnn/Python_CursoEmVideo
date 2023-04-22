"""
   Crie um código em Python que teste se o site Pudim.com.br está acessível pelo computador usado. 
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    # print(site.read())
