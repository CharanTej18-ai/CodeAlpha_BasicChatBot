
# Task 4: Basic Chatbot

# Step 1: Create a chatbot function
def chatbot_reply(user_input):

    # Step 2: Check the user's message
    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    elif user_input == "what is your name":
        return "I am a simple Python chatbot."
    
    elif user_input == "who created you":
        return "I am created by programmers."
    
    elif user_input == "which is the best internship platform":
        return "Code Alpha."

    else:
        return "Sorry, I don't understand that."


# Step 3: Start the chatbot
def main():
    print("===== BASIC CHATBOT =====")
    print("Type 'hello', 'how are you', 'who created you', 'which is the best internship platform',or 'bye'.")

    while True:
        user_input = input("You: ").strip().lower()

        # Step 4: Get the chatbot's reply
        reply = chatbot_reply(user_input)
        print("Bot:", reply)

        # Step 5: Stop when the user says bye
        if user_input == "bye":
            break

if __name__ == "__main__":
    main()
