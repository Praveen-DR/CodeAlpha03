pip install nltk   // install libraries

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

import nltk
from nltk.chat.util import Chat, reflections

# Define a set of pairs, which are patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created for demonstration purposes.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I assist you today?",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! It was nice talking to you.",]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand that.", "Could you please rephrase?",]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def chat():
    print("Hi! I am your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Take care.")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Start the chatbot
if __name__ == "__main__":
    chat()

