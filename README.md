# GPT Chatbot
 GPT-based chatbot for talking to:
 1. My cat, Gary
 2. Mahatma Gandhi
 3. A therapist called Isha
 4. Any personality from history

## How to use
 1. Clone the repo or download the zip (See the green button on the top right)
 2. Install the requirements (`pip install -r requirements.txt`)
 3. Get OpenAI API keys from https://platform.openai.com/account/api-keys. Put them in the Python script called `openai_keys_user.py`.
 4. Run the script `python3 app.py`.
 5. Choose a personality to talk to.
 6. Enjoy! Type `exit` to exit the chat. 
 7. To restart the chat, run the script again.

 Note: Remember to be in the same directory as the script when you run it. If you are not, you can use `cd` to change the directory. Ask ChatGPT for help if you need it. (Or raise an issue on the GitHub repo.)

## How it works
The script uses the OpenAI API to generate text. The API is called with a prompt, which is the text that the model uses to generate the next text. The first prompt would depend on the personality you choose to talk to. Subsequent prompts are texts that the user has typed so far. The model generates the next text, and the user types the next text. This process is repeated until the user types `exit`.

If you run into any issues, please open an issue on the GitHub repo. Have fun!

## Next
1. I am planning to add more personalities to talk to. If you have any suggestions, please open an issue on the GitHub repo.
2. There will be a blog post on my website explaining how I built this and how to use it in complete detail. I will link it here when it is ready.

## Pro-tip
I've provided the prompts here in the text files. YOu can use them to talk to the personalities in ChatGPT web app as well. Specifically, I've found talking to the cat (`cat_prompt.txt`) to be much better when talking via GPT-4 than GPT-3.5-turbo, on which the current app is based. I don't have access to GPT-4 API yet, but I will update the app when I do.