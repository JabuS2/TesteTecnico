import os
import json
import logging
from openai import OpenAIError
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicialização do modelo ChatOpenAI via langchain-community
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Mensagem de sistema que define o comportamento do agente
system_message = SystemMessage(content=(
    "Você é um assistente especializado em filmes. "
    "Lembre-se de conversar de forma natural e amigável, podendo responder perguntas, explorar curiosidades e discutir sobre o filme."
))

# Lista que acumula o histórico de mensagens
messages = [system_message]


def chat():
    """
    Entra em um lop de chat interativo com o usuário.
    """
    print("Iniciando chat sobre filmes. Digite 'sair' para encerrar.")
    while True:
        try:
            user_input = input("Você: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("sair", "exit", "quit"):
                print("Sessão encerrada. Até a próxima!")
                break

            # Adiciona mensagem do usuário ao histórico
            messages.append(HumanMessage(content=user_input))

            # Chamada ao modelo
            try:
                response = llm(
                    messages=messages
                )
            except OpenAIError as api_err:
                logger.error(f"[OpenAI API Error] {api_err}")
                print("Erro na API do OpenAI. Tente novamente mais tarde.")
                continue

            # Extrai o texto da resposta
            ai_content = response.content if hasattr(response, 'content') else None
            if not ai_content:
                print("Nenhuma resposta gerada.")
                continue

            # Adiciona resposta do AI ao histórico e exibe
            messages.append(AIMessage(content=ai_content))
            print(f"FilmeBot: {ai_content}")

        except KeyboardInterrupt:
            print("\nSessão interrompida pelo usuário.")
            break
        except Exception as e:
            logger.error(f"[Erro Genérico] {e}")
            print("Ocorreu um erro inesperado. Tente novamente.")


if __name__ == "__main__":
    chat()
