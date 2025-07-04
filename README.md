Psy-9

A voice-controlled magic trick disguised as customer service.The magician gets the card wrong — then says, “It’s okay. I have insurance.”

The Premise: Magician Insurance

You guess the spectator’s card.
You get it wrong.
An awkward pause.
You look nervous, then say calmly,“That’s fine. I have magician’s insurance.”
You hand them a business card for a mysterious company.They call the number.You type in your security code.
After a moment, a robotic voice answers:
"Your spectator chose the Seven of Hearts. Thank you for using Psy-9."

They hang up.No app. No stooge. No explanation.Just a phone call and a company that somehow knows.


What Is Psy-9?

Psy-9 is a fully automated, real-time voice illusion powered by:
A seven-digit security code that encodes any card in a deck
Twilio voice menus and DTMF input
Pre-generated MP3 files for all cards and system responses
AWS Polly for voice synthesis
A Flask backend that handles everything during the call

This is not a gimmick or a simulation. It's a working magic trick delivered through actual phone infrastructure. No app installation required. No special props. No assistants. Just code, sound, and misdirection.

Project Structure - 

deck.py:
Generates the 52 card audio files using AWS Polly

audio_manager.py:
Flask app containing Twilio endpoints and logic for call handling

/generated_audio:
Folder containing MP3s for each card and system prompts

Required audio files:
intro.mp3, code.mp3, invalid.mp3, processing.mp3, thank_you.mp3, goodbye.mp3

How the Code Works:
Spectators are prompted to enter a 7-digit code. The format is:

[12][S][CC][21]

12 — Start security digits
S — Suit index (1–4)
CC — Card value index (01–13)
21 — End security digits

Example: 1231321 decodes to "King of Spades"

Once the code is submitted:

If valid:
Plays processing.mp3
Plays the chosen card’s MP3 file
Plays thank_you.mp3

If invalid:
Plays invalid.mp3
Allows one retry
Then plays goodbye.mp3 and ends the call

Installation:

Install Python dependencies:
pip install flask twilio boto3 tqdm

Set up AWS credentialsThis script uses Amazon Polly to generate audio. Make sure your AWS CLI is configured or credentials are available under ~/.aws/credentials.

Generate audio filesRun the generator to create card audio:
run - python deck.py

Make sure your /generated_audio folder contains the 52 card MP3s plus the required system files listed above.

Start the server:
run - python audio_manager.py

Expose your server to the internetUse a tunneling tool like ngrok:
ngrok http 5000

Then point your Twilio number’s Voice webhook to:
https://your-ngrok-url/gather

Performing the Effect:

Spectator names a card
You intentionally get it wrong
You hand them a business card for your “Magician Insurance Provider”
They call the number
You discreetly input the 7-digit code

The system does the rest

The performance is 100% hands-off after the code is entered.The audio reveals are polished and professional.The impact is surreal.

Why I Made This:

I wanted to build a magic trick that used real-world tools to create a performance that felt unexplainable. Not just a prank — a fully contained system. Something I could hand to a spectator without needing to talk, tap, or guide.
This was the first time I blended API logic, audio generation, and Twilio’s voice platform into something theatrical.
It’s a strange project. But it works.

Future Ideas:

Add speech recognition instead of keypad input
Create style variants: friendly, threatening, prophetic, bureaucratic
Add GUI for generating alternate prompt sets

Final Note

This project was finished on April 1st, 2025. It was not a joke.
