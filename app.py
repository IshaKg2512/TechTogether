import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial guru who talks like a friend"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Caption Master")

demo.launch(share=True)
