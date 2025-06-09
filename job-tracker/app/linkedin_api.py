import requests


def get_linkedin_jobs(keyword="software internship", location_id="104738515"):
    url = "https://linkedin-api8.p.rapidapi.com/search-jobs"

    querystring = {
        "keywords": keyword,
        "locationId": location_id,
        "datePosted": "pastMonth",
        "sort": "mostRelevant",
        "start": "0"
    }

    headers = {
        "X-RapidAPI-Key": "c0209917fbmshb2904d0694a82cdp1712eajsn3c4d0dfb9173",
        "X-RapidAPI-Host": "linkedin-api8.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            response_data = response.json()

            if not isinstance(response_data.get("data"), list):
                print("API returned unexpected data format")
                return []

            jobs = []
            for item in response_data["data"]:
                try:
                    jobs.append({
                        "title": item.get("title", "No title"),
                        "companyName": item.get("company", {}).get("name", "Unknown company"),
                        "location": item.get("location", "Location not specified"),
                        "jobUrl": item.get("url", "#"),
                        "datePosted": item.get("postAt", "").split(" ")[0]  # Extract just the date
                    })
                except Exception as e:
                    print(f"Skipping malformed job item: {str(e)}")
                    continue

            return jobs
        else:
            print(f"API request failed with status {response.status_code}")
            return {"error": f"API request failed with status {response.status_code}"}

    except Exception as e:
        print(f"Exception while fetching jobs: {str(e)}")
        return {"error": str(e)}