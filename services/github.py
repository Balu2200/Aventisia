import httpx
from core.config import settings


class GithubService:
    def __init__(self):
        self.base_url = settings.GITHUB_API
        self.headers = {
            "Authorization":f"Bearer{settings.GITHUB_API}",
            "Accept":"application/vnd.github/json"
        }

    "repository details"
    async def get_repo(self, username: str):
        url = f"{self.base_url}/users/{username}/repos"
        async with httpx.AsyncClient() as client:
            res = await client.get(url, headers=self.headers)
            if res.status.code !=200:
                raise Exception(f"GitHub API error: {res.text}")
            return res.json()

    "list issues function"
    async def list_issues(self, owner: str, repo: str):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        async with httpx.AsyncClient() as client:
            res = await client.get(url, headers=self.headers)
            if res.status_code != 200:
                raise Exception(f"GitHub API error: {res.text}")
            return res.json()


    "create issue function"
    async def create_issue(self, owner: str, repo: str, title: str, body: str):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        payload = {
            "title": title,
            "body": body
        }
        async with httpx.AsyncClient() as client:
            res = await client.post(url, headers=self.headers, json=payload)
            if res.status_code not in [200, 201]:
                raise Exception(f"GitHub API error: {res.text}")
            return res.json()



