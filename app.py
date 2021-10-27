#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask.wrappers import Response
import wikipedia
from wikipedia.exceptions import PageError
# chatterbot==1.0.8 has issue with spacy v3 so got to edit tagging.py's 13th line for english support
#It's only for the first time
#Sorry for my trashy code but it works :)
with open(r'venv\Lib\site-packages\chatterbot\tagging.py', 'r') as tagfile:
    # read a list of lines into myeditlines
    myeditlines = tagfile.readlines()

# now change the 13th line, note that you have to add a newline
myeditlines[12] = ("   "+"     if self.language.ISO_639_1.lower() == 'en':\n"+"   "+"         self.nlp = spacy.load('en_core_web_sm')\n"+"   "+"     else:\n"+"  "+"          self.nlp = spacy.load(self.language.ISO_639_1.lower())\n")

# and write everything back
with open(r'venv\Lib\site-packages\chatterbot\tagging.py', 'a') as tagfile:
    tagfile.writelines(myeditlines)
    tagfile.close()


app = Flask(__name__)
#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english")
read_only=True
#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    if "search" in userText or "find" in userText or "pedia"in userText or"wiki"in userText:
        try:
            statement="According to Wikipedia "+wikipedia.summary(userText, sentences=3)
        except:
            response="Sorry,try something else"
            return response
    else:
        statement=str(englishBot.get_response(userText))
    return statement

if __name__ == "__main__":
    app.run()