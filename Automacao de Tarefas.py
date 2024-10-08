#Sempre pensar como EU FARIA MANUALMENTE O PROCESSO QUE EU DESEJO QUE O PROGRAMA EXECUTE
# Etapa  1 : Entrar no Sistema da Empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)

import pyautogui #Biblioteca que permite controlar o mouse teclado e tela do computador por códigos
import time
import pandas #Biblioetca mais usada para tratativa de dados

    #Abrir o navegador e abrir uma nova guia
pyautogui.PAUSE = 0.5 #Da um tempo antes de executar a próxima ação (Tempo necessário para que não haja erro entre o tempo que o computador demora para executar as informações)
pyautogui.click  # Clica com o Mouse | O lugar da tela é definido por valores de um plano cartesiano (valores de x,y)
pyautogui.press("win")  # Aperta uma tecla
pyautogui.write("chrome")  # Escreve um texto
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)
# Etapa 2: Fazer o login no sistema
pyautogui.click(x=603, y=470)
pyautogui.write("caiomedtrindade@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=959, y=675)

#Etapa 3: Importar a Base de Dados (Usando a biblioetca Pandas)
#Fazer que o programa leia a base de dados e armazene no código
# Importante lembrar, o arquivo precisa estar na mesma pasta que o nosso código, se não teria que passar todo o caminho seguido pelo aplicativo de arquivos para encontrar
tabela = pandas.read_csv("Python First Automatized Project/produtos.csv")
print(tabela)
#Etapa 4: Cadastrar um Produto  
pyautogui.click(x=605, y=331)
linha = 0
for linha in tabela.index:
 #Codigo do Produto 
    codigo = tabela.loc[linha, "codigo"]  # O pandas só identifica em colchetes
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # Marca do Produto
    marca = tabela.loc[linha, "marca"] 
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # Tipo do Produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # Categoria do Produto
    categoria = tabela.loc[linha, "categoria"] 
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # Preço Unitário do Produto
    preco_unitario = tabela.loc[linha, "preco_unitario"]  
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    # Custo do Produto
    custo = tabela.loc[linha, "custo"]  
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #OBS do Produto
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    #Voltando para o inicio da página
    pyautogui.scroll(7777)
    pyautogui.click(x=605, y=331)   
    # Repetir o processo até o ultimo Produto
