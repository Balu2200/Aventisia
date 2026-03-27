from fastapi import APIRouter, HTTPException

from services.github import GithubService
from models.schema import IssueCreate


router = APIRouter()
service = GithubService()


@router.get("/repos/{username}")
async def get_repositories(username : str):
    try:
        return service.get_repo(username)
    except Exception as e:
        raise HTTPException(status_code=500, details=str(e))



@router.get("/issues/{owner}/{repo}")
async def get_issues(owner : str,  repo: str):
    try:
        return service.list_issues(owner, repo)

    except Exception as e:
        raise HTTPException(status_code=500, details=str(e))


@router.post("/create-issues")
