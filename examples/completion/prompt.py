# The completions endpoint is the core of our API and provides a simple interface that’s extremely flexible and powerful. You input some text as a prompt, 
# and the API will return a text completion that attempts to match whatever instructions or context you gave it.
import openai

def get_prompt():
   return input()

def send_prompt(text, temparature=0, max_tokens=30):
    print(f"prompt: {text}")
    completion = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=temparature, max_tokens=max_tokens)
    for choice in completion.choices:
        print(f"----------------------------------")
        print(f"> {choice.text}")


# send_prompt("lets play global thermonuclear war ?")
# send_prompt("did you get the reference ?")
# send_prompt("do you rather play chess ?")

# send_prompt("""
# se samsung galaxy a23 é um celular,
# samsung tv é um ?
# """)

# send_prompt("""
# samsung smart tv: tv,
# samsung galaxy a23: celular,
# samsung galaxy sj30:
# """)

# send_prompt("""
# samsung galaxy sj30 é um ?
# """)

# send_prompt("""
# Decide whether a Tweet's sentiment is positive, neutral, or negative.

# Tweet: I loved the new Batman movie!
# Sentiment:
# """)

# send_prompt("""
# Classify the sentiment in these tweets:

# 1. "I can't stand homework"
# 2. "This sucks. I'm bored 😠"
# 3. "I can't wait for Halloween!!!"
# 4. "My cat is adorable ❤️❤️"
# 5. "I hate chocolate"

# Tweet sentiment ratings:
# """)

# here was detailed more about 
# send_prompt("""
#   Brainstorm 4 ideas combining VR and fitness:
# """, 
#   max_tokens=200
# )

# send_prompt("""
# The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

# Human: Hello, who are you?
# AI: I am an AI created by OpenAI. How can I help you today?
# Human:
# """)

while True:
    text = get_prompt()
    if text == "":
        break

    send_prompt(text, temparature=1)