import wikipedia
wikipedia.set_lang("pt")

result = wikipedia.summary("chatgpt")
print(result)