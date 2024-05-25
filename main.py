import requests

def singlePrompt(prompt):
    api_url = "https://reverse.mubi.tech/v1"
    model = "gpt-4"
    
    try:
        response = requests.post(f"{api_url}/chat/completions", json={
            "model": model,
            "messages": [{
                "role": "user",
                "content": prompt
            }]
        }, headers={
            "Content-Type": "application/json",
            "Origin": "https://gptcall.net/",
            "Referer": "https://gptcall.net/"
        })
        
        response.raise_for_status()
        data = response.json()
        bot_response = data["choices"][0]["message"]["content"]
        return bot_response
        
    except Exception as e:
        print("Error sending prompt to GPT:", e)
        return "Error: " + str(e)

def main():
    print("CLI-GPT")
    
    while True:
        user_input = input("> ").strip()
        
        if user_input.lower() == "exit":
            break
        
        bot_response = singlePrompt(user_input)
        print("GPT:", bot_response)

if __name__ == "__main__":
    main()
