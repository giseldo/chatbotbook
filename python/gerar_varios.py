import os
import re

def dividir_markdown_por_secoes(arquivo_entrada, pasta_saida):
    # Certifique-se que a pasta de saída existe
    os.makedirs(pasta_saida, exist_ok=True)

    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Dividir usando cabeçalhos de primeiro nível
    secoes = re.split(r'(?m)^# (.+)', conteudo)

    # secoes[0] é o conteúdo antes da primeira seção (geralmente vazio)
    for i in range(1, len(secoes), 2):
        titulo = secoes[i].strip()
        corpo = secoes[i + 1].strip()

        # Criar nome de arquivo seguro
        nome_arquivo = re.sub(r'\W+', '_', titulo.lower()) + '.md'
        caminho_arquivo = os.path.join(pasta_saida, nome_arquivo)

        # Escrever conteúdo no novo arquivo
        with open(caminho_arquivo, 'w', encoding='utf-8') as f_out:
            f_out.write(f"# {titulo}\n\n{corpo}\n")

    print(f"Divisão concluída: {len(secoes)//2} arquivos criados em '{pasta_saida}'.")

# Exemplo de uso
dividir_markdown_por_secoes("main.md", "secoes_md")
