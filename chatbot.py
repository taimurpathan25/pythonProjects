
import datetime

user_name = input("Enter your name: ")
currentHour = datetime.datetime.now().hour

# Greeting based on current time
if 5 <= currentHour < 12:
    print("Good Morning", user_name)
elif 12 <= currentHour < 17:
    print("Good Afternoon", user_name)
elif 17 <= currentHour < 21:
    print("Good Evening", user_name)
else:
    print("Good Night!", user_name)

print("Welcome to Personal Chatbot!")

user_responses = {
    "hello": "Hi! Welcome. How can I help?",
    "who are you": "I am a Smart Chatbot.",
    "how are you": "I'm doing great, thanks for asking!",
    "can you help me": "Absolutely! Tell me what you need help with.",
    "are you a human": "I'm an AI chatbot designed to assist you.",
    "i don't understand": "No problem! Let me explain it in a simpler way.",
    "thank you so much": "You're very welcome! I'm happy I could help."
}

def getUserResponse(userAskQuestion):
    userAskQuestion = userAskQuestion.lower()

    for key, response in user_responses.items():
        if key in userAskQuestion:
            return response

    return "Sorry, I don't know the answer to that question yet!"

while True:
    userInput = input("Please ask your question: ")

    if userInput.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!", user_name)
        break

    answer = getUserResponse(userInput)
    print("Chatbot Answer:", answer)
