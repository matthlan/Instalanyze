<div align="center">

# 📊 Instalanyze

### Insta DM Analyser 💬

*Upload an Instagram chat, get instant charts. Find out who texts more, when, and with which emojis.* 😏

</div>

---

## ✨ What does it do?

Drop in the JSON file Instagram gives you when you download your data, and Instalanyze turns one conversation into interactive charts:

| | Feature | What you get |
|---|---|---|
| 📈 | **Messages per day** | A line chart of how many messages each person sent over time, plus the total |
| 🥧 | **Who talks more?** | A pie chart of the share of messages sent by each participant |
| 😂 | **Most used emojis** | A bar chart of the top 10 emojis in the conversation |

All charts are built with [Plotly](https://plotly.com/python/), so you can hover, zoom and pan. 🔍

## 🚀 Getting started

### 📋 Prerequisites

- 🐍 Python 3.8 or later
- 📦 `pip`

### 🔧 Installation

```bash
git clone https://github.com/matthlan/Instalanyze.git
cd Instalanyze
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install streamlit
```

> ⚠️ **Heads up:** `app.py` imports `streamlit`, but it is not listed in `requirements.txt`, so it is installed separately above. Adding it to `requirements.txt` is recommended.

### ▶️ Run it

```bash
streamlit run app.py
```

Streamlit opens the app in your browser, by default at `http://localhost:8501`. 🎉

## 📥 How to get your Instagram data

1. 📱 In Instagram, go to **Settings → Accounts Center → Your information and permissions → Download your information**.
2. 🗂️ Request your data, choose **JSON** as the format, and include at least the *Messages* category.
3. 📧 When Instagram sends the archive, download and unzip it.
4. 💬 Your conversations are in `messages/inbox/<conversation-name>/`, stored as `message_1.json` (plus `message_2.json`, … for long chats).

> ℹ️ Menu names change from time to time. If they differ, check Instagram's help pages.

## 🕹️ Usage

1. ▶️ Start the app with `streamlit run app.py`.
2. 📤 Click **Upload your JSON file** and pick a `message_*.json` file.
3. 🔎 Click **Analyze**.
4. 🎨 Explore your charts!

## 🚧 Limitations

- 👫 Made for **one-to-one conversations** (two participants). Group chats are not supported yet.
- 📄 Each upload analyses **one JSON file**. Long chats are split into several `message_N.json` files, which must be analysed separately for now.
- 🙈 Messages without text (photos, reels, …) and "Liked a message" entries are ignored in the emoji count.

## 🔒 Privacy

Everything runs on **your own machine** 🏠: the app's code sends nothing to any third-party service. Chat exports are personal data, so keep your JSON files private and **never commit them to Git**. 🤫

## 🧰 Built with

- 🎈 [Streamlit](https://streamlit.io/) – web interface
- 🐼 [pandas](https://pandas.pydata.org/) and 🔢 [NumPy](https://numpy.org/) – data handling
- 📊 [Plotly](https://plotly.com/python/) – interactive charts
- 😀 [emojis](https://pypi.org/project/emojis/) – emoji extraction

---

<div align="center">

Made with ☕ and way too many 😂

</div>
