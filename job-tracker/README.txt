# 🔍 LinkedIn Job Tracker

A Flask web application that fetches live job listings from LinkedIn using the Real-Time LinkedIn Scraper API (via RapidAPI). Users can search for remote internship opportunities by keyword and location.

---

## 🚀 Features

- Real-time job search powered by [linkedin-api8.p.rapidapi.com](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8)
- Filters by:
  - Keyword (e.g., "software internship")
  - Location (`Ireland`, `US`, `UK`, `Germany`, `France`, or `Worldwide`)
- Returns job title, company, location, apply link, and posting date
- Fully responsive frontend (HTML/CSS/JavaScript)
- Deployed-ready with `gunicorn` for Render

---

## 📦 Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **API**: [linkedin-api8 RapidAPI](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8)
- **Testing**: Used Postman to debug parts of the Api's as nothing was being returned on frontend console.
- **Deployment**: Render or any WSGI-compatible service