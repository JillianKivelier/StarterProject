# using a file , from USER INPUT, converted into a base64 string
from openai import AzureOpenAI
import base64
client = AzureOpenAI(
    api_key="16gB1rS6rjqJZ2POdeJuHxSOaTkZeLhI418RD70rb2R93kYVyDLkJQQJ99AKACHYHv6XJ3w3AAABACOGPq8l",   
    api_version="2024-02-15-preview",
    azure_endpoint="https://corp-enit-enterprise-openai.openai.azure.com/"
)
# function to encode image
def convert_to_base64(image_path):
    file_text = open(image_path, 'rb')
    file_read = file_text.read()
    return base64.b64encode(file_read).decode("utf-8")

image_path = input("Enter a file path\n")
image_base64 = convert_to_base64(image_path)
prompt = "Generate alternative text for the image"

chat_completion = client.chat.completions.create(
    messages=[
        
            {"role": "user","content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url":{
                        "url": f"data:image/jpeg;base64,{image_base64}"}
                }
            ]
            },
            {"role": "system", "content": "You are helping the visually impaired understand an image"}
    ],
    model="gpt-4.1-mini",
    max_tokens=250
)

print(chat_completion.choices[0].message.content)