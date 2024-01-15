
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new chat bot named AdmissionBot
admission_bot = ChatBot('AdmissionBot', storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not have information about that. Please consult the college admission office.',
        'maximum_similarity_threshold': 0.3
    }
])

corpus_trainer = ChatterBotCorpusTrainer(admission_bot)

# Train the chatbot using the English language corpus data
corpus_trainer.train('chatterbot.corpus.english')


trainer = ListTrainer(admission_bot)

# Train with admission-related data
trainer.train([
    "Hi, I am your AdmissionBot, here to help with your college admission queries!",
    "What are the admission procedures?",
    "Admission procedures typically involve submitting an application, relevant documents, and meeting eligibility criteria.",
    "What are the admission requirements?",
    "Admission requirements may include GPA, standardized tests, recommendation letters, and other specific criteria depending on the college and program.",
    "Are there any deadlines for admission?",
    "Yes, admission deadlines vary by college and program. It's crucial to check the specific deadlines for the college you are interested in.",
    "Goodbye",
    "Goodbye! If you have more admission questions, feel free to ask.",
])

# Dynamic user interaction
user_name = input("AdmissionBot: Hi, I am your AdmissionBot! What is your name?\nUser: ")
response = admission_bot.get_response(f"My name is {user_name}.")
print(f"AdmissionBot: {user_name} is a great name! How can I assist you with your college admission today?")

conversation = []  # Maintain a list to store the conversation

while True:
    user_input = input(f"{user_name}: ")
    conversation.append(f"{user_name}: {user_input}")

    if user_input.lower() == 'bye':
        response = admission_bot.get_response("Goodbye! If you have more admission questions, feel free to ask.")
        conversation.append(f"AdmissionBot: {response}")
        print(f"AdmissionBot: {response}")
        break
    else:
        try:
            response = admission_bot.get_response(user_input)
            conversation.append(f"AdmissionBot: {response}")
            print(f"AdmissionBot: {response}")
        except:
            response = "I am sorry, but I do not have information about that. Please consult the college admission office."
            conversation.append(f"AdmissionBot: {response}")
            print(f"AdmissionBot: {response}")
