# using URL from USER INPUT
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="16gB1rS6rjqJZ2POdeJuHxSOaTkZeLhI418RD70rb2R93kYVyDLkJQQJ99AKACHYHv6XJ3w3AAABACOGPq8l",   
    api_version="2024-02-15-preview",
    azure_endpoint="https://corp-enit-enterprise-openai.openai.azure.com/"
)

image_path = input("Enter an image URL\n")
prompt = "Generate alternative text for the image"

chat_completion = client.chat.completions.create(
    messages=[
        
            {"role": "user","content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": image_path}}
            ]
            },
            {"role": "system", "content": "You are helping the visually impaired understand an image"}
    ],
    model="gpt-4.1-mini",
    max_tokens=250
)

print(chat_completion.choices[0].message.content)