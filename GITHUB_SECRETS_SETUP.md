# GitHub Secrets Setup for HuggingFace

## Add HF_TOKEN to GitHub Secrets

### Step 1: Get Your HuggingFace Token

1. Go to: https://huggingface.co/settings/tokens
2. Click **New token**
3. Token type: **Write** ⚠️ (required for uploads)
4. Name: `gesso_tesst-github-actions`
5. Click **Generate token**
6. **Copy the token** (starts with `hf_...`)

---

### Step 2: Add Secret to GitHub Repository

1. Go to your repository: https://github.com/FAJU85/gesso_tesst
2. Click **Settings** tab
3. In left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Fill in:
   ```
   Name: HF_TOKEN
   Value: hf_your_token_here (paste your token)
   ```
6. Click **Add secret**

---

### Step 3: Verify Secret Added

Your Secrets page should show:
```
Name: HF_TOKEN
Updated: Just now
```

---

## How It Works

### GitHub Actions Workflow

The workflow file `.github/workflows/sync-to-huggingface.yml` will:

1. **Trigger:** On every push to `main` branch (or manual trigger)
2. **Checkout:** Clone your repository
3. **Install:** Python + huggingface_hub library
4. **Upload:** Files to HuggingFace Space using `HF_TOKEN` secret
5. **Deploy:** Space auto-rebuilds with new files

### Files Synced

| File | Purpose |
|------|---------|
| `volcanic-sand-funnel.html` | Main landing page |
| `volcanic-sand-landing.html` | Alternative page |
| `SPACE_README.md` | Space metadata |
| `README.md` | Documentation |
| `.gitignore` | Git exclusions |

---

## Test the Workflow

### Manual Trigger

1. Go to: https://github.com/FAJU85/gesso_tesst/actions
2. Click workflow: **Sync to HuggingFace Space**
3. Click **Run workflow**
4. Select branch: `main`
5. Click **Run workflow**
6. Watch the logs for upload progress

### Automatic Trigger

```bash
# Make any change
echo "# Test" >> README.md

# Commit and push
git add .
git commit -m "Test HF sync"
git push

# Watch actions tab - workflow runs automatically!
```

---

## Your HuggingFace Space

After first successful sync:

**Space URL:** https://huggingface.co/spaces/FAJU85/gesso-tesst

### If Space Doesn't Exist Yet

Create it first:
1. Go to: https://huggingface.co/new-space
2. Owner: `FAJU85`
3. Space name: `gesso-tesst`
4. SDK: **Static**
5. Visibility: Public or Private
6. Click **Create Space**

Then run the workflow to upload files.

---

## Security Notes

| Practice | Status |
|----------|--------|
| Token in GitHub Secrets | ✅ Secure |
| Token NOT in code/config | ✅ Secure |
| Token NOT committed to git | ✅ Secure |
| Write permission only | ✅ Minimal scope |
| Repository-scoped secret | ✅ Only this repo can use |

### Never Do This ❌

```bash
# DON'T commit token to git
echo "HF_TOKEN=hf_xxx" >> .env  # ❌

# DON'T put token in workflow file
env:
  HF_TOKEN: hf_xxx  # ❌

# DON'T share token publicly
```

### This Is Secure ✅

```yaml
# GitHub Actions reads from secrets
env:
  HF_TOKEN: ${{ secrets.HF_TOKEN }}  # ✅
```

---

## Troubleshooting

### Workflow Fails: "401 Unauthorized"
- Token is invalid or expired
- Create new token with **Write** permission
- Update secret in GitHub Settings

### Workflow Fails: "404 Not Found"
- Space doesn't exist yet
- Create Space at https://huggingface.co/new-space
- Or check space name matches: `FAJU85/gesso-tesst`

### Workflow Fails: "Secret not found"
- Secret name must be exactly `HF_TOKEN` (case-sensitive)
- Check in Settings → Secrets and variables → Actions

### Space Not Updating
- Check workflow logs for errors
- Space may take 1-2 minutes to rebuild
- Clear browser cache and refresh

---

## Summary

```
1. Get HF Token → https://huggingface.co/settings/tokens
2. Add GitHub Secret → Settings → Secrets → New secret (HF_TOKEN)
3. Create HF Space → https://huggingface.co/new-space
4. Push to GitHub → Workflow auto-syncs to Space
5. View Live → https://huggingface.co/spaces/FAJU85/gesso-tesst
```

---

## Your Configuration

| Item | Value |
|------|-------|
| GitHub Repo | https://github.com/FAJU85/gesso_tesst |
| HF Space | https://huggingface.co/spaces/FAJU85/gesso-tesst |
| Secret Name | `HF_TOKEN` |
| Workflow File | `.github/workflows/sync-to-huggingface.yml` |
