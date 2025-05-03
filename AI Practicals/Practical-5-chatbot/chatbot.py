def restaurant_chatbot():
    menu = {
        "pizza": 12.99,
        "burger": 8.99,
        "salad": 7.50,
        "pasta": 10.50,
        "soda": 2.00,
    }

    print("Welcome to our restaurant chatbot! How can I help you today?")

    while True:
        user_input = input("> ").lower()

        if "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("Hello! How can I assist you with your order?")
        elif "menu" in user_input:
            print("Our menu:")
            for item, price in menu.items():
                print(f"{item}: ${price:.2f}")
        elif "order" in user_input:
            print("What would you like to order?")
            order_item = input("> ").lower()

            if order_item in menu:
                print(f"You've ordered a {order_item}. That will be ${menu[order_item]:.2f}.")
                continue_order = input("Would you like to order anything else? (yes/no): ").lower()
                if "no" in continue_order:
                    print("Thank you for your order!")
                elif "yes" in continue_order:
                    continue
                else:
                    print("I'm sorry, I don't understand.")
            else:
                print("Sorry, we don't have that item on our menu.")
        elif "reservation" in user_input or "book" in user_input:
            print("Please provide your name, date, and time for the reservation.")
            name = input("Name: ")
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time (HH:MM): ")
            print(f"Reservation for {name} on {date} at {time} confirmed.")
        elif "contact" in user_input or "phone" in user_input:
            print("You can contact us at 555-123-4567.")
        elif "address" in user_input:
            print("Our address is 123 Main Street.")
        elif "thank" in user_input or "appreciate" in user_input:
            print("You're welcome! Enjoy your meal.")
        elif "bye" in user_input or "goodbye" in user_input or "exit" in user_input:
            print("Goodbye! Have a great day.")
            break
        else:
            print("I'm sorry, I don't understand. Could you please rephrase your question?")

if __name__ == "__main__":
    restaurant_chatbot() 
