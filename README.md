
<img src="https://github.com/rmondal-official/PINAC/blob/main/Readme%20Assets/PINAC_template%202.png" style="max-width: 100%;" alt="PINAC banner">


<div align="middle">
PINAC Intelligent System automates tasks in Google Apps, Microsoft Apps, Meta Apps, and more using APIs. It integrates AI for writing emails, notes, documents, and presentations. PINAC envisions tech enhancing workflows to save time and cognitive resources.
</div>
<div align="middle"> 
<b>It's currently in early development phase. Your contributions shape PINAC's growth towards its full potential.</b>
</div>


<h1 align="middle">🎯 Present Features</h1>

* **Google Contact Integration:** Easily search for and add contacts to your Google Account.
* **Gmail Integration:** Sending emails and creating drafts now made even simpler, with or without attachments.
* **Google Calendar Integration:** Stay on top of your day with a quick look at today's or upcoming events in your Google Calendar. Enjoy the seamless integration!


<h1 align="middle">📁 Project File Structure</h1>
Project file structure ✨  

        .
        ├── ai_models/                          # folder houses code for interacting with AI models
        │   ├── chatgpt/
        │   ├── gemini/
        │   └── model_utils.py                  # Common utilities for all AI models
        ├── app_configs/                        # stores API keys and credentials 
        │   ├── google.json, etc
        ├── apps/                               # folder contains app-wise specific folders
        │   ├── google/
        │   │   ├── __init__.py
        │   │   ├── gmail.py
        │   │   └── drive.py
        │   ├── microsoft/..
        │   ├── meta/..
        |   └── utils.py                       # Common utility functions (if required)
        ├── common/
        │   ├── __init__.py
        │   ├── GUI /..
        │   ├── error_handling.py
        │   └── utils.py
        ├── main.py                           # scripts that run our application
        └── requirements.txt

If anyone having better idea, let me know in Discussion


<h1 align="middle">🎉 Contribution</h1>

Are you a developer or automation enthusiast? Your contributions are eagerly welcomed with open arms!
_Please read <a href="https://github.com/rmondal-official/PINAK/blob/main/CONTRIBUTING.md">Contribution.md</a>_


<h1 align="middle">Contact</h1>

If you have any questions, suggestions, or require guidance regarding contribution, feel free to reach out through the following channels:

* **<a href="https://github.com/rmondal-official/PINAK/discussions">GitHub Discussions</a>:** Engage in discussions within the repository's Discussions tab.
* **<a href="https://github.com/rmondal-official/PINAK/issues">Issue Tracker</a>:** Raise issues or questions directly on the project's issue tracker.

We are excited to have you join the PINAC journey! Your contributions will play a vital role in shaping this project into a powerful tool for productivity and efficiency.
