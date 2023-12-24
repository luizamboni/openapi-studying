import openai
import os

FINE_TUNED_MODEL = os.getenv("FINE_TUNED_MODEL")

prompts = [
    "Eram os deuses astronautas -> ",
    "Bateria noteboot 127/220V -> ",
    "celular Stephen King , quarta edição -> ",
    "cama box solteiro -> ",
    "A evolução dos Sistemas Celulares: A evolução dos Sistemas Celulares Vol. 1 -> ",
    "A evolução dos Sistemas Celulares: A evolução dos Sistemas Celulares -> ",
    "A evolução dos Sistemas Celulares Vol. 1 -> ",
    "Eram os deuses astronautas -> ",
    "the advendures of zamboni: second edition ->",
]

for prompt in prompts:
    res = openai.Completion.create(
        model=FINE_TUNED_MODEL,
        prompt=prompt,
        max_tokens=1,
        logprobs=5,
    )

    print(
        prompt, res.get("choices", [])[0].get("text")
    )