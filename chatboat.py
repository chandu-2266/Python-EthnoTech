def show_welcome():
    print("Bot: Hello! I am your AI ChatBot.")
def get_response(user_input):
    responses = {
        "hi": "Hello!",
        "how are you": "I am fine.",
        "what is python": "Python is a programming language.",
        "who are you": "I am an AI ChatBot."
    }
    return responses.get(user_input.lower(),
                         "Sorry, I don't understand that question.")
def start_chat():
    show_welcome()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day.")
            break
        print("Bot:", get_response(user_input))

start_chat()
