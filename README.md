# End-to-End Social Media Sentiment Scraper with DB, API & Visualizer  
### Reddit-Only MVP Roadmap

**Author:** Sumayer Khan Sajid (ID 2221818642)  
**Course:** CSE299 – Junior Development Project, North South University  
**Status:** 🟢 Environment & Repo Ready 🟠 Building Reddit Collector

---

## 🎯 Goal
Build a minimal, end-to-end pipeline that:
1. Fetches Reddit posts for a given keyword via the official API  
2. Cleans and normalizes text  
3. Applies VADER sentiment analysis  
4. Stores results in a structured database  
5. Serves sentiment summaries through an API and a simple dashboard  

This MVP focuses only on **Reddit**.  
Future versions will add X/Twitter and more platforms.

---

## 🧩 Project Structure
\`\`\`
collector/        → Reddit API fetchers
preprocessing/    → Text cleaning functions
analysis/         → VADER sentiment scripts
database/         → DB schema & connectors
api/              → REST API (Flask/FastAPI)
dashboard/        → Streamlit UI for visualization
utils/            → Config, logger, helpers
data/             → Temporary raw & processed files (ignored by Git)
\`\`\`

---

## ⚙️ Setup

### 1️⃣ Clone & Environment
\`\`\`bash
git clone https://github.com/SumayerKhan/End-to-End_Social_Media_Sentiment_Scraper_DB_API_Visualizer.git
cd End-to-End_Social_Media_Sentiment_Scraper_DB_API_Visualizer
python -m venv venv
source venv/bin/activate     # on Windows: venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

### 2️⃣ Environment Variables (\`.env\`)
Copy \`.env.example\` → \`.env\` and fill in your secrets:

\`\`\`
REDDIT_CLIENT_ID=xxxx
REDDIT_CLIENT_SECRET=xxxx
REDDIT_USER_AGENT=sentiment_scraper:v1.0 (by u/YourUsername)
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=sentiment_db
\`\`\`

---

## 🧠 MVP Workflow
\`\`\`
Keyword → Reddit API → Preprocessing → VADER → Database → API → Dashboard
\`\`\`

| Phase | Goal | Status |
|-------|------|--------|
| Phase 0 | Repo & venv setup | ✅ Done |
| Phase 1 | Reddit collector (fetch + save) | 🔄 In progress |
| Phase 2 | Preprocessing (clean text) | ⏳ Pending |
| Phase 3 | Sentiment (VADER) | ⏳ Pending |
| Phase 4 | Database integration | ⏳ Pending |
| Phase 5 | API + dashboard slice | ⏳ Pending |
| Phase 6 | MVP stabilization & docs | ⏳ Pending |

---

## 🧾 Key Decisions
- **Ethical API access:** Use official Reddit API (PRAW) for data collection.  
- **Model:** VADER (lexicon + rule-based, social-media optimized).  
- **Database:** MySQL or PostgreSQL with three tables – \`raw_posts\`, \`processed_posts\`, \`sentiment_posts\`.  
- **Visualization:** Streamlit dashboard showing daily positive/neutral/negative trends.  

---

## 🧰 Development Notes
- Work on feature branches (\`feature/reddit-collector\`, \`feature/vader-analysis\`, etc.)  
- Merge into \`dev\` after each tested module, then to \`main\` when stable.  
- Keep \`data/\` and \`.env\` out of Git (\`.gitignore\` handles this).  

---

## 🚀 Running the Pipeline (MVP)
1. Activate venv  
2. Run \`collector/reddit_collector.py\` for a keyword  
3. Inspect \`data/raw/reddit_sample.json\` to verify API output  
4. Proceed with preprocessing → VADER → DB insertion  
5. Launch dashboard to view sentiment trend  

---

## 🧭 Next Steps
- ✅ Finish Reddit collector  
- 🧹 Implement text cleaning pipeline  
- 💬 Integrate VADER sentiment scores  
- 🗃️ Design and connect database schema  
- 📈 Build minimal API and dashboard for visual output  

---

## 📄 License & Acknowledgement
For academic use (CSE299 – North South University).  
Uses Reddit API data under their public usage policy.  
VADER sentiment model by Hutto & Gilbert (2014).

---