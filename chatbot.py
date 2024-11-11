import random

responses = {
    "greeting": ["Hello! How can I help you today?", "Hi! How can I assist you?", "Hey! How may I help you?"],
    "order": ["Your order is being processed and will be delivered soon.", 
              "We are packing your order. Expect it to ship soon!", 
              "Your order will arrive in 3-5 business days."],
    "payment": ["We accept credit card, debit card, and PayPal payments.", 
                "You can pay via credit card or PayPal.", 
                "We have multiple payment options including PayPal and cards."],
    "goodbye": ["Goodbye! Have a great day!", "See you soon! Bye!", "Thank you for visiting. Goodbye!"]
}

def chatbot():
    print("Welcome  Chatbot! Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'bye':
            print("Chatbot: " + random.choice(responses["goodbye"]))
            break
        
        # Simple keyword-based responses with randomness
        if "hello" in user_input.lower() or "hi" in user_input.lower():
            print("Chatbot: " + random.choice(responses["greeting"]))
        elif "order" in user_input.lower():
            print("Chatbot: " + random.choice(responses["order"]))
        elif "payment" in user_input.lower():
            print("Chatbot: " + random.choice(responses["payment"]))
        elif "bye" in user_input.lower():
            print("Chatbot: " + random.choice(responses["goodbye"]))
            break
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")

# Start the chatbot
chatbot()
