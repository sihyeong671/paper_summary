from src.utils import (
    get_hugging_face_top_k_daily_papers,
    download_papers_by_arxiv_id
)

def main():
    papers = get_hugging_face_top_k_daily_papers(3)
    download_papers_by_arxiv_id(arxiv_ids=[paper.arxiv_id for paper in papers])



if __name__ == "__main__":
    main()
