import os
import openai
import time

with open('key.txt', 'r') as key:
    key = key.read()

openai.api_key = key

def query(prompt,model="text-davinci-002",max_tokens=16,temperature=1):
    print('<START>')
    x = time.time()
    completion = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    
    print(time.time()-x)
    print('<END>')
    print(completion)
    
    return completion ["choices"] [0] ["text"]