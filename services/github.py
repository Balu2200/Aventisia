import httpx
from core.config import settings
from core.exception import GitHubAPIException


class GithubService:
    def __init__(self):
        self.base_url = settings.GITHUB_API
        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        }
        self.timeout = httpx.Timeout(10.0)

    async def _request(self, method: str, url: str, json=None):
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.request(
                method,
                url,
                headers=self.headers,
                json=json
            )

        if response.status_code >= 400:
            raise GitHubAPIException(
                status_code=response.status_code,
                detail=response.text
            )

        return response.json()

    # Fetch repositories
    async def get_repo(self, username: str):
        url = f"{self.base_url}/users/{username}/repos"
        return await self._request("GET", url)

    # List issues
    async def list_issues(self, owner: str, repo: str):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        return await self._request("GET", url)

    # Create issue
    async def create_issue(self, owner: str, repo: str, title: str, body: str):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        payload = {
            "title": title,
            "body": body
        }
        return await self._request("POST", url, json=payload)

    # Fetch commits
    async def get_commits(self, owner: str, repo: str):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        return await self._request("GET", url)

    # Create pull request
    async def create_pull_request(
        self,
        owner: str,
        repo: str,
        title: str,
        head: str,
        base: str,
        body: str = ""
    ):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls"
        payload = {
            "title": title,
            "head": head,
            "base": base,
            "body": body
        }
        return await self._request("POST", url, json=payload)