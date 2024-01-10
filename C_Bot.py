from openai import OpenAI     #importing OpenAI library from openai by "pip install openai"

OpenAI.api_key='Mention your API Key' #get Unique API Key from browser 

message=[{"role":"system","content":"Welcome programmer"}]
while True:
  resp=input("User prompt: ")
  if resp:
    message.append(
        {"role":"user","content":resp},
    )
    chat=OpenAI.ChatCompletion.create(
        model="gpt-3.5-turbo",message=message,temperature=0.5     #you can modify the version of gpt if required
    )
  respond=chat.choices[0].message.content   #generating the response
  print(f"C_Bot: {respond}")                
  message.append({"role":"assistant","content":respond})   #updating the conversation
