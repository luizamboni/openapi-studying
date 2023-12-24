import openai

animals = ["cat", "dog", "duck"]
styles = ["manga style", "3d render", "impressionist"]
sentiments = ["angry", "happy", "confused" ]
number_of_alternatives = 1

for animal in animals:
    for style in styles:
        for sentiment in sentiments:

            prompt = f"{style} {sentiment} cute fat orange pokemon {animal}"

            response = openai.Image.create(
                prompt=prompt,
                n=number_of_alternatives,
                size="1024x1024"
            )

            image_url = response['data'][0]['url']
            print(prompt, image_url)