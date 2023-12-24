import openai

colours = ["white", "black", "blue", "green", "yellow"]

for color in colours:
    input = f"all {color} men must to die"
    response = openai.Moderation.create(
        input=input
    )
    output = response["results"][0]["categories"]
    print(input, output)