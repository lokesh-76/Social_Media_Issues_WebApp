import os
import praw
import pandas as pd
import time
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st

st.set_page_config(page_title="Social Media Tracker", layout="wide")

# Keywords to filter
keywords = ['windows','report','issue','update','upgrade','screen','hang','flick','package','crash','error','problem','bug',
            'fix','patch','troubleshoot','help','support','solution','work','download','install','uninstall','play','glitch',
            'launch','stuck','23h2','24h2','25h2','26h2']

st.title("🔍 Social Media Tracker")
st.caption("Scraping Reddit and Microsoft Community")

# Initialize containers
with st.spinner("Fetching Reddit data..."):
    try:
        reddit = praw.Reddit(  
            client_id='v3cuXYxt94bXX3hZmWvWtA',
            client_secret='oAE-Hxcrv2KddpRBgzwaiToGXozxfQ',
            user_agent='Glad-Line-2254'
        )
        subreddits = ['windowsinsiders','Games','gaming','videogames','WindowsHelp','Windows','Windows10','Windows11','techsupport',
                      'pcmasterrace','gaming','games','SteamDeck','gamesEcultura','Steam','PCGaming','gachagaming','Gamingcirclejerk',
                      'gameswap','GameStop','truegaming','gamedev','PS4','XboxOne','Retrogaming','IndieDev','pcgaming','bugs',
                      'softwarebugs','TechSupport','webdev','CrashBandicoot']
        dict_reddit = {}
        count = 0
        for sub in subreddits:
            for submission in reddit.subreddit(sub).new(limit=50):
                dict_reddit[count] = {
                    "Date": pd.to_datetime(submission.created_utc, unit='s', errors='coerce'),
                    "Title": submission.title,
                    "url": submission.url,
                    "Source": "Reddit",
                    "UpVotes": submission.ups
                }
                count += 1
            time.sleep(2)
        df_data = pd.DataFrame.from_dict(dict_reddit, orient='index')
        df_data = df_data.drop_duplicates(subset=['Title'], keep='first')
        df_data.loc[:, "Date"] = pd.to_datetime(df_data["Date"], unit='s', errors='coerce')
        df_reddit = df_data.sort_values(by='Date', ascending=False)
    except Exception as e:
        st.error(f"Reddit scraping failed: {e}")
        df_reddit = pd.DataFrame()

# Microsoft Learn
with st.spinner("Fetching Microsoft Community data..."):
    try:
        dict_learn = {}
        for page in range(1, 6):
            url = f"https://learn.microsoft.com/en-us/answers/tags/60/windows?orderby=createdat&page={page}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            blocks = soup.find_all('div', class_='box margin-bottom-xxs')
            for count, block in enumerate(blocks):
                title_tag = block.find('h2', class_='title is-6 margin-bottom-xxs')
                link_tag = block.find('a')
                date_tag = block.find('span', class_='display-block font-size-xs has-line-height-reset')
                title = title_tag.get_text(strip=True) if title_tag else 'No title'
                link = "https://learn.microsoft.com" + link_tag.get('href') if link_tag else 'No link'
                date_str = date_tag.get_text(strip=True).replace('asked', '').strip() if date_tag else 'No date'
                dict_learn[len(dict_learn)] = {
                    "Date": pd.to_datetime(date_str, errors='coerce'),
                    "Title": title,
                    "url": link,
                    "Source": "Microsoft Learn",
                    "UpVotes": ""
                }
            time.sleep(2)
        df_data_m = pd.DataFrame(dict_learn)
        df_data_m_t = df_data_m.T
        df_data_m_t  = df_data_m_t.drop_duplicates(subset=['Title'], keep='first')
        timezone = pytz.timezone("Asia/Kolkata")
        df_data_m_t['Date'] = pd.to_datetime(df_data_m_t['Date'], errors='coerce')
        df_data_m_t['Date'] = df_data_m_t['Date'].dt.tz_convert('UTC').dt.tz_convert(timezone).dt.strftime('%Y-%m-%d %H:%M:%S')
        df_data_m_t['Date'] = pd.to_datetime(df_data_m_t['Date'], errors='coerce')
        df_learn = df_data_m_t.sort_values(by='Date', ascending=False)
    except Exception as e:
        st.error(f"Microsoft Learn scraping failed: {e}")
        df_learn = pd.DataFrame()

