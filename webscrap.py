import requests
from bs4 import BeautifulSoup
import urllib.parse

def google_search(query, num_results=10):
    base_url = "https://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    params = {
        "q": query,
        "num": num_results
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        print("Failed to retrieve results")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.select('.tF2Cxc'):
        title = result.select_one('h3')
        link = result.select_one('a')
        description = result.select_one('.VwiC3b')

        if title and link and description:
            results.append({
                'title': title.get_text(),
                'link': link['href'],
                'description': description.get_text()
            })

    if not results:
        print("No results found")
    return results

def display_results(results):
    print("\nTop Google Search Results:\n")
    for idx, result in enumerate(results, start=1):
        print(f"{idx}. {result['title']}")
        print(f"   Link: {result['link']}")
        print(f"   Description: {result['description']}\n")

def save_results_to_file(results, filename="google_search_results.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Top Google Search Results:\n\n")
        for idx, result in enumerate(results, start=1):
            file.write(f"{idx}. {result['title']}\n")
            file.write(f"   Link: {result['link']}\n")
            file.write(f"   Description: {result['description']}\n\n")
    print(f"Results saved to {filename}")

def main():
    print("Welcome to the Google Search Results Scraper")
    query = input("Enter your search query: ").strip()
    num_results = int(input("Enter the number of results to retrieve (default is 10): ") or 10)

    results = google_search(query, num_results=num_results)

    if results:
        display_results(results)

        save_option = input("Do you want to save the results to a file? (yes/no): ").strip().lower()
        if save_option == "yes":
            filename = input("Enter the filename (default: google_search_results.txt): ").strip()
            if not filename:
                filename = "google_search_results.txt"
            save_results_to_file(results, filename)

if __name__ == "__main__":
    main()
