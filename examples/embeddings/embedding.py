import openai, numpy as np


groups = [
    "Ar-Condicionado Split Piso / Teto Carrier X-Power 36000 BTUs Frio Inverter 42ZQVB36C5 38CCVB36515MC",
    "Ar-Condicionado Split Cassete Carrier 36000 BTUs Frio Inverter 40KVCB36C5 / 38CCVA36515MC"
]

products = [
    "Ar Condicionado Split Cassete Inverter Carrier Frio 36000 Btus 220V Monofásico 40Kvqb36c5", 
    "Ar Split Cassete Inverter Carrier Frio 36000 Btus 220v/1f 38CCVB36515MC",
    "Ar Cond Split Teto Inverter 36000 Carrier Xpower Frio 220v 42ZQVC36C5",
]

resp = openai.Embedding.create(
    input=groups + products,
    engine="text-similarity-davinci-001")

embeddings = [ x['embedding'] for x in resp['data'] ]

for group in enumerate(embeddings[0:2]):
    for product in embeddings[2:5]:

        similarity_score = np.dot(group, product)

        print(similarity_score)