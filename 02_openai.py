from openai import OpenAI
 
client = OpenAI(
  api_key="API_key",
)

command = '''
[21:05, 12/6/2024] Arjun: bro suggest some music for coding
[21:06, 12/6/2024] Vivek: wait I got something good
[21:06, 12/6/2024] Vivek: https://www.youtube.com/watch?v=2Vv-BfVoq4g
[21:06, 12/6/2024] Arjun: nicee
[21:07, 12/6/2024] Arjun: but this feels more like chill music
[21:07, 12/6/2024] Arjun: I need something more energetic
[21:07, 12/6/2024] Vivek: alright hold on
[21:07, 12/6/2024] Vivek: sending another one
[21:08, 12/6/2024] Vivek: https://www.youtube.com/watch?v=fLexgOxsZu0
[21:08, 12/6/2024] Arjun: ohh this one is fire 🔥
[21:08, 12/6/2024] Arjun: perfect coding vibe
[21:09, 12/6/2024] Vivek: told you 😎
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named arjun who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Arjun"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)