# uses tkinter to create file upload interface instead of prompting for the file path itself 
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
#sets up the main application window
root = Tk()
root.title("Upload File")


def convert_to_base64(image_path):
    file_text = open(image_path, 'rb')
    # reads file as binary
    file_read = file_text.read()
    # converts binary data into base-64 encoded bytes 
    # then converts bytes into a string
    return base64.b64encode(file_read).decode("utf-8")

# common function to send request to API
def send_request(image_URL):
    prompt = "Generate alternative text for the image"
    # API Call to openai , chat_completion stores response 

    chat_completion = client.chat.completions.create(
    # converstaion passed to ai with prompt from user along with instructions to guide response (system)
         messages=[
        
            {"role": "user","content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": image_URL}}
            ]
                },
                {"role": "system", "content": "You are helping the visually impaired understand an image"}
            ],
        model="gpt-4.1-mini",
        # limits how long the response is 
     max_tokens=250
        )
    result = chat_completion.choices[0].message.content
    output_label.config(text=result)


def use_url():
    url = url_entry.get()
    if not url:
        output_label.config(text="Please enter a URL")
        return

    send_request(url)

def open_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    print(f"Selected file: {file_path}")
    image_base64 = convert_to_base64(file_path)
    data_url = f"data:image/jpeg;base64,{image_base64}"

    send_request(data_url)



ttk.Label(root, text="Image URL:").grid(row=0, column=0, padx=10, pady=5)
url_entry = ttk.Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=5)

# button that calls the command open file to select a file
button_open = ttk.Button(root, text = "Select file", command=open_file).grid(row=1, column=0, pady=10)
# button that calls command to use URL 
button_open2 = ttk.Button(root, text = "USE URL", command=use_url).grid(row=1, column=1, pady=10)


output_label = ttk.Label(root, text="", wraplength=400)
output_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)





root.mainloop()
