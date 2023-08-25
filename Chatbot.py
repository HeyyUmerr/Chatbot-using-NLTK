import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "How can I help you today?"]
    ],
    [
        r"how are you",
        ["I'm good, thanks for asking.", "I'm doing well.", "All good! How about you?"]
    ],
    [
        r"(.*) your name?",
        ["I am a chatbot.", "My name is ChatGPT."]
    ],
    [
        r"what can you do|what are your capabilities|how can you help",
        ["I can provide information, answer questions, and have basic conversations with you."]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye!", "Have a great day!"]
    ],
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Start the chat
print("Chatbot: Hello! I'm your chatbot. Type 'quit' to exit.")
chatbot.converse()
