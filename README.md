# 🧠 Social Media Tracker Web App

This is a Streamlit-based web application that scrapes user-reported issues and discussions from **Reddit**, **Microsoft Learn**, and **Microsoft Tech Community**, filtered by Windows-related keywords. It helps testers, developers, and support engineers monitor feedback and reported problems across platforms in one place.

---

## 🚀 Features

- 🔍 Scrapes data from:
  - Reddit (multiple subreddits)
  - Microsoft Learn Q&A
  - Microsoft Tech Community forums
- 🧠 Filters posts using Windows-specific keywords
- 📅 Displays data from recent days or full history
- 📊 View data in interactive tables
- 📥 Download filtered results as Excel directly from the app

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- PRAW (Reddit API)
- BeautifulSoup (web scraping)
- Selenium (web interaction)
- OpenPyXL (Excel export)

---

## 📦 Setup Instructions

### Clone the repo

```bash
git clone https://github.com/LokeshAdivishnu/SMT_WebApp.git
cd SMT_WebApp
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run webapp.py
```

App will run locally at `http://localhost:8501`

---

## 🌐 Deploy Online (Optional)

Use [Streamlit Cloud](https://streamlit.io/cloud) for free hosting:

1. Push your code to GitHub
2. Log in at [streamlit.io/cloud](https://streamlit.io/cloud)
3. Create a new app → Link your GitHub repo
4. Deploy & share your unique URL!

---

## 📁 Project Structure

```
SMT_WebApp/
├── webapp.py               # Main Streamlit script
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```

---

## 🧩 To-Do / Enhancements

- 🔄 Replace Selenium with headless API scraping for full online support
- 📈 Add charts (e.g., volume trends or top keywords)
- 🔔 Add email alerts or notifications
- ⏱️ Set up automatic data refresh (scheduler)

---

## 📬 Author

**Lokesh Adivishnu**  
GitHub: [@LokeshAdivishnu](https://github.com/LokeshAdivishnu)

---

## 📝 License

This project is open-source and free for personal and educational use.
