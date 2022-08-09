def tamanho(lista):
  cont = 0
  for i in lista:
    cont = cont + 1
  return cont    
lista = ["abacate", "mamao", "limao", "tomate"]
a = tamanho(lista)
print(a)

def apagaGeral(lista):
  lista = []
  return lista
l = apagaGeral(lista)
print(l)

def chama(valor, lista):
    if valor in lista:
      return "true"
    else:
      return "false"
fruta = input()
d = chama(fruta, lista)
print(d)


  
    
    
    
    
