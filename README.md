# Aventisia

## Setup Instructions

### 1. Create virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```env
GITHUB_TOKEN=your_github_token
GITHUB_API=https://api.github.com
```

---

## How to Run the Project

```powershell
python -m uvicorn main:app --reload
```

If port `8000` is already in use:

```powershell
python -m uvicorn main:app --reload --port 8001
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### 1. Get User Repositories

```
GET /github/repos/{username}
```

Example:

```
/github/repos/octocat
```

---

### 2. List Repository Issues

```
GET /github/issues/{owner}/{repo}
```

Example:

```
/github/issues/octocat/Hello-World
```

---

### 3. Create Issue

```
POST /github/create-issues
```

Request body:

```json
{
  "owner": "octocat",
  "repo": "Hello-World",
  "title": "Bug report",
  "body": "Steps to reproduce..."
}
```

---

### 4. Get Commit History

```
GET /github/commits/{owner}/{repo}
```

Example:

```
/github/commits/octocat/Hello-World
```

---

### 5. Create Pull Request

```
POST /github/create-pull-request
```

Request body:

```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "title": "New Feature",
  "head": "feature-branch",
  "base": "main",
  "body": "Description of changes"
}
```
