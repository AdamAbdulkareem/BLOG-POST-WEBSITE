import os
import openai
openai.api_key_path = "api-key.txt"
openai.api_key = os.getenv("api-key.txt")
synopsis = openai.Completion.create(
    model="text-davinci-003",
    prompt="I want to write a blog post about \"Will AI replace developers\". Give a list of 5 sections in a numbered bullet point format about this blog post.",
    max_tokens=3000,
    temperature=0.7
)
print(synopsis)