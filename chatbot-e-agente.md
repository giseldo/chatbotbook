# Chatbot e Agente

Define-se chatbot como um programa computacional projetado para interagir com usuários por meio de linguagem natural. Por outro lado, o conceito de agente possui uma definição mais ampla: trata-se de uma entidade computacional que percebe seu ambiente por meio de sensores e atua sobre esse ambiente por meio de atuadores \[7]. A Figura 2 ilustra uma arquitetura conceitual de alto nível para um agente.

Figura 2: Arquitetura conceitual de um agente.

<figure><img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1743720242023/3df617ac-c48c-496e-8dc9-89eaece3f5c9.png" alt=""><figcaption></figcaption></figure>

**Fonte: Diretamente retirado de \[7]**

Nesse contexto, um chatbot (Figura 3) pode ser considerado uma instanciação específica de um agente, cujo propósito primário é a interação conversacional em linguagem natural.

**Figura 2 -** Representação esquemática de um chatbot.

<figure><img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1743895555574/e4125367-da81-4bef-8658-6b97aa8d4b3d.png" alt=""><figcaption></figcaption></figure>

**Fonte: Giseldo Neo (2025)**

Com o advento de modelos de linguagem avançados, como os baseados na arquitetura Generative Pre-trained Transformer (GPT), observou-se uma re-contextualização do termo “agente” no domínio dos sistemas conversacionais. Nessa acepção mais recente, um sistema focado predominantemente na geração de texto conversacional tende a ser denominado “chatbot”. Em contraste, o termo “agente” é frequentemente reservado para sistemas que, além da capacidade conversacional, integram e utilizam ferramentas externas (por exemplo, acesso à internet, execução de código, interação com APIs) para realizar tarefas complexas e interagir proativamente com o ambiente digital. Um sistema capaz de realizar uma compra online, processar um pagamento e confirmar um endereço de entrega por meio do navegador do usuário seria, portanto, classificado como um agente, diferentemente de chatbots mais simples como ELIZA, cujo foco era estritamente o diálogo.

Diversos frameworks têm sido desenvolvidos para facilitar a criação desses agentes complexos, como CrewAI e bibliotecas associadas a plataformas como Hugging Face (e.g., Transformers Agents), que fornecem abstrações e ferramentas em Python para orquestrar múltiplos componentes e o uso de ferramentas externas.

A popularidade dos chatbots tem crescido significativamente em diversos domínios de aplicação \[3, 2, 8]. Essa tendência é corroborada pelo aumento do interesse de busca pelo termo “chatbots”, conforme análise de dados do Google Trends no período entre 2020 e 2025 (Figura 4). Nesta figura, os valores representam o interesse relativo de busca ao longo do tempo, onde 100 indica o pico de popularidade no período analisado e 0 (ou a ausência de dados) indica interesse mínimo ou dados insuficientes.

**Figura 4: Evolução do interesse de busca pelo termo “chatbot” (Google Trends, 2020-2025).**

<figure><img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1743895546931/b8014353-538d-4ae1-9fa0-5bb3a442aed9.png" alt=""><figcaption></figcaption></figure>

**Fonte: Google Trends acesso em 05/04/2025**

### Origem do termo chatbot/chatterbot

Embora ELIZA \[9] seja frequentemente considerado um dos primeiros exem- plos de software conversacional, o termo “chatbot” ainda não era utilizado na época de sua criação. O termo “chatterbot”, sinônimo de “chatbot”, foi popularizado por Michael Mauldin em 1994, ao descrever seu programa JULIA \[5]. Subsequentemente, o termo também foi registrado em publicações acadêmicas, como nos anais da Virtual Worlds and Simulation Conference de 1998 \[1].

### Gerenciamento do Diálogo e Fluxo Conversacional

A interação textual mediada por chatbots não se constitui em uma mera justaposição aleatória de turnos de conversação ou pares isolados de estímulo resposta. Pelo contrário, espera-se que a conversação exiba coerência e mantenha relações lógicas e semânticas entre os turnos consecutivos. O estudo da estrutura e organização da conversa humana é abordado por disciplinas como a Análise da Conversação.

No contexto da linguística textual e análise do discurso em língua portuguesa, os trabalhos de Marcuschi \[4] são relevantes ao investigar a organização da conversação. Marcuschi analisou a estrutura conversacional em termos de unidades coesas, como o “tópico conversacional”, que agrupa turnos relacionados a um mesmo assunto ou propósito interacional.

Conceitos oriundos da Análise da Conversação, como a gestão de tópicos, têm sido aplicados no desenvolvimento de chatbots para aprimorar sua capacidade de manter diálogos coerentes e contextualmente relevantes com usuários humanos \[6]. Na prática de desenvolvimento de sistemas conversacionais, a estrutura lógica e sequencial da interação é frequentemente modelada e referida como “fluxo de conversação” ou “fluxo de diálogo”. Contudo, é importante ressaltar que a implementação explícita de modelos sofisticados de gerenciamento de diálogo, inspirados na Análise da Conversação, não é uma característica universal de todos os chatbots, variando conforme a complexidade e o propósito do sistema. Um exemplo esquemático de um fluxo conversacional é apresentado na Figura 5.

**Figura 5: Exemplo esquemático de um fluxo conversacional em um chatbot.**

<figure><img src="https://github.com/giseldo/chatbot_BTA_BPMN_to_AIML/raw/master/images/first.png" alt=""><figcaption></figcaption></figure>
