from openai import OpenAI

client = OpenAI(
    api_key="PASTE_YOUR_KEY_HERE"

)
completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    message=[
        {"role": "system", "content": "you are a virtual assistant named jarvis skilled in general tasks like alexa  and Google cloud "}
,        
        {"role" : "user" , "content":  "what is coding"         }
    ]
)
print(completion.choices[0].message)