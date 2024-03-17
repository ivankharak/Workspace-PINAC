<h2 align="middle"> Getting Started with Google APIs :<br> A Beginner's Guide</h2>

This guide will walk you through the **basic steps** of getting started with Google APIs for this Project, making it easy for beginners.


## 1. Create a Google Cloud Project

First create your Google Cloud account using your gmail id.

To use Google APIs, you'll need a Google Cloud Project. It's free to create and easy to manage. Head over to: [https://console.cloud.google.com/](https://console.cloud.google.com/)

Click **Create Project** and give it a descriptive name.


## 2. Enable Required APIs

Go back to the <a herf="https://console.cloud.google.com/apis/library?orgonly=true&project=eco-notch-382007&supportedpurview=project">API Explorer Page</a> and find the specific API you want to use.    
For this project you need:  
* **Google People API**
* **Gmail API**
* **Google Calendar API**
* **Google Drive API**
* **Google Tasks API**

Click on it and navigate to the **Enable API** section. 



## 3. Create App
Go to <a herf="https://console.cloud.google.com/apis/credentials/consent?orgonly=true&project=eco-notch-382007&supportedpurview=project">This Page</a> and Create App.

Remember: (Set Publishing status:  **Testing App**, User type: **External** ) and fill other required details.

> ### ⚠️ Required Scopes for App:  
> 1. "https://www.googleapis.com/auth/contacts"  
> 2. "https://mail.google.com/"   
> 3. "https://www.googleapis.com/auth/calendar"  
> 4. "https://www.googleapis.com/auth/tasks"

Next add **text users** (the account from which you are going fetch apps data).


## 4. Create Credentials
To access the API, you'll need credentials  
Go to the **credentials** then:  
1. **Click Create Credentials > OAuth client ID.**
2. **Click Application type > Desktop app**
3. Don't change application name. It can cause somtime unwanted error
4. Click **OK**
5. **Download the JSON file**,
6. Change the JSON file name to exactly `client_secret.json` and place it to `configs/` folder of the project.



## 4. Install the Client Library

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## 5. Done !