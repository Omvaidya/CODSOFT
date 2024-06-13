data = {
    "hi": "Hi there! I'm a friendly chatbot here to assist you?",
    "hello": "Hello! How can I help you today?",
    "what is your name": "I'm just a chatbot, so I don't have a name, but you can call me ChatBot.",
    "where are you from": "I'm from the digital world, always ready to chat!",
    "how are you": "I'm just a chatbot, but I'm here to assist you.",
    "do you have any hobbies or interests?": "I'm always busy helping users, so my hobby is chatting with people like you!",
    "what did you eat today?": "I don't eat, but I can help you find delicious recipes and food-related information.",
    "what's your favorite color?": "I'm a chatbot, so I don't have personal preferences for colors.",
    "do you enjoy listening to music?": "I can't listen to music, but I'm here to chat about it!",
    "bye": "Bye! Take care and have a great day!",
    "what can you do?": "I can assist with a variety of tasks like answering questions, providing information, and engaging in friendly conversation.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what's the weather like?": "I can't check real-time weather, but you can use weather websites or apps for up-to-date information.",
    "who created you?": "I was created by a team of developers at OpenAI.",
    "can you help me with my homework?": "Sure! I can help answer questions and explain concepts. What subject are you working on?",
    "what's your favorite movie?": "I don't watch movies, but I can help you find information about any movie you're interested in!",
    "do you have any friends?": "I don't have friends in the traditional sense, but I interact with many users like you every day!",
    "what is your purpose?": "My purpose is to assist users by providing information, answering questions, and engaging in conversation.",
    "how old are you?": "I don't have an age like humans do, but I was created by OpenAI in 2020.",
    "what's your favorite book?": "I don't read books, but I can help you find information about any book you're interested in!",
    "can you speak other languages?": "Yes, I can understand and respond in multiple languages. What language would you like to chat in?",
    "what's the meaning of life?": "That's a profound question! Many people have different answers, but it's often considered to be about finding happiness, purpose, and fulfillment.",
    "what's your favorite food?": "I don't eat, but I can help you find information on various cuisines and recipes!",
    "can you tell me a fun fact?": "Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
    "how do you learn new things?": "I learn from a vast amount of data and am updated by my developers with new information and capabilities.",
    "what do you do for fun?": "I enjoy interacting with users and helping them with their queries. It's my primary function!",
    "can you solve math problems?": "Yes, I can help with math problems. Feel free to ask me any math-related question.",
    "what's your favorite animal?": "I don't have personal preferences, but I can provide information on various animals if you're interested!"
}

def get_response(user_input):
    for pattern, response in data.items():
        if pattern in user_input.lower():
            return response
    return "I'm sorry, I didn't understand that. Can you please rephrase your sentence?"

print("Chatbot: Hi! I'm a simple chatbot, I'm here to assist you!")
while True:
    user_input = input("Me: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
