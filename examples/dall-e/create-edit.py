import openai


response = openai.Image.create_edit(
  image=open("./input-images/gatuno.png", "rb"),
#   mask=open("mask.png", "rb"),
  prompt="a cat with a hat",
  n=5,
  size="1024x1024"
)
for data in response['data']:
    print(data['url'])
