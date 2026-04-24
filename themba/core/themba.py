from groq import Groq
import os
from themba.config.settings import NAME, PERSONALITY, LLM_PROVIDER, MODEL
from themba.skills.search import search_web
from themba.skills.memory import load_memory, add_to_memory
from themba.skills.launcher import handle_launch

class Themba:
    def __init__(self):
        self.client = None
        self.history = load_memory()
        self.setup_llm()
        print(f"✅ {NAME} brain initialized successfully.")

    def setup_llm(self):
        if LLM_PROVIDER == "groq":
            self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
            print("  Using Groq client")
        else:
            print(f"  ⚠ LLM provider '{LLM_PROVIDER}' not fully set up yet.")

    def get_response(self, user_input: str) -> str:
        """Get response from Themba"""
        try:
            # Detect launch commands first
            launch_keywords = ["open", "launch", "start", "go to", "search on"]
            if any(kw in user_input.lower() for kw in launch_keywords):
                result = handle_launch(user_input)
                if result:
                    self.history = add_to_memory(self.history, "user", user_input)
                    self.history = add_to_memory(self.history, "assistant", result)
                    return result

            # Detect if web search is needed
            search_keywords = ["search", "look up", "find", "what is", "who is",
                             "latest", "news", "today", "current", "weather", "price"]
            needs_search = any(kw in user_input.lower() for kw in search_keywords)

            if needs_search:
                print("  [Searching web...]")
                search_results = search_web(user_input)
                augmented_input = f"""The user asked: {user_input}

Here are web search results to help answer:
{search_results}

Please answer the user's question using the search results above."""
            else:
                augmented_input = user_input

            # Add user message to history
            self.history = add_to_memory(self.history, "user", augmented_input)

            # Build messages with full history
            messages = [{"role": "system", "content": PERSONALITY}] + self.history

            response = self.client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=600
            )

            reply = response.choices[0].message.content.strip()
            self.history = add_to_memory(self.history, "assistant", reply)

            return reply
        except Exception as e:
            return f"I'm sorry sir, I couldn't process that right now. Error: {str(e)[:100]}"

    def greet(self):
        from themba.config.settings import GREETING
        return GREETING