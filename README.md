# Movie Info Chatbot

Este projeto implementa um agente de chat interativo em Python, usando LangChain e a OpenAI API, especializado em filmes.

## Pré-requisitos

- Python 3.10 ou superior.  
- Uma chave de API válida da OpenAI (definida na variável de ambiente `OPENAI_API_KEY`).

## Instalação

1. Clone este repositório(tópico simulado, pois enviei em arquivo):  
   ```
   git clone https://github.com/JabuS2/TesteTecnico
   cd TesteTecnico
   ```
2. Instale as dependências:  
   ```
   pip install -r requirements.txt
   ```

## Uso

Execute o script principal:
```
python movie_info.py
```

Em seguida, digite títulos de filmes e converse com o agente. Para encerrar, digite `sair`.

## Estrutura dos arquivos

- `movie_info.py`: script principal com loop de chat e integração ao OpenAI via LangChain.  
- `requirements.txt`: lista de dependências.  
- `README.md`: este arquivo de documentação.
- `.env`: este arquivo contem a chave de api

## Customizações

- Ajuste `temperature` ou `model_name` em `movie_info.py` para alterar a criatividade e o modelo utilizado.  
- Edite o `SystemMessage` para afinar o estilo de resposta do agente.

## Licença

MIT © Guilherme dos Santos
