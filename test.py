import openai
from dotenv import load_dotenv
import os
load_dotenv('.env')
# openai.api_key = os.environ['OPENAI_API_KEY']
openai.api_type = "azure"
openai.api_base = os.environ['OPENAI_API_BASE']
openai.api_version = os.environ['OPENAI_API_VERSION']
openai.api_key = os.environ['OPENAI_API_KEY']

print(openai.Completion.create(prompt="who are you?",model='gpt-4-32k',engine="gpt_4_32k"))

# def get_completion(prompt, model="gpt-4-32k"):
#     messages = [{"role": "user", "content": prompt}]
#
#     response = openai.ChatCompletion.create(
#
#         model=model,
#
#         engine="gpt_4_32k",
#
#         messages=messages,
#
#         temperature=0,
#
#         max_tokens=4000,
#
#         top_p=1,
#
#         frequency_penalty=0,
#
#         presence_penalty=0,
#
#         stop=None
#
#     )
#
#     return response
# # , response.usage['total_tokens'])

# output = openai.Completion.create(prompt="Who are you?",model="gpt-3.5-turbo-instruct",max_tokens=100)

# output =get_completion(prompt="Who are your?")
# print(output.choices[0]['message']['content'])
print(output)