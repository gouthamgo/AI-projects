from transformers import pipeline

classifer = pipeline('sentiment-analysis')

res = classifer("I like learning about AI")

print(res)