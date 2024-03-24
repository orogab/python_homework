import requests
from bs4 import BeautifulSoup

def scrape_index():
    url = "https://index.hu/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Assuming the structure might have changed, trying a more generic approach:
        # This attempts to fetch any main titles, adjust as necessary.
        titles = soup.find_all(['h1', 'h2', 'h3'])

        extracted_titles = [title.text.strip() for title in titles if 'cikkcim' in title.get('class', [])]

        return extracted_titles
    else:
        print(f"Error: Unable to fetch the content. Status code: {response.status_code}")
        return None

def save_titles_to_file(titles, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(title + '\n')

if __name__ == "__main__":
    titles = scrape_index()

    if titles:
        save_titles_to_file(titles, "orosz_gabor_index.txt")
        print("Titles successfully extracted and saved to 'orosz_gabor_index.txt'")
    else:
        print("Failed to extract titles.")
