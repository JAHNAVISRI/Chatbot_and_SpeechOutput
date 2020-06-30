# Chatbot_and_SpeechOutput

# To Create the ChatBot

1) mkdir watson_ws/src

2) clone this repository from GitHub to your src

3) create the virtual environment in the name of venv

4) source venv/bin/activate

5) pip install aiml

6) cd watson_ws/src/pyaiml

7) python test.py (This file gives output for the input speech/text)

To provide speech input, git clone the speech workspace and run

python recognize_speech.py 

Note: The prebuild convo required for our specific purpose is already trained. To re-train the models follow the guide 

# To get Sound Output

1) source venv/bin activate

2) pip install watson-developer-cloud

3) cd watson_ws/src

4) python rostts.py

Note: There is a word limit for usage of watson_ws. So the speech output can be replaved any other sound package.
