import openai
# put your key here
cliente = openai.OpenAI(api_key = "")

def conversa_chatgpt(mensagem):
    try:
        resposta = cliente.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": mensagem}
                ]

        )
        return resposta.choices[0].message.content
    except Exception as e:
        return f"Erro: {e}"

while True:
    mensagem_usuario = input("Voce: ")
    if mensagem_usuario.lower() in ["sair", "tchau", ]:
        break
    resposta_bot = conversa_chatgpt(mensagem_usuario)
    print(f"chatbot",{resposta_bot})
