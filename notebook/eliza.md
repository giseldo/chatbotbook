# Chatbot ELIZA em Python

A seguir, apresentamos uma implementação simplificada de um chatbot no estilo ELIZA usando Python. 
Esse código demonstra o uso de expressões regulares para identificar padrões (palavras-chave) na entrada do usuário e gerar respostas de acordo com regras de transformação definidas manualmente.

<a target="_blank" href="https://colab.research.google.com/github/giseldo/chatbotbook/blob/main/notebook/eliza.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

```Python
import re  
import random  

regras = [
    (re.compile(r'\b(hello|hi|hey)\b', re.IGNORECASE),
     ["Hello. How do you do. Please tell me your problem."]),

    (re.compile(r'\b(I am|I\'?m) (.+)', re.IGNORECASE),
     ["How long have you been {1}?",   
      "Why do you think you are {1}?"]),

    (re.compile(r'\bI need (.+)', re.IGNORECASE),
     ["Why do you need {1}?",
      "Would it really help you to get {1}?"]),

    (re.compile(r'\bI can\'?t (.+)', re.IGNORECASE),
     ["What makes you think you can't {1}?",
      "Have you tried {1}?"]),

    (re.compile(r'\bmy (mother|father|mom|dad)\b', re.IGNORECASE),
     ["Tell me more about your family.",
      "How do you feel about your parents?"]),

    (re.compile(r'\b(sorry)\b', re.IGNORECASE),
     ["Please don't apologize."]),

    (re.compile(r'\b(maybe|perhaps)\b', re.IGNORECASE),
     ["You don't seem certain."]),

    (re.compile(r'\bbecause\b', re.IGNORECASE),
     ["Is that the real reason?"]),

    (re.compile(r'\b(are you|do you) (.+)\?$', re.IGNORECASE),
     ["Why do you ask that?"]),

    (re.compile(r'\bcomputer\b', re.IGNORECASE),
     ["Do computers worry you?"]),
]

respostas_padrao = [
    "I see.",  
    "Please tell me more.",  
    "Can you elaborate on that?"  
]

def response(entrada_usuario):
    """Gera uma resposta estilo ELIZA para a entrada do usuário."""
    for padrao, respostas in regras:
        match = padrao.search(entrada_usuario)  
        if match:
            resposta = random.choice(respostas)
            if match.groups():
                resposta = resposta.format(*match.groups())
            return resposta
    return random.choice(respostas_padrao)


print(response("I am feeling sad."))
```

No código acima, definimos vários padrões regex que representam as “palavras-chave” de interesse (por exemplo, saudações, frases com “I am”, “I need”, referências à família, etc.). 
Quando a função response é chamada com uma string de entrada, ela itera por essas regras na ordem e usa padrao.search(entrada) para verificar se o padrão aparece na frase do usuário.

Ao encontrar um match, seleciona-se uma resposta. Observe que muitas respostas contêm placeholders como {1} – esses marcadores serão substituídos pelo conteúdo capturado na entrada do usuário. 
Por exemplo, se o usuário digitar "I am sad", a regex do padrão 2 capturará o grupo ("I am", "sad"), e a resposta escolhida "Why do you think you are 1?" será formatada como "Why do you think you are sad?". 
Caso nenhuma regra específica seja acionada, o chatbot retorna aleatoriamente uma das respostas genéricas em respostas_padrao (como "I see.").

Demonstração: Suponha a seguinte interação usando o chatbot implementado

```Python
print("User: Hello.")
print("Bot: " + response("Hello."))

print("User: I am feeling sad.")
print("Bot: " + response("I am feeling sad."))

print("Maybe I was not good enough.")
print("Bot: " + response("Maybe I was not good enough."))

print("My mother tried to help.")
print("Bot: " + response("My mother tried to help."))
```

```
Usuário: Hello
Bot: Hello. How do you do. Please tell me your problem.

Usuário: I am feeling sad
Bot: Why do you think you are feeling sad?

Usuário: Because I lost my job
Bot: Is that the real reason?

Usuário: Maybe I was not good enough.
Bot: You don't seem certain.

Usuário: My mother tried to help.
Bot: Tell me more about your family.
```

Podemos ver que o bot respondeu “Hello...” à saudação inicial (regra 1), depois detectou “I am sad” e devolveu uma pergunta usando sad (regra 2), seguiu questionando o “Because...” (regra 8) e reagiu a “Maybe...” (regra 7), e assim por diante. Cada resposta foi escolhida conforme as regras e conteúdo da frase do usuário, semelhante ao comportamento do ELIZA original.
