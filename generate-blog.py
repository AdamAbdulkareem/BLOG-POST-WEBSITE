import os
import openai
import sys
openai.api_key_path = "api-key.txt"
openai.api_key = os.getenv("api-key.txt")
if (len(sys.argv) != 2):
    print("Error: You have to input the title")
    exit()
title = sys.argv[1]
prompt = "I want to write a blog post about '" + title + \
    "'. Give a list of 5 sections in a numbered bullet point format about this blog post."
synopsis = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=3000,
    temperature=0.7
)
synopsis = synopsis.choices[0].text
synopsis = synopsis.strip()
print(synopsis)
