include .env


dalle_gen:
	python3 examples/dall-e/create-image.py

list:
	python3 examples/completion/list.py

prompt:
	python3 examplest/completion/prompt.py

embedding:
	python3 examples/embedings/embedding.py

finetune_prepare:
	head -n 1000 data/test.csv > data/sample_1000.csv
	openai tools fine_tunes.prepare_data -f data/sample_1000.csv

finetune_send:
	openai api fine_tunes.create -t data/sample_1000_prepared.jsonl -m curie
