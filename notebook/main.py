from langchain.llms import HuggingFaceHub
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 1. Baixar e carregar um modelo local
model_name = "facebook/opt-1.3b"  # Modelo relativamente pequeno que pode rodar em CPUs/máquinas modestas

# Carrega o tokenizador e o modelo
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Cria um pipeline de texto
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=100,
    device="cpu"  # Use "cuda" se tiver GPU
)

# 2. Cria um LLM do LangChain usando o pipeline
llm = HuggingFacePipeline(pipeline=pipe)

# 3. Cria um template de prompt
template = """Pergunta: {pergunta}

Resposta: Vamos pensar passo a passo."""
prompt = PromptTemplate(template=template, input_variables=["pergunta"])

# 4. Cria uma cadeia (chain) para interação
llm_chain = LLMChain(prompt=prompt, llm=llm)

# 5. Interage com o modelo
pergunta = "Explique como funciona a fotossíntese de forma simples."
resposta = llm_chain.run(pergunta)
print(resposta)