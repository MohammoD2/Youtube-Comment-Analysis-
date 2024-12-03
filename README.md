Youtube Comment Analysis v1
==============================

YouTube Comment Analysis involves extracting, processing, and analyzing comments from YouTube videos to uncover insights. This analysis can provide valuable information about audience sentiment, engagement trends, and the effectiveness of content strategies.YouTube Comment Analysis involves extracting, processing, and analyzing comments from YouTube videos to uncover insights. This analysis can provide valuable information about audience sentiment, engagement trends, and the effectiveness of content strategies.

# YT Chrome Plugin Repository

This repository contains the necessary files and instructions to set up a Flask backend and a custom Chrome extension for YouTube. Follow the steps below to install and run the project.

## Requirements
- Python 3.x
- Pip (Python package manager)
- Google Chrome Browser
- Google API Key for YouTube Data API

---

## Installation Instructions

### 1. Clone the Backend Repository
Download the backend repository to your local machine. Open your terminal or command prompt and run:
```bash
git clone https://github.com/YourUsername/yt-chrome-plugin.git
cd yt-chrome-plugin
```
### 2. Install Backend Dependencies
Use the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```
### 3. Run the Flask App
Navigate to the project folder and start the Flask application:
```bash
python app.py
```
### 4. Clone the Frontend Repository
Download the frontend repository for the Chrome extension:
```bash
git clone https://github.com/MohammoD2/yt-chrome-plugin-frontend.git
```
### 5. Update the API Key
Locate the appropriate JavaScript file in the frontend repository (e.g,popup.js). Replace the placeholder API key with your Google API YouTube Key:
```bash
const API_KEY = 'YOUR_GOOGLE_API_KEY';
```
## Get a YouTube API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/) and log in.
2. Create a new project:
   - Click **Project** dropdown > **New Project** > Name it > **Create**.
3. Enable the YouTube Data API v3:
   - Go to **APIs & Services > Library** > Search for "YouTube Data API v3" > **Enable**.
4. Generate an API key:
   - Go to **APIs & Services > Credentials** > **Create Credentials** > **API Key** > Copy it.
5. (Optional) Restrict your API key:
   - In **Credentials**, click the pencil icon next to your key > Set restrictions (e.g., HTTP referrers or IPs) > **Save**.

### 6. Load the Chrome Extension

1. Open Google Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer Mode** by toggling the switch in the top-right corner.
3. Click on **Load unpacked**.
4. Select the folder of the cloned frontend repository.
5. Now you able to run my repository





