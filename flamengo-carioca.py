import requests
from bs4 import BeautifulSoup

# URL do site do Flamengo para o Campeonato Carioca 2024
url = "https://www.flamengo.com.br/campeonatos/campeonato-carioca-2024"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Faz a requisição HTTP
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra a tabela de classificação
    tabela_classificacao = soup.find('table', class_='table-responsive')

    # Inicializa o conteúdo do arquivo com cabeçalhos de tabela do Conky
    conteudo = "${font Monospace:size=6}${color red}\n${alignc}"
    conteudo += " | %-3s | %-20s | %-5s | %-3s | %-3s | %-3s | %-3s | %-3s | %-3s | %-3s | %-3s |" % (
        "Pos", "Time", "Pts", "J", "V", "E", "D", "GP", "GC", "SG", "%"
    )
    conteudo += "${color}\n"

    # Encontra as linhas da tabela
    linhas = tabela_classificacao.find_all('tr')

    # Itera sobre as linhas e extrai as informações
    for linha in linhas[1:]:  # Ignora a primeira linha (cabeçalho)
        colunas = linha.find_all(['td', 'th'])

        # Extrai os dados da linha
        posicao = colunas[0].text.strip()
        time = colunas[1].find('span', class_='semi-bold').text.strip()
        pontos = colunas[2].text.strip()
        jogos = colunas[3].text.strip()
        vitorias = colunas[4].text.strip()
        empates = colunas[5].text.strip()
        derrotas = colunas[6].text.strip()
        gols_pro = colunas[7].text.strip()
        gols_contra = colunas[8].text.strip()
        saldo_gols = colunas[9].text.strip()
        percentual = colunas[10].text.strip()

        # Adiciona os dados ao conteúdo do arquivo
        conteudo += "${color white}  | %-3s | %-20s | %-5s | %-3s | %-3s | %-3s | %-3s | %-3s | %-3s | %-3s | %-3s |$color" % (
            posicao, time, pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo_gols, percentual
        )
        conteudo += "\n"

    # Salva o conteúdo no arquivo flamengo-carioca.txt
    with open("flamengo-carioca.txt", "w") as file:
        file.write(conteudo)

    print("Arquivo flamengo-carioca.txt criado com sucesso.")
else:
    print("Erro na requisição HTTP. Código de status:", response.status_code)
