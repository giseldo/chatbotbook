import os
import re
import subprocess
import shutil

subprocess.run("pandoc -s main.tex -o script/main.md", shell=True, check=True)

arquivo_entrada = "script/main.md"
pasta_saida = "script/secoes_md"

os.makedirs(pasta_saida, exist_ok=True)

with open(arquivo_entrada, 'r', encoding='utf-8') as f:
    conteudo = f.read()

secoes = re.split(r'(?m)^# (.+)', conteudo)
contador = 0

for i in range(1, len(secoes), 2):
    contador += 1
    titulo = secoes[i].strip()
    corpo = secoes[i + 1].strip()

    nome_arquivo = re.sub(r'\W+', '_', titulo.lower()) + '.md'
    caminho_arquivo = os.path.join(pasta_saida, str(contador) + "_" + nome_arquivo)

    with open(caminho_arquivo, 'w', encoding='utf-8') as f_out:
        f_out.write(f"# {titulo}\n\n{corpo}\n")

print(f"Divisão concluída: {len(secoes)//2} arquivos criados em '{pasta_saida}'.")

pasta_origem = pasta_saida
pasta_destino = "..\\cursos\\docs\\chatbotbook"

# os.makedirs(pasta_destino, exist_ok=True)

for arquivo in os.listdir(pasta_origem):
    if arquivo.endswith(".md"):
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        shutil.copy(caminho_origem, caminho_destino)

print(f"Arquivos .md movidos de '{pasta_origem}' para '{pasta_destino}'.")
