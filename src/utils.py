import os
import json
import requests
import arxiv
from bs4 import BeautifulSoup

from .models import PaperInfo


def get_hugging_face_top_k_daily_papers(k: int) -> list[PaperInfo]:
    try:
        url = "https://huggingface.co/papers"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        containers = soup.find_all('div', class_='SVELTE_HYDRATER contents')
        top_k_papers: list[PaperInfo] = []

        for container in containers:
            data_props = container.get('data-props', '')
            if data_props:
                try:
                    json_data = json.loads(data_props.replace('&quot;', '"'))
                    if 'dailyPapers' in json_data:
                        for paper in json_data['dailyPapers']:
                            paper_info = PaperInfo(
                                title=paper['title'],
                                arxiv_id=paper['paper']['id'],
                                abstract=paper['summary'],
                            )
                            top_k_papers.append(paper_info)
                            if len(top_k_papers) >= k:
                                break
                except json.JSONDecodeError:
                    continue

        return top_k_papers
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching the HTML: {e}")
        return []

def download_papers_by_arxiv_id(arxiv_ids: list[str]) -> None:
    try:
        results = arxiv.Client().results(arxiv.Search(id_list=[*arxiv_ids]))
        for result in results:
            os.makedirs("papers/", exist_ok=True)
            result.download_pdf(dirpath="papers/", filename=f"{result.title}.pdf")
        
    except Exception as e:
        print(f"Error occurred while downloading the paper: {e}")


if __name__ == "__main__":
    print(len(get_hugging_face_top_k_daily_papers(3)))