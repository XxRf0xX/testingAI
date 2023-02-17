import openai

'''Pon tu APIKEY aqui'''
openai.api_key=''

while True:
    
    propmt = input("\nIndroduce una pregunta: ")
    if propmt == 'exit':
        break

    complection = openai.Completion.create(
    engine = 'text-davinci-003',
    prompt = propmt,
    max_tokens = 2000
)

    print(complection.choices[0].text)
