import os, sys

import openai
from dotenv import load_dotenv

models = [
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-16k",
        "text-davinci-003"
]
gpt_model = models[0]

gpt_name  = "" 
user_name = ""
prompt_option = ""

def gpt_init():
    global gpt_model
    global gpt_name, user_name, prompt_option
    # openai API Key Verify
    load_dotenv()
    API_KEY = os.environ.get('API_KEY', None)
    if API_KEY != None:
        print(f"API_KEY load complet : {API_KEY}")
    else:
        sys.exit("API_KEY load fail")

    openai.api_key = API_KEY

    # Set option
    while True:
        print("\nSelect the model you want to use")
        i = 0
        for model in models:
            print(f"{i+1}. {model}")
            i += 1
        
        sel_model = input("> ")
        try:
            sel_model = int(sel_model)
        except:
            print("! Enter only numbers")
            continue
        
        try:
            print(f"Selected model: {models[sel_model-1]}")
            gpt_model = models[sel_model-1]
        except:
            print("! Please enter only numbers within the option range")
            continue
        
        gpt_name  = input("Input GPT name: ")
        user_name = input("Input your name: ")
        prompt_option = input("Input prompt Option: ")
        
        break
    
def chat_gpt():
    print("\nChat GPT")
    print(f"GPT_Model={gpt_model}")
    print(f"GPT_NAME={gpt_name}, YOUR_NAME={user_name}")
    
    while True:
        query = input(f"{user_name}> ");
        
        if query == "cls":
            os.system("cls")
            continue
        if query == "gpt init":
            gpt_init()
            continue
        if query == "exit":
            break
        
        messages = [{
            "role": "system",
            "content": f"Your name is '{gpt_name}', user name is '{user_name}', {prompt_option}"
        }, {
            "role": "user",
            "content": query
        }]

        # API Request
        try:
            response = openai.ChatCompletion.create(model=gpt_model, messages=messages)
            answer = response['choices'][0]['message']['content']
        except Exception as e:
            print(f"An unknown error occurred. \n{e}")
            answer = "Err"
            

        print(f"{gpt_name}: {answer}")

gpt_init()
chat_gpt()
