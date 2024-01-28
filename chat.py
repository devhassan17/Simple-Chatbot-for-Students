import google.generativeai as genai

genai.configure(api_key='AIzaSyCyHZ07xZqI5e1tA6_KV2sIfWDNm7_a0oM')

model = genai.GenerativeModel('gemini-pro')



while True:
    user_prompt = input("Enter Message: ")
    chat = model.start_chat(history=[])

    response = chat.send_message(user_prompt)

    print(response.text)