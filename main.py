from agent import DataScienceAssistant

def main():
    print("🧠 Welcome to the AI Data Science Assistant Chatbot!")
    print("Ask anything related to data science. Type 'exit' to quit.\n")

    assistant = DataScienceAssistant()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        reply = assistant.ask(user_input)
        print(f"\nAssistant:\n{reply}\n")

if __name__ == "__main__":
    main()
