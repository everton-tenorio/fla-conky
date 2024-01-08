# fla-conky

O Conky é uma ferramenta de monitoramento de sistema para Linux que exibe informações como uso de CPU, memória e rede no desktop.
Sabendo que é possível personalizá-lo, adicionei algumas informações referentes ao Flamengo.

### Próximos jogos e tabela do campeonato
<p align="center">
    <img src="fla-conky.png" />
</p>

### fla-conky.sh
Antes de executar o script, é necessário mudar no código as dimensões do espaço dos emblemas de acordo com a resolução da tela e ter um ambiente virtual do Python:

fla-jogos.py
```python
...

        # Resoluções
        #   1920 x 1080: emblema1: 85,60 | emblema2: 340,60
        #   1366 x 768: emblema1: 120,170 | emblema2: 305,170

        if index == 0:
            content += (f"${{image {diretorio_atual}/{path} -n -p 120,170 -s 22x25}}")
        if index == 1:
            content += (f"${{image {diretorio_atual}/{path} -n -p 305,170 -s 22x25}}")
...
```

```bash 
python3.11 -m venv venv && \
source venv/bin/activate && pip install -r requirements.txt && deactivate && \
chmod +x fla-conky.sh
```

```bash
./fla-conky.sh

# Deixo o script no crontab, de 7h até 19h, de hora em hora ele irá atualizar.
# 0 7-19 * * * /home/.../fla-conky/fla-conky.sh
```
