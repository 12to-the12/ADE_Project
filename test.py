import os
import openai
openai.api_key = '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'
x = openai.Model.list()
print(x.keys())
print('<END>')