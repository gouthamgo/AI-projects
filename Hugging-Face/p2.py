from transformers import pipeline

# Initialize a text generation pipeline
generator = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta")

# Input prompt for text generation
prompt = "Hello, I'm a language model"

# Generate new text based on the prompt
res = generator(prompt, max_length=50, num_return_sequences=3)

# Print the generated text
for i, output in enumerate(res):
    print(f"Generated Text {i+1}:")
    print(output['generated_text'])
    print("\n")


from transformers import pipeline

# Create pipeline
my_pipeline = pipeline("task-name", model="model-name")  # model is optional

# Use pipeline
result = my_pipeline("Your input text here")