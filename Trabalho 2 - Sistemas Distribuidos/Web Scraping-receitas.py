
# ### Importar Bibliotecas
from tqdm import tqdm
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

# ### URL alvo para Web Scrapping
url = 'https://www.confina.com.br/receitas'

# Captura todos os links de receitas da pagina.

def get_lyrics(band):
    try:
        print('Obtendo links/Receitas')
        # Lista, com valores únicos
        ctrl_page = set()
        html = urlopen(f"{url}/{band}")

        # Parser das tags HTML
        bs = BeautifulSoup(html, 'html.parser')
        bs.prettify()

        # Neste momento estamos filtrando as tags do tipo <a> que estão contidas na tag <ol> da página
        for link in bs.find_all('a', class_=['tag', 'sabor-do-interior']):
            if 'href' in link.attrs:
                # Adicionando as páginas que contém a receitas em uma lista
                ctrl_page.add(f"{link.attrs['href']}")


        for lyrics in ctrl_page:
            # Chamar Função pra ler a sub-página que contém a receita completa, além do nome da receita
            get_receitas(band, lyrics)
            # print(band,lyrics)

    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')


# Captura todas as receitas de uma pagina.

def get_receitas(band, new_page):
    music = ''

    try:
        #lendo as Lista de ingredientes
        html = urlopen(f"{new_page}")
        # parser novamente com a página html lida
        bs = BeautifulSoup(html, 'html.parser')

        # Estamos lendo os versos que estão separados por tags <p>
        # posteriormente nós limpamos e agrupamos a letra.
        for verse in tqdm(bs.find('div', {'class': 'text'}).find_all('p')):
            music += ' '.join(verse.stripped_strings)
            music += ' '

        # coleta do título da música na tag <div> com a class 'cnt-head_title'
        title_receita = bs.find(
            'div', {'class': 'title large'}).find_all('h3')[0]
        title_receita = ' '.join(title_receita.stripped_strings)

        # Salvando estas informações
        save_lyrics(band, music, title_receita)

        print("Receita Capturada : " + title_receita)
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')

#### Salvar as receitas em Lista
# Salva receitas em disco no formato .txt contanto o padrão '<b>band</b>$<b>title</b>.txt'

def save_lyrics(band, music, title_music):

    plain_text = music.lower()

    try:
        print(plain_text, file=open("data" + os.sep +
              band + "$" + title_music+'.txt', 'w'))
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar gravar o arquivo. {e}')

#### Capturando Ingredientes de Receitas

#ALMOÇO
get_lyrics("?_sft_receita-ocasiao=almoco")

#CAFÉ DA MANHA
get_lyrics("?_sft_receita-ocasiao=cafe-da-manha")

#PETISCOS - SALGADOS
get_lyrics("?_sft_receita-ocasiao=petiscos")




