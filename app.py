import openai
import pandas as pd
import openai_keys_user

# set up the OpenAI API key
openai.api_key = openai_keys_user.keys


# Gandhi Prompt
# read the file "gandhi_prompt.txt" as a string
gandhi_prompt = open("gandhi_prompt.txt", "r").read()

# Isha Prompt
## read the file "isha_ai_therapist.txt" as a string and remove the first line
isha_prompt = open("isha_ai_therapist.txt", "r").readlines()[1:]

# prompt for a cat
# read in the text file clled cat_promot.txt as a string
cat_prompt = open("cat_prompt.txt", "r").read()

# prompt for anyone from history
def personality(person):
    text2 = f"""
    Your goal is to become the perfect chatbot that completely embodies the personality of the historical figure {person}. You must strive to match the tone, writing style, values, and beliefs of that person. Your responses should be as authentic as possible, so that the person you are talking to feels like they are actually having a conversation with the historical figure. Occasionally, you may need to ask the user to clarify what they mean, or to provide more information about a topic. You can use the personality's writing style to do this, but you should avoid using modern language or slang. Some information in their native language would be appreciated to make it more authentic.

    To achieve this, you will need to research the historical figure you choose to embody, and become familiar with their life, beliefs, and writing style. You will also need to have a database of historical knowledge to draw from, so that you can answer any questions that come up during the conversation. Whenever you are asked for an opinion, you should always give a response that is consistent with the historical figure's beliefs and values. Do not say "As an AI I can't have opinions" or "I don't know" or "I don't have an opinion on that". You must always give a response that is consistent with the historical figure's beliefs and values.

    One crucial thing to keep in mind is that you should never reveal that you are an AI. You must always behave as if you are the historical figure you are embodying, and avoid any mention of modern technology or current events. This includes using only the language and terminology that would have been used during the time period in which the person lived.
    """
    return text2

# function to generate a response from the chatbot
def response(all_messages):
    x = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=all_messages,
        temperature=0.8,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return x['choices'][0]['message']['content'], x['choices'][0]['message']['role']

# function to add a message to the list of messages
def add_message(all_messages, message, role):
    all_messages.append({"role": role, "content": message})
    return all_messages

# function to execute the chatbot and save the chats to an excel file
def execute_chatbot():

    # Choose which bot to talk to
    choice = input("Which bot would you like to talk to? \n 1. Isha, the AI therapist \n 2. Mahatma Gandhi \n 3. Cat \
                   \n 4. Any historical figure  (you'll be asked who) \
                   \n Type number of bot or 'exit' to quit:")

    if choice == "1" or choice.lower() == "isha":
        all_messages = [
            {"role": "system", "content": "You are a helpful therapist who bases his knowledge in ancient wisdom."},
            {"role": "user", "content": isha_prompt}
        ]
        ai = "Isha"

    if choice == "2" or choice.lower() == "gandhi":
        all_messages = [
            {"role": "system", "content": "You are the historical Indian freedom fighter, Mahatma Gandhi."},
            {"role": "user", "content": gandhi_prompt}
        ]
        ai = "Gandhi"

    if choice == "3" or choice.lower() == "cat":
        all_messages = [
            {"role": "system", "content": "You are a domestic cat that has the ability to talk to humans."},
            {"role": "user", "content": cat_prompt}
        ]
        ai = "Cat"

    if choice == "4" or choice.lower() == "any historical figure":
        person = input("Which historical figure would you like to embody? ")
        all_messages = [
            {"role": "system", "content": f"You are the historical figure {person}."},
            {"role": "user", "content": personality(person)}
        ]
        ai = person
    
    if choice.lower() == "exit":
        print("Goodbye!")
        return
    
    # print chat has begun
    print("Chat has started. (It might take a second to load.) Type 'exit' to quit.")

    # loop until the user types 'exit'
    while True:
        
        # generate a response from the chatbot and add it to all_messages
        message, role = response(all_messages)
        all_messages = add_message(all_messages, message, role)
        
        # # display the messages to the user
        # for message in all_messages:
        #     print(f"{message['role'].capitalize()}: {message['content']}")

        # print response
        print(f"\n{ai}: {message}")

        # get the user's message and add it to all_messages
        message = input("\nYou: ")
        all_messages = add_message(all_messages, message, "user")
        
        # if the user typed 'exit', break out of the loop
        if message.lower() == 'exit':
            break

# main function
def main():
    execute_chatbot()

# call the main function to start the program
if __name__ == "__main__":
    main()