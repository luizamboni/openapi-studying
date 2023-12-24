import openai

# list models
models = openai.Model.list()

# print the first model's id
for model in models.data:
    print(model)

# create a completion
completion = openai.Completion.create(model="ada", prompt="can yout teach me english ?")

# print the completion
for choice in completion.choices:
    print(f"> {choice.text}")

