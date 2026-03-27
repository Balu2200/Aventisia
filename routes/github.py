from fastapi import APIRouter, HTTPException
from services.github import GithubService
from models.schema import IssueCreate, PullRequestCreate
from core.exception import GitHubAPIException


router = APIRouter()
service = GithubService()


@router.get("/repos/{username}")
async def get_repositories(username: str):
    try:
        return await service.get_repo(username)

    except GitHubAPIException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/issues/{owner}/{repo}")
async def get_issues(owner: str, repo: str):
    try:
        return await service.list_issues(owner, repo)

    except GitHubAPIException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/create-issues")
async def create_issues(data: IssueCreate):
    try:
        return await service.create_issue(
            data.owner,
            data.repo,
            data.title,
            data.body
        )

    except GitHubAPIException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/commits/{owner}/{repo}")
async def get_commits(owner: str, repo: str):
    try:
        return await service.get_commits(owner, repo)

    except GitHubAPIException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/create-pull-request")
async def create_pull_request(data: PullRequestCreate):
    try:
        return await service.create_pull_request(
            data.owner,
            data.repo,
            data.title,
            data.head,
            data.base,
            data.body
        )

    except GitHubAPIException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")