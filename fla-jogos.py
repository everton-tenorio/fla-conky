import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve

# URL do site do Flamengo
url = "https://www.flamengo.com.br/jogos/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Faz a requisição HTTP
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Cria o objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra o elemento com a classe 'panel-games'
    panel_games = soup.find(class_='panel-games')

    # Extrai as informações necessárias
    month = panel_games.find('h2').get_text(strip=True)
    date_time = panel_games.find('div', class_='py-4').find('p').get_text(strip=True)
    tournament = panel_games.find('p', class_='destaque').get_text(strip=True)
    teams = panel_games.find('div', class_='game-teams').find_all('p', class_='d-none d-lg-inline-block')
    team1 = teams[0].get_text(strip=True)
    team2 = teams[1].get_text(strip=True)

    # Extrai os URLs das imagens dos emblemas
    emblem_urls = [
        urljoin(url, img['src']) for img in panel_games.find_all('img')
    ]

    # Baixa as imagens localmente
    local_emblem_paths = []
    for i, url in enumerate(emblem_urls):
        local_path = f"emblema_{i + 1}.png"
        urlretrieve(url, local_path)
        local_emblem_paths.append(local_path)

    # Cria o conteúdo do arquivo de texto
    content = f"${{color red}}\n${{font Arial Black:size=12}}{month}$font$color\n"
    content += f"{date_time}\n"
    content += f"${{color red}}{tournament}$color\n"
    content += f"${{alignc}}${{color white}}${{font Arial Black:size=15}}{team1} x {team2}${{font}}$color"
    
    # Adiciona as imagens ao conteúdo
    diretorio_atual = os.getcwd()
    for index, path in enumerate(local_emblem_paths):
        if index == 0:
            content += (f"${{image {diretorio_atual}/{path} -n -p 120,170 -s 22x25}}")
            # 50, 660
        if index == 1:
            content += (f"${{image {diretorio_atual}/{path} -n -p 305,170 -s 22x25}}")
            # 275,660

    # Salva o conteúdo no arquivo flamengo-jogos.txt
    with open("flamengo-jogos.txt", "w") as file:
        file.write(content)

    print("Arquivo flamengo-jogos.txt criado com sucesso.")
else:
    print("Erro na requisição HTTP. Código de status:", response.status_code)

