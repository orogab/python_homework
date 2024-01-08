import requests
from bs4 import BeautifulSoup

def scrape_index():
    url = "https://index.hu/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h1', class_='cikkcim')

        extracted_titles = [title.text.strip() for title in titles]

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
