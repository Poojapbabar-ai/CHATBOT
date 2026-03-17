
import os
from dotenv import load_dotenv
import groq

load_dotenv()

# Read your prompt file

#------------- as i used emoji's we needed to change the encoding to utf-8 -------------
# with open("prompt.txt", "r") as f:
#     my_prompt = f.read()

with open("prompt.txt", "r", encoding="utf-8") as f:
    my_prompt = f.read()

client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

# user_question = "what are the thyroxine 75 mcg price"
user_question = "what are the thyroxine 75 mcg price"

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    max_tokens=1024,
    messages=[
    {"role": "system", "content": my_prompt},   
    {"role": "user", "content": user_question}
]
)

print("Bot:", response.choices[0].message.content)
