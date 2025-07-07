import requests
from bs4 import BeautifulSoup
import os

def crawl_web_content(urls):
    """
    Crawl the given URLs and extract relevant content.
    
    Args:
        urls (list): List of URLs to crawl.
        
    Returns:
        dict: A dictionary containing the crawled content.
    """
    crawled_data = {}
    
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title and paragraphs as an example
            title = soup.title.string if soup.title else 'No Title'
            paragraphs = soup.find_all('p')
            content = ' '.join([para.get_text() for para in paragraphs])
            
            crawled_data[url] = {
                'title': title,
                'content': content
            }
        except requests.exceptions.RequestException as e:
            print(f"Error crawling {url}: {e}")
    
    return crawled_data

def save_crawled_data(data, output_dir='crawled_data'):
    """
    Save the crawled data to text files.
    
    Args:
        data (dict): The crawled data.
        output_dir (str): Directory to save the output files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for url, content in data.items():
        filename = os.path.join(output_dir, f"{url.replace('http://', '').replace('https://', '').replace('/', '_')}.txt")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Title: {content['title']}\n\n")
            f.write(content['content'])

if __name__ == "__main__":
    urls_to_crawl = [
        'https://example.com/catalog',
        'https://example.com/faq',
        # Add more URLs as needed
    ]
    
    crawled_data = crawl_web_content(urls_to_crawl)
    save_crawled_data(crawled_data)