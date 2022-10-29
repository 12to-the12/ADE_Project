# this file contains the method used to interact with the GPT-3 API

import os
import openai
import time

# this opens is the API key, which is stored locally
with open('C:/Users/logan/key.txt', 'r') as text:
    key: str = text.read()

openai.api_key: str = key



def query(prompt,model="text-davinci-002",max_tokens=16,temperature=1) -> str:
    print(f"the key is {key}")
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


    if __name__ == "__main__":
        pass