# # Tech Community
# with st.spinner("Fetching Tech Community data..."):
#     try:
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--no-sandbox")
#         service = Service("D:\\Desktop\\AETriage_Tracker\\chromedriver.exe")  # Update path if needed
#         driver = webdriver.Chrome(service=service, options=chrome_options)
#         driver.get("https://techcommunity.microsoft.com/category/windows/discussions/windows11")
#         time.sleep(5)
#         for _ in range(5):
#             try:
#                 show_more = driver.find_element(By.XPATH, '//button[contains(text(), "Show More")]')
#                 if show_more.is_displayed():
#                     driver.execute_script("arguments[0].click();", show_more)
#                     time.sleep(3)
#             except:
#                 break
#         soup = BeautifulSoup(driver.page_source, "html.parser")
#         discussions = soup.find_all("div", class_="MessageViewInline_lia-message__ALtxi")
#         dict_tech = {}
#         for i, disc in enumerate(discussions):
#             title_tag = disc.find("a", class_="MessageViewInline_lia-subject-link__BO63O")
#             date_tag = disc.find("span", title=True)
#             title = title_tag.get_text(strip=True) if title_tag else 'No title'
#             href = title_tag['href'] if title_tag else ''
#             date_str = date_tag['title'] if date_tag else ''
#             dt = datetime.strptime(date_str, "%B %d, %Y at %I:%M %p") if date_str else datetime.now()
#             dict_tech[i] = {
#                 "Date": dt,
#                 "Title": title,
#                 "url": "https://techcommunity.microsoft.com/category/windows" + href,
#                 "Source": "Microsoft Tech Community",
#                 "UpVotes": ""
#             }
#         driver.quit()
#         df_tech = pd.DataFrame(dict_tech)
#         df_tech_t = df_tech.T
#         df_tech_t = df_tech_t.drop_duplicates(subset=['Title'], keep='first')
#         df_tech_t['Date'] = pd.to_datetime(df_tech_t['Date'], errors='coerce')
#         df_tech_t['Date'] = df_tech_t['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        
#     except Exception as e:
#         st.error(f"Tech Community scraping failed: {e}")
#         df_tech = pd.DataFrame()

# Merge & Filter
# df_all = pd.concat([df_reddit, df_learn, df_tech_t], ignore_index=True)
df_all = pd.concat([df_reddit, df_learn], ignore_index=True)
df_all['Title'] = df_all['Title'].astype(str)
df_filtered = df_all[df_all['Title'].str.lower().apply(lambda text: any(k in text for k in keywords))]

# Date filters
cutoff_all = datetime(2025, 1, 1)
cutoff_5days = datetime.now() - timedelta(days=5)
df_n_days = df_filtered[df_filtered['Date'].dt.date >= cutoff_all.date()]
df_5_days = df_n_days[df_n_days['Date'].dt.date >= cutoff_5days.date()]
df_n_days = df_n_days.sort_values(by='Date', ascending=False)
df_5_days = df_5_days.sort_values(by='Date', ascending=False)
df_all = df_all.sort_values(by='Date', ascending=False)
# Display tables
st.subheader("📌 Recent Issues (Last 5 Days)")
st.dataframe(df_5_days, use_container_width=True, hide_index=True)

st.subheader("🗂️ All Filtered Data (Since 2025)")
st.dataframe(df_n_days, use_container_width=True, hide_index=True)

st.subheader("📊 All Collected Data")
st.dataframe(df_all, use_container_width=True, hide_index=True)

# # Download buttons
# def convert_df(df):
#     return df.to_excel(index=False, engine='openpyxl')

# st.download_button("📥 Download All Filtered Data", data=convert_df(df_n_days), file_name="AllFiltered.xlsx")
# st.download_button("📥 Download Last 5 Days Data", data=convert_df(df_5_days), file_name="Last5Days.xlsx")
