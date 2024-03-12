<head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PINAC</title>
        <style>
        @font-face {
                font-family: nasa;
                src: url(https://github.com/rmondal-official/PINAC/blob/ca9d4fff49503df8ebbb670be994eb2bf7602f0c/common/UI/web/font/nasalization-rg.otf);
        }
        @font-face {
                font-family: ai-text;
                src: url(https://github.com/rmondal-official/PINAC/blob/ca9d4fff49503df8ebbb670be994eb2bf7602f0c/common/UI/web/font/KodeMono-VariableFont_wght.ttf);
        }
        header {
                border-radius: 10px;
                background-color: white;
        }
        #project-title {
                font-size: 15vw;
                color: black;
                font-family: nasa;
                align-items: center;
                padding-top: 4vw;
        }
        .sub-heading {
               font-family: ai-text; 
        }
        </style>
</head>
<body>
        <header>
                <div class="header-content">
                        <h1 id="project-title" align="middle">PINAC</h1>
                </div>
        </header>       
</body>

<br>

<div id="Introduction" align="middle">
Introducing <b>PINAC Intelligent System</b> - your ultimate <b>AI</b> companion! This versatile tool is here to revolutionize your digital interactions on Google Apps, Microsoft Apps, Meta Apps, and beyond. Say goodbye to tedious tasks and hello to seamless integration that boosts productivity and simplifies your daily routine. With AI capabilities for chatting, emailing, note-taking, document creation, PDF summaries, and more, PINAC is the key to enhancing your workflow and saving valuable time and cognitive resources. Get ready to elevate your tech game with PINAC !
</div>


<h1 align="middle" class="sub-heading">🎯 Present Features</h1>

* **Google Contact Integration:** Easily search for and add contacts to your Google Account.
* **Gmail Integration:** Sending emails and creating drafts now made even simpler, with or without attachments.
* **Google Calendar Integration:** Stay on top of your day with a quick look at today's or upcoming events and regional holidays in your Google Calendar. Enjoy the seamless integration!
* **GUI Interface:** We are thrilled to announce that we now have a GUI interface for chatting with AI and asking your queries to get answers! (other features are coming very soon)

<img src="https://github.com/rmondal-official/PINAC/blob/main/readme_assets/App_screenshot.jpg" alt="app screenshot">
<br>


<h1 align="middle" class="sub-heading">💡 Upcoming Features</h1>

* Multiple AI Models integration 🤩
* Much improved GUI interface with better chatting System and features for more efficiency ✨
*  Google Drive & task Integration
*  Voice Command and Voice assistance in App 🗣️
<br>


<h1 class="sub-heading" align="middle">📁 Project File Structure</h1>


        .
        ├── ai_models/               # AI models code
        │   ├── chatgpt/
        │   ├── gemini/
        │   └── model_utils.py       # Common utilities of AI models
        ├── configs/                 # for API keys & credentials 
        ├── apps/                    # contains parent-app-wise folders
        │   ├── google/              # google app-wise .py files
        │   ├── microsoft/           # ms app-wise .py files
        │   ├── meta/                # meta app-wise .py files
        |   └── utils.py             # Common utility functions
        ├── common/
        │   ├── __init__.py          # (If required)
        │   └── UI/                  # GUI App files
        │       ├── main.py          # GUI based on Eel Framework
        │       └── web/             # Web files for GUI (Eel)
        │           ├── index.html
        │           ├── style.css      
        │           └── script.js    
        ├── main.py                  # final scripts
        ├── requirements.txt
        ├── readme_assets/
        ├── .gitignore
        ├── LICENSE
        ├── CONTRIBUTING.md
        └── README.md

If anyone having better idea, let me know in Discussion


<h1 class="sub-heading" align="middle">🎉 Contribution</h1>

Are you a developer or automation enthusiast? Your contributions are eagerly welcomed with open arms!
_Please read <a href="https://github.com/rmondal-official/PINAK/blob/main/CONTRIBUTING.md">Contribution.md</a>_


<h1 class="sub-heading" align="middle">🗨️ Contact</h1>

If you have any questions, suggestions, or require guidance regarding contribution, feel free to reach out through the following channels:

* **<a href="https://github.com/rmondal-official/PINAK/discussions">GitHub Discussions</a>:** Engage in discussions within the repository's Discussions tab.
* **<a href="https://github.com/rmondal-official/PINAK/issues">Issue Tracker</a>:** Raise issues or questions directly on the project's issue tracker.

We are excited to have you join the PINAC journey! Your contributions will play a vital role in shaping this project into a powerful tool for productivity and efficiency.
