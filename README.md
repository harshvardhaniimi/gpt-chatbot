# GPT Chatbot
 GPT-based chatbot for talking to:
 1. My cat, Gary
 2. Mahatma Gandhi
 3. A therapist called Isha
 4. Any personality from history

## How to use
 1. Clone the repo or download the zip (See the green button on the top right)
 2. Install the requirements ( `pip install -r requirements.txt`)
 3. Get OpenAI API keys from https://platform.openai.com/account/api-keys. Put them in the Python script called `openai_keys_user.py`.
 4. Run the script `python3 gpt_chatbot.py`.
 5. Choose a personality to talk to.
 6. Enjoy! Type `exit` to exit the chat. 
 7. To restart the chat, run the script again.

## How it works
The script uses the OpenAI API to generate text. The API is called with a prompt, which is the text that the model uses to generate the next text. The first prompt would depend on the personality you choose to talk to. Subsequent prompts are texts that the user has typed so far. The model generates the next text, and the user types the next text. This process is repeated until the user types `exit`.

If you run into any issues, please open an issue on the GitHub repo. Have fun!
