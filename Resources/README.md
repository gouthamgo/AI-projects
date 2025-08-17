# 🌐 Data Sources Collection

A curated list of reliable and free data sources for data science, machine learning, research, and analytics projects. Whether you're building a model, doing exploratory analysis, or creating visualizations, this guide helps you find high-quality data.

✨ **Use this repo as a starting point to discover, access, and utilize public data effectively.**

---

## 📚 Table of Contents
- [Why This Repository?](#why-this-repository)
- [Data Sources](#data-sources)
  - [1. Public & Free APIs](#1-public--free-apis)
  - [2. Web Scraping (Ethical Guidelines)](#2-web-scraping-ethical-guidelines)
  - [3. Government & Public Data](#3-government--public-data)
  - [4. Collect Your Own Data](#4-collect-your-own-data)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

---

## 🤔 Why This Repository?

Finding quality, accessible, and legal data is often the first hurdle in any data-driven project. This repository aims to:
- Provide a centralized list of **free and public data sources**.
- Promote **ethical data practices**.
- Help beginners and experts alike jumpstart their projects.

---

## 📁 Data Sources

### 1. Public & Free APIs

| Name | Description | Link |
|------|-------------|------|
| OpenWeatherMap | Real-time weather data | [openweathermap.org/api](https://openweathermap.org/api) |
| News API | Global news headlines | [newsapi.org](https://newsapi.org) |
| TMDb (The Movie DB) | Movies, TV shows, actors | [themoviedb.org/api](https://www.themoviedb.org/documentation/api) |
| CoinGecko | Cryptocurrency data | [coingecko.com/api](https://www.coingecko.com/en/api) |
| NASA Open APIs | Space, images, missions | [api.nasa.gov](https://api.nasa.gov) |
| Google Books | Book metadata | [developers.google.com/books](https://developers.google.com/books) |
| Unsplash | High-res images | [unsplash.com/developers](https://unsplash.com/developers) |
| JSONPlaceholder | Fake REST API for testing | [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) |

📌 **Tip**: Explore [**public-apis/public-apis**](https://github.com/public-apis/public-apis) on GitHub — a massive, community-maintained list of free APIs.

---

### 2. Web Scraping (Ethical Guidelines)

You can extract data from websites, but always:
- ✅ Check `robots.txt` (e.g., `https://example.com/robots.txt`)
- ✅ Review the site’s Terms of Service
- ✅ Avoid aggressive scraping (use delays)
- ✅ Identify your bot with a proper `User-Agent`

#### Sites That Allow Ethical Scraping:
- **Wikipedia** – Use MediaWiki API or BeautifulSoup with caution.
- **IMDb (via AWS Public Dataset)** – Not directly scrapable, but available via AWS.
- **BBC News / Reuters (for research)** – Possible with permission or academic use.
- **Public court records, job boards, real estate listings** – If not rate-limited and publicly accessible.

🔧 Tools: `BeautifulSoup`, `Scrapy`, `Selenium`, `Playwright`

⚠️ **Warning**: Never scrape personal, sensitive, or paywalled data without permission.

---

### 3. Government & Public Data

These sources provide reliable, well-documented datasets across domains.

| Country | Source | Link |
|--------|--------|------|
| United States | Data.gov | [data.gov](https://data.gov) |
| European Union | EU Open Data Portal | [data.europa.eu](https://data.europa.eu) |
| United Kingdom | Data.gov.uk | [data.gov.uk](https://data.gov.uk) |
| Canada | Open Government Portal | [open.canada.ca](https://open.canada.ca) |
| World Bank | Global development data | [data.worldbank.org](https://data.worldbank.org) |
| United Nations | Global statistics | [data.un.org](https://data.un.org) |
| Kaggle Datasets | Community & public datasets | [kaggle.com/datasets](https://www.kaggle.com/datasets) |
| Google Dataset Search | Search engine for datasets | [datasetsearch.research.google.com](https://datasetsearch.research.google.com) |

📁 Common categories: Health, Education, Climate, Transportation, Crime, Census.

---

### 4. Collect Your Own Data

Sometimes the best data is self-collected.

#### Methods:
- **Surveys & Questionnaires**
  - Tools: Google Forms, Typeform, SurveyMonkey
  - Use for: User behavior, opinions, preferences
- **Sensor Data**
  - IoT devices, Raspberry Pi, Arduino
  - Use for: Environmental monitoring, smart systems
- **Mobile/Web Apps**
  - Log user interactions (with consent)
  - Use for: UX research, A/B testing
- **Social Media Listening**
  - Use official APIs (e.g., X/Twitter API, Reddit API)
  - Avoid scraping private content

🔐 Always follow **privacy laws** (GDPR, CCPA) and obtain **informed consent**.

---

## 💡 How to Use

1. **Browse** the sections above to find a data source relevant to your project.
2. **Check access requirements** (API keys, registration, rate limits).
3. **Download or connect** using Python, R, or other tools.
4. **Cite the source** when using data (good practice and often required).

### Example: Fetching Data from JSONPlaceholder
```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data[0])
```

🤝 Contributing
We welcome contributions! If you know a great free data source or want to improve this guide:

Fork the repo
Create a new branch (feature/add-dataset)
Add your changes (with clear descriptions)
Submit a pull request
Please follow the Code of Conduct (if applicable).

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

Note: This repository only links to data sources. We do not host or claim ownership of any dataset. Always comply with the terms of use of the original data providers. 

🙌 Acknowledgments
public-apis/public-apis
Kaggle
data.gov
Open-source community contributors

📌 Happy data hunting! Let’s build smarter, ethical, and impactful projects together. 🚀


---

### ✅ How to Use This README
1. Save this as `README.md` in your GitHub repository.
2. Optionally, add subfolders like:
   - `/datasets/` – for sample data
   - `/notebooks/` – for Jupyter examples
   - `/scripts/` – for scraping or API fetching code
3. Add a `LICENSE` file (e.g., MIT) if you want to open-source the repo.

Let me know if you’d like a version with badges, icons, or in another language!