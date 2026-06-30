# HuggingFace Connection Guide

## Quick Setup (3 Steps)

### Step 1: Get Your HuggingFace Token

1. Go to: https://huggingface.co/settings/tokens
2. Click **New token**
3. Token type: **Write** (required for uploading rules/data)
4. Name: `gesso_tesst-mcp` (or any name)
5. Click **Generate token**
6. **Copy the token** (starts with `hf_...`)

### Step 2: Authenticate with CLI

```bash
# Login to HuggingFace
hf auth login
```

Paste your token when prompted (it won't show as you type).

### Step 3: Configure Environment

```bash
# Set environment variable (current session)
set HF_TOKEN=hf_your_token_here

# Or set permanently (recommended)
setx HF_TOKEN "hf_your_token_here"
```

---

## What This Enables

With HuggingFace connected, the `ai-rule-learning-mcp` server can:

| Feature | Description |
|---------|-------------|
| **Cloud Backup** | Sync rules and memory to HF dataset |
| **Community Learning** | Contribute to and benefit from shared patterns |
| **Cross-Device Sync** | Access your rules from any machine |
| **Dataset Storage** | Store conversation patterns securely |

---

## MCP Server Configuration

Update your MCP config to use HuggingFace:

### Current Config Location
`C:\Users\user\.goose\mcp.json`

### Add Environment Variable
```json
{
  "mcpServers": {
    "ai-rule-learning-mcp": {
      "command": "python",
      "args": ["-m", "ai_rule_learning_mcp.server"],
      "env": {
        "HF_TOKEN": "hf_your_token_here",
        "ARL_DATASET": "FAJU85/AI_Rule_Learning",
        "ARL_CONTRIBUTE": "true"
      }
    }
  }
}
```

---

## Create Your Dataset (Optional)

If you want your own private dataset:

1. Go to: https://huggingface.co/new-dataset
2. Dataset name: `AI_Rule_Learning`
3. Visibility: Private (recommended)
4. Click **Create Dataset**

Then update `ARL_DATASET` in your config:
```
ARL_DATASET=FAJU85/AI_Rule_Learning
```

---

## Test Connection

```bash
# Test authentication
hf auth whoami

# Should show your username if logged in
```

---

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `HF_TOKEN` | Optional | HuggingFace write token |
| `ARL_DATASET` | Optional | Your HF dataset name |
| `ARL_SESSIONS` | Optional | Session paths to scan |
| `ARL_CONTRIBUTE` | Optional | Enable community contributions (true/false) |

---

## Privacy & Security

- **Token Storage:** Stored locally in `%USERPROFILE%\.huggingface`
- **Data Upload:** Only anonymized gap patterns (no raw text)
- **Dataset Access:** Private by default
- **Community Sharing:** Opt-in only (`ARL_CONTRIBUTE=true`)

---

## Troubleshooting

### "Invalid token"
- Ensure token type is **Write**
- Token starts with `hf_`
- No extra spaces when copying

### "Permission denied"
- Create your own dataset first
- Or use the default community dataset

### "Not logged in"
```bash
# Re-authenticate
hf auth logout
hf auth login
```

---

## Next Steps After Setup

1. ✅ Get token from https://huggingface.co/settings/tokens
2. ✅ Run `hf auth login`
3. ✅ Set `HF_TOKEN` environment variable
4. ✅ Update MCP config
5. ✅ Restart Goose to apply changes

---

## Your Info

- **GitHub:** FAJU85
- **Email:** ee.ee455@gmail.com
- **Suggested HF Username:** FAJU85 (or your actual HF username)
