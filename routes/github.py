from fastapi import APIRouter, HTTPException

from services.github import GithubService
from models.schema import IssueCreate


router = APIRouter()
service = GithubService()


@router.get("/repos/{username}")
async def get_repositories(username : str):
    try:
        return await service.get_repo(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/issues/{owner}/{repo}")
async def get_issues(owner : str,  repo: str):
    try:
        return await service.list_issues(owner, repo)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-issues")
async def create_issues(data : IssueCreate):
    try:
        return await service.create_issue(
            data.owner,
            data.repo,
            data.title,
            data.body
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
