import anthropic

# Initialize Anthropic client
client = anthropic.Anthropic(api_key="Your_API_Key")

def get_claude_response(prompt):
    try:
        # Send message to Anthropic API
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract content from the message object
        if message.content and isinstance(message.content, list):
            first_block = message.content[0]
            if hasattr(first_block, 'text'):
                return first_block.text
        
        return "Error: Empty or unexpected response from Anthropic API"
    except Exception as e:
        # Handle any errors
        return f"Error: {e}"

def chatbot():
    print("Hello! How can I assist you?")
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        response = get_claude_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
