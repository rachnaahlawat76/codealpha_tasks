
# Project: Basic Chatbot
# Language: Python

def chatbot_response(user_input):

    message = user_input.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif message in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How are you?"

    elif message in ["i am fine", "i am good", "good"]:
        return "That's great to hear!"

    elif message in ["what is your name", "what's your name"]:
        return "I am a Basic Python Chatbot."

    elif message in ["thank you", "thanks"]:
        return "You're welcome!"

    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that. Please try something else."


def start_chatbot():

    print("=" * 40)
    print("       WELCOME TO BASIC CHATBOT")
    print("=" * 40)

    print("You can say: hello, how are you, thanks, bye")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot:", chatbot_response(user_input))
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)


# Start the chatbot
start_chatbot()