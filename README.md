# Aventisia

A small FastAPI service that connects to the GitHub REST API. The app currently supports:

- Listing public repositories for a GitHub user
- Listing issues for a repository
- Creating a new issue in a repository

## Tech Stack

- Python
- FastAPI
- Uvicorn
- HTTPX
- python-dotenv

## Project Structure

```text
Aventitia/
|-- core/
|   `-- config.py
|-- models/
|   `-- schema.py
|-- routes/
|   `-- github.py
|-- services/
|   `-- github.py
|-- .env
|-- main.py
`-- requirements.txt
```

## How It Works

- [main.py](d:\Web-Development\Aventitia\main.py) creates the FastAPI app and registers the GitHub router under `/github`.
- [routes/github.py](d:\Web-Development\Aventitia\routes\github.py) defines the API endpoints.
- [services/github.py](d:\Web-Development\Aventitia\services\github.py) handles outbound requests to GitHub using `httpx.AsyncClient`.
- [models/schema.py](d:\Web-Development\Aventitia\models\schema.py) defines the request body schema for issue creation.
- [core/config.py](d:\Web-Development\Aventitia\core\config.py) loads environment variables from `.env`.

## Requirements

Create a `.env` file with:

```env
GITHUB_TOKEN=your_github_token
GITHUB_API=https://api.github.com
```

Notes:

- `GITHUB_TOKEN` is required for creating issues.
- `GITHUB_API` should normally stay as `https://api.github.com`.

## Installation

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run The App

```powershell
.\.venv\Scripts\Activate.ps1
python -m uvicorn main:app --reload
```

If port `8000` is already in use:

```powershell
python -m uvicorn main:app --reload --port 8001
```

Swagger UI will be available at:

```text
http://127.0.0.1:8000/docs
```

or, if using port `8001`:

```text
http://127.0.0.1:8001/docs
```

## API Endpoints

### 1. List User Repositories

`GET /github/repos/{username}`

Example:

```text
/github/repos/octocat
```

Returns the repositories for the given GitHub username.

### 2. List Repository Issues

`GET /github/issues/{owner}/{repo}`

Example:

```text
/github/issues/octocat/Hello-World
```

Returns the issues for the selected repository.

### 3. Create Issue

`POST /github/create-issues`

Request body:

```json
{
  "owner": "octocat",
  "repo": "Hello-World",
  "title": "Bug report",
  "body": "Steps to reproduce..."
}
```

Returns the created GitHub issue response.

## Future Improvements

- Validate that required environment variables exist at startup
- Add response models and stronger request validation
- Add tests for routes and service methods
- Improve error handling for GitHub API responses
- Rename `create-issues` to `create-issue` for consistency
