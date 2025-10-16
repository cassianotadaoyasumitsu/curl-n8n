# URL Checker Script

A Python script that gets the effective URL from a redirect chain (similar to `curl -w "%{url_effective}"`).

## What it does

- Fetches the final URL after following all redirects from `https://picsum.photos/800/1000`
- Logs the result with timestamps
- Automatically runs every 8 hours via GitHub Actions

## Files

- `script.py` - Main script
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification
- `.github/workflows/scheduled-url-check.yml` - GitHub Actions workflow

## Setup with GitHub Actions

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Add URL checker script with GitHub Actions"
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

### 2. Automatic Scheduling
Once pushed to GitHub, the script will automatically run every 8 hours (at 00:00, 08:00, 16:00 UTC).

### 3. View Results
- Go to your GitHub repository
- Click on "Actions" tab
- View the workflow runs and logs

## Manual Execution

### Local Testing
```bash
python script.py
```

### Manual GitHub Actions Run
- Go to Actions tab in your GitHub repository
- Click on "Scheduled URL Check" workflow
- Click "Run workflow" button
