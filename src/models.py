from pydantic import BaseModel

class PaperInfo(BaseModel):
    title: str
    arxiv_id: str
    abstract: str | None = None