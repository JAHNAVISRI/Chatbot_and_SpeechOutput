# To Create a ChatBot

Create a virtual environment in the name of venv

1) source venv/bin/activate
	
2) pip install aiml
	
3) mkdir watson_ws/src

4) git clone this package into src folder

5) cd watson_ws/src/Chatbot_and_SpeechOutput/pyaiml
  
6) python test.py (This file gives the output for the provided input through Voice/Keyboard)

To provide the input through speech, git clone the speech package and run

7) python recognize_speech.py

Note: The prebuild convo required for our specific purpose is already trained. To re-train the models follow the guide

# To get Sound Output

1) source venv/bin activate

2) pip install watson-developer-cloud

3) cd watson_ws/src/Chatbot_and_SpeechOutput

4) python rostts.py

Note: There is a word limit for usage of watson_ws. So the speech output can be replaved any other sound package.
