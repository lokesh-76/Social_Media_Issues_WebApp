# Social Media Tracker Web App

This is a Streamlit-based web application designed to scrape user-reported issues and discussions from Reddit, Microsoft Learn, and Microsoft Tech Community, specifically filtered by Windows-related keywords.  
It enables testers, developers, and support engineers to monitor feedback and reported problems across platforms in a single interface.

## Features

- Scrapes data from:
  - Reddit (multiple subreddits)
  - Microsoft Learn Q&A
  - Microsoft Tech Community forums
- Filters posts using Windows-specific keywords
- Displays data from recent days or the full history
- Presents results in interactive, filterable tables
- Allows direct download of filtered results as Excel files

## Tech Stack

- Python
- Streamlit
- Pandas
- PRAW (Reddit API)
- BeautifulSoup (Web Scraping)
- Selenium (Web Interaction)
- OpenPyXL (Excel Export)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/LokeshAdivishnu/SMT_WebApp.git
   cd SMT_WebApp
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run webapp.py
   ```
   The app will run locally at: [http://localhost:8501](http://localhost:8501)

## Optional: Deploy Online

You can deploy the app using Streamlit Cloud:

1. Push your code to GitHub
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and link your GitHub repository
4. Deploy and share your unique URL

## Project Structure

```
SMT_WebApp/
├── webapp.py               # Main Streamlit script
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```

## Future Enhancements

- Replace Selenium with headless API-based scraping for better online compatibility
- Add charts such as volume trends or top keywords
- Implement email alerts or notifications
- Set up automatic data refresh using a scheduler

## License

This project is open-source and free for personal and educational use.

---

**Created by Lokesh Adivishnu**
