# GitHub Connection Guide

## Quick Setup (3 Steps)

### Option A: Using the Setup Script (Easiest)

```bash
# Run the setup script
setup-github.bat
```

Follow the prompts to enter your repository URL.

---

### Option B: Manual Setup

#### 1. Create Repository on GitHub

1. Go to: https://github.com/new
2. Repository name: `marketing-funnel-project` (or your choice)
3. Visibility: Private or Public
4. **Important:** Do NOT initialize with README, .gitignore, or license
5. Click **Create repository**

#### 2. Connect Local Repository

```bash
# Navigate to project
cd C:\all_proj

# Add GitHub remote (replace with your repo URL)
git remote add origin https://github.com/FAJU85/marketing-funnel-project.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

#### 3. Verify Connection

```bash
# Check remote
git remote -v

# Check status
git status
```

---

## GitHub CLI Alternative

If you have GitHub CLI installed:

```bash
# Create and push in one command
gh repo create marketing-funnel-project --public --source=. --remote=origin --push
```

Install GitHub CLI: https://cli.github.com/

---

## Common Commands

| Command | Description |
|---------|-------------|
| `git status` | Check current status |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit changes |
| `git push` | Push to GitHub |
| `git pull` | Pull from GitHub |
| `git log --oneline` | View commit history |
| `git remote -v` | Show remote URLs |

---

## Authentication

### Using HTTPS (Recommended for most users)

GitHub will prompt for credentials on first push. Use:
- **Username:** Your GitHub username
- **Password:** Personal Access Token (not your GitHub password)

Create a token: https://github.com/settings/tokens

### Using SSH (Advanced)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "ee.ee455@gmail.com"

# Add to GitHub
# 1. Copy key: cat ~/.ssh/id_ed25519.pub
# 2. Go to: https://github.com/settings/keys
# 3. Add new SSH key

# Change remote to SSH
git remote set-url origin git@github.com:FAJU85/marketing-funnel-project.git
```

---

## After Setup

### Making Changes

```bash
# Edit files
# ... make your changes ...

# Stage and commit
git add .
git commit -m "Describe your changes"

# Push to GitHub
git push
```

### Pulling Updates

```bash
# Get latest from GitHub
git pull origin main
```

---

## Troubleshooting

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin YOUR_REPO_URL
```

### "Authentication failed"
- Check your Personal Access Token is valid
- Ensure token has `repo` scope
- Try: `git credential-manager erase` then push again

### "Updates were rejected"
```bash
# Pull first, then push
git pull origin main
git push
```

---

## Your Repository Info

- **Git User:** FAJU85
- **Git Email:** ee.ee455@gmail.com
- **Current Branch:** main
- **Initial Commit:** Done ✅

Next: Create repository at https://github.com/new
