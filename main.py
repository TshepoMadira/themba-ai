from themba.core.themba import Themba
from themba.utils.voice import speak
from themba.skills.memory import clear_memory

def main():
    print("🚀 Initializing Themba...\n")
    themba = Themba()

    greeting = themba.greet()
    print(greeting)
    speak(greeting)
    print("Type 'exit' to quit or 'forget' to clear memory.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                farewell = "Goodbye sir. It was a pleasure assisting you."
                print(f"Themba: {farewell}")
                speak(farewell)
                break

            if user_input.lower() == 'forget':
                clear_memory()
                themba.history = []
                print("Themba: Memory cleared, sir. Fresh start.\n")
                continue

            if not user_input:
                continue

            print("Thinking...")
            response = themba.get_response(user_input)
            print(f"\nThemba: {response}\n")
            speak(response)

        except KeyboardInterrupt:
            print("\n\nThemba: Shutting down... Take care, sir.")
            speak("Shutting down. Take care, sir.")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()