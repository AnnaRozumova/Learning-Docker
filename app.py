import uvicorn
from fastapi import FastAPI, Query
from datetime import datetime, timezone
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World!"}


@app.get("/now")
def get_current_time():
    utc_now = datetime.now(timezone.utc)
    return {"utc_time": utc_now.isoformat()}


@app.get("/search")
async def google_search(q: str = Query(..., description="The search query")):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://www.google.com/search?q={q}")

        soup = BeautifulSoup(response.text, 'html.parser')

        link = soup.find('a', href=True)

        if link:
            first_link = link['href']
            return{"query": q, "first_link": first_link}
        else:
            return{"query": q, "message": "No links found"}
        
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/proxyendpoints/{searched_thing}/{how_many_links}")
async def proxy_endpoint(searched_thing: str, how_many_links: int):
    try:
        # Instantiate httpx.AsyncClient before using it in the context manager
        async with httpx.AsyncClient() as client:
            # Send a GET request to Google with the search query
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
            }
            response = await client.get(f"https://www.google.com/search?q={searched_thing}", headers=headers)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all search result links
        links = soup.find_all('a', href=True)

        # Extract the first `how_many_links` links that look like actual search result links
        found_links = []
        for link in links:
            href = link['href']
            if href.startswith("/url?q="):  # Google's search result links often start with /url?q=
                actual_link = href.split("&")[0].replace("/url?q=", "")
                if actual_link.startswith("http"):  # Ensure it's an actual URL
                    found_links.append(actual_link)

            if len(found_links) == how_many_links:
                break

        if found_links:
            return {"searched_thing": searched_thing, "found_links": found_links}
        else:
            return {"searched_thing": searched_thing, "message": "No valid links found"}

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
