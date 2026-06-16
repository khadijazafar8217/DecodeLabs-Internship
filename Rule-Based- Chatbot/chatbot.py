# Main logic skeleton for the Rule-Based AI Chatbot
from Responses import GREETINGS, EXIT_COMMANDS, KNOWLEDGE_BASE

def start_chatbot():
    print("AI: Hello! Welcome to the DecodeLabs Rule-Based AI Chatbot interface.")
    print("(Type 'exit', 'bye', or 'quit' at any time to close the session)\n")
    # Continuous loop for human-machine interaction

    while True:
        # Step 1: Input (Raw Feed)
        raw_input = input("You: ")
        # Step 2: Sanitization & Normalization
        clean_input = raw_input.lower().strip()
        
        # Step 3: Process (The Logic Skeleton)
        
        # Check for Exit Commands
        if clean_input in EXIT_COMMANDS:
            print("AI: Goodbye! Have a productive day at DecodeLabs.")
            break # Breaks the continuous loop
            
        # Check for Greetings
        elif clean_input in GREETINGS:
            print("AI: Hello there! How can I assist you with your training task today?")
            
        # Check for Intent Matching in Knowledge Base
        elif clean_input in KNOWLEDGE_BASE:
            print(f"AI: {KNOWLEDGE_BASE[clean_input]}")
            
        # Fallback for unexpected inputs (White-box deterministic guardrail)
        else:
            print("AI: I am sorry, but I do not recognize that instruction. I am programmed to only follow specific predefined rules.")

if __name__ == "__main__":
    start_chatbot()