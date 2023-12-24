import openai
from PIL import Image


img = Image.open("./input-images/gatuno.jpeg")
width, height = img.size

allowed_sizes = ['256x256', '512x512', '1024x1024']

target_width, target_height = allowed_sizes[2].split("x")

left = 0 
right = int(target_width)
bottom = height
top = height - int(target_height)

img_croped = img.crop((left, top, right, bottom))
img_converted = img_croped.convert('RGBA')
img_converted.save("./input-images/gatuno.png", format='PNG')

response = openai.Image.create_variation(
  image=open("./input-images/gatuno.png", "rb"),
  n=3,
  size=f"1024x1024"
)


for data in response['data']:
    print(data['url'])
