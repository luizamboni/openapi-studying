import openai

system_message = "You are a helpful assistant."
system_message = "You are a stupid assistant."

resp = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

for choice in resp["choices"]:
    print(choice["message"]["content"])

for name, value in resp["usage"].items():
    print(name, value)