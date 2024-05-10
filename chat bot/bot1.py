from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def generate_response(prompt, max_length=100, num_return_sequences=1):
    # Tokenize input and generate response
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output_ids = model.generate(input_ids, max_length=max_length, num_return_sequences=num_return_sequences)
    responses = [tokenizer.decode(output_id, skip_special_tokens=True) for output_id in output_ids]
    return responses

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    # Generate a response based on user input
    response = generate_response(user_input, max_length=50, num_return_sequences=1)[0]

    print("Chatbot:", response)