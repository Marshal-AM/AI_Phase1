import re
def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                question, answer = parts[0], parts[1]
                dataset.append({"question": question, "answer": answer})
    return dataset

def find_answer(question, dataset):
    for entry in dataset:
        if question.lower() in entry['question'].lower():
            return entry['answer']
    return "I'm sorry, I don't have an answer to that question."

def chat_with_bot(dataset):
    print("Chatbot: Hi! I'm your Q&A chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        answer = find_answer(user_input, dataset)
        print("Chatbot:", answer)

if __name__ == "__main__":
    dataset_path = 'C:/Users/mathe/OneDrive/Desktop/projects/chatbot/dataset.txt'  
    chat_dataset = load_dataset(dataset_path)
    chat_with_bot(chat_dataset)
