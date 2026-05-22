from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import base64

from openai import AzureOpenAI

# client set up, setting neccessary credentials for upcoming API call
client = AzureOpenAI(
    api_key="16gB1rS6rjqJZ2POdeJuHxSOaTkZeLhI418RD70rb2R93kYVyDLkJQQJ99AKACHYHv6XJ3w3AAABACOGPq8l",   
    api_version="2024-02-15-preview",
    azure_endpoint="https://corp-enit-enterprise-openai.openai.azure.com/"
)
def open_file():
    # Opens a file dialog and returns the selected file path
    file_path1 = filedialog.askopenfilename()
    if file_path1:
        file = f"{file_path1}"
        return file

def convert_to_base64(image_path):
    file_text = open(image_path, 'rb')
    file_read = file_text.read()
    return base64.b64encode(file_read).decode("utf-8")

loop = 1
while loop == 1:
    root = Tk()
    root.title("Upload File")
    

    command = open_file()
    button_open = ttk.Button(root, text = "Select file", command=command)
    button_open.pack(pady=10)

    print(f"Selected file: {command}")

    image_base64 = convert_to_base64(command)
    prompt = "Generate alternative text for the image"

    # API Call to openai , chat_completion stores response 

    chat_completion = client.chat.completions.create(
    # converstaion passed to ai with prompt from user along with instructions to guide response (system)
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
    # limits how long the response is 
    max_tokens=250
)

    print(chat_completion.choices[0].message.content)


    root.mainloop()
