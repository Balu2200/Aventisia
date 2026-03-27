from pydantic import BaseModel


class IssueCreate(BaseModel):
    owner : str
    repo : str
    title : str
    body : str


class PullRequestCreate(BaseModel):
    owner: str
    repo: str
    title: str
    head: str
    base: str
    body: str = ""