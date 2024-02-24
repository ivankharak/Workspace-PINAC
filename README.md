
<img src="https://github.com/rmondal-official/PINAK/blob/main/Readme%20Assets/pinac%20template.jpg" style="max-width: 100%;" alt="PINAC banner">

# Introduction 👾

<img src="https://github.com/rmondal-official/PINAK/blob/main/Readme%20Assets/fluide%20230%20with%20robot.png" alt="" width="250" height="200" align="right">

**PINAC Intelligent System** is a project that aims to enhanced efficiency of your daily works using **smart voice command** based automation for tasks within **Google Apps**, **Microsoft Apps**, **Meta Apps** and beyond. It intregates **AI** capabilities to complete task like writing email, making subject notes, writing documents, creating presentation and many more. **PINAC** envisions a future where technology seamlessly augments daily workflows, freeing up valuable time and cognitive resources for users.


# Current Stage 🔍 

We are currently in the initial stages of development, laying the groundwork for a robust and versatile automation system. Your contributions are crucial in shaping PINAC's evolution and propelling it towards its full potential.


<h1 align="right">Project Plans 🔮   </h1>
<img src="https://github.com/rmondal-official/PINAK/blob/main/Readme%20Assets/AI%20assistant-modified.png" alt="" width="250" height="250" align="left">
<br>

* **Enhance Efficiency:** Automate repetitive tasks within various applications, minimizing manual effort and maximizing output.  
* **Expand App Compatibility:** Continuously integrate support for new applications, broadening PINAC's reach and utility.  
* **Add New Features:** Introduce more sophisticated automation capabilities, including conditional logic, error handling, and user-defined triggers.  
* **Beginner-Friendly Contribution:** Foster a welcoming and inclusive environment for contributors of all experience levels.  
<br>

# Project File Structure 📁 
Proposed file structure

        app_automation/
        ├── ai_models/                          # folder houses code for interacting with AI models
        │   ├── chatgpt/
        │   ├── gemini/
        │   └── model_utils.py                  # Common utilities for all AI models
        ├── app_configs/                        # stores API keys and credentials 
        │   ├── google.json
        │   ├── microsoft.json
        │   └── meta.json
        ├── apps/                               # folder contains app-wise specific folders
        │   ├── google/
        │   │   ├── __init__.py
        │   │   ├── gmail.py
        │   │   └── drive.py
        │   ├── microsoft/
        │   │   ├── __init__.py
        │   │   ├── outlook.py
        │   │   └── onedrive.py
        │   ├── meta/
        │   |   ├── __init__.py
        │   |   ├── facebook.py
        │   |   └── instagram.py
        |   └── utils.py                       # Common utility functions (if required)
        ├── common/
        │   ├── __init__.py
        │   ├── error_handling.py
        │   ├── logging.py
        │   └── utils.py
        ├── main.py                           # scripts that run our application
        └── requirements.txt


        # NOTE:
        # Name every app python file as appname__automator.py
        # example: for gmail ---> gmail__automator.py
        # only two files shown under google or ms for showing purpose,there will be more
        
If anyone having better idea, let me know in Discussion


# Contribution 🎉

This project is beginner-friendly and we warmly welcome contributions from passionate developers and automation enthusiasts!  
_Please read <a href="https://github.com/rmondal-official/PINAK/blob/main/CONTRIBUTING.md">Contribution.md</a>_


# Contact

If you have any questions, suggestions, or require guidance regarding contribution, feel free to reach out through the following channels:

* **<a href="https://github.com/rmondal-official/PINAK/discussions">GitHub Discussions</a>:** Engage in discussions within the repository's Discussions tab.
* **<a href="https://github.com/rmondal-official/PINAK/issues">Issue Tracker</a>:** Raise issues or questions directly on the project's issue tracker.
* **<a href="https://www.linkedin.com/in/rajesh-mondal-35078b2b5/">LinkedIn</a>**: Feel free to message me if you have any doubt regarding contributon to the project or any doubt on Contribution.md.

We are excited to have you join the PINAC journey! Your contributions will play a vital role in shaping this project into a powerful tool for productivity and efficiency.
