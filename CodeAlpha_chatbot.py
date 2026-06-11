def chatbot():

    print("=== AI Chatbot ===")
    print("Type 'bye' to exit\n")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hello! How can I help you?")

        elif "name" in user:
            print("Bot: My name is CloudBot.")

        elif "college" in user:
            print("Bot: I can help with college-related queries.")

        elif "course" in user:
            print("Bot: Information Science and Engineering is a great course.")

        elif "cloud" in user:
            print("Bot: Cloud Computing provides on-demand computing services.")

        elif "python" in user:
            print("Bot: Python is a popular programming language.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()