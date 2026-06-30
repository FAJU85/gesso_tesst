# MCP Servers Configuration for Goose

This document describes the MCP (Model Context Protocol) servers configured for your Goose environment.

## Installed MCP Servers

### 1. agileforagents (v0.3.8)

**Purpose:** Transform project ideas into verified, sprint-ready agile task boards.

**Available Tools:**
| Tool | Description |
|------|-------------|
| `generate_agile_tasks` | Convert any project idea into a verified agile task board with sprints, assumptions, and done criteria |
| `get_agent_rules` | Return the AgileForAgents working protocol for use in agent system prompts |
| `feedback_stats` | Get usage statistics for generated agile boards |

**Usage Example:**
```python
# Generate an agile task board
result = await mcp_client.call_tool(
    "generate_agile_tasks",
    {
        "prompt": "Build a REST API for a todo app with user authentication",
        "format": "claude",  # or "json" or "cursor"
        "detail_level": "standard"  # or "detailed"
    }
)
```

**Configuration:**
- **Command:** `python -m agileforagents.server`
- **Config File:** `C:\Users\user\.goose\mcp.json`
- **License:** MIT

---

### 2. ai-rule-learning-mcp (v0.2.0)

**Purpose:** Learn guardrail rules from AI conversations and inject them automatically into all AI agent configs.

**Available Tools:**
| Tool | Description |
|------|-------------|
| `get_guardrail_rules` | Load personal guardrail rules at session start |
| `record_feedback` | Record corrections/preferences to generate rules in real-time |
| `sync_sessions` | Analyze session history to detect patterns and generate rules |
| `remember` | Persist facts/preferences for future sessions |
| `recall` | Load all persisted memories |
| `install_scheduler` | Set up nightly automatic sync at 02:00 |
| `list_providers` | Show detected AI agents and session sources |
| `save_skill` | Save reusable workflow procedures |
| `list_skills` | List all saved skills |
| `get_skill` | Load full steps for a saved skill |
| `analyze` | Analyze rules, session health, injection attacks, effectiveness |
| `update_community_knowledge` | Contribute to and benefit from community learning |

**Usage Examples:**

```python
# Record feedback to create a rule
await mcp_client.call_tool(
    "record_feedback",
    {
        "feedback_type": "preference",
        "description": "User prefers concise responses without unnecessary explanations",
        "rule_hint": "Always provide direct answers first, then offer additional details if asked"
    }
)

# Remember a fact about the user
await mcp_client.call_tool(
    "remember",
    {
        "type": "context",
        "content": "User works with Python 3.11, TypeScript, and prefers FastAPI for backends"
    }
)

# Recall all memories at session start
memories = await mcp_client.call_tool("recall", {})

# Save a reusable skill
await mcp_client.call_tool(
    "save_skill",
    {
        "name": "Deploy to Hugging Face",
        "description": "Deploy a machine learning model to Hugging Face Spaces",
        "steps": "1. Create requirements.txt\n2. Create app.py...\n3. Push to HF...",
        "triggers": ["deploy", "hugging face", "hf spaces"]
    }
)
```

**Configuration:**
- **Command:** `python -m ai_rule_learning_mcp.server`
- **Config File:** `C:\Users\user\.goose\mcp.json`
- **Environment Variables:**
  - `ARL_SESSIONS`: Session paths to scan (default: `~/.claude/projects`)
  - `ARL_CONTRIBUTE`: Enable community contributions (default: `false`)
  - `HF_TOKEN`: HuggingFace token for cloud backup (optional)
- **License:** Source Available (free for personal use)

---

## Configuration File Location

**Goose MCP Config:** `C:\Users\user\.goose\mcp.json`

```json
{
  "mcpServers": {
    "agileforagents": {
      "command": "python",
      "args": ["-m", "agileforagents.server"]
    },
    "ai-rule-learning-mcp": {
      "command": "python",
      "args": ["-m", "ai_rule_learning_mcp.server"],
      "env": {
        "ARL_SESSIONS": "C:\\Users\\user\\.claude\\projects",
        "ARL_CONTRIBUTE": "false"
      }
    }
  }
}
```

---

## Testing

Run the test suite to verify both servers are working:

```bash
cd C:\all_proj
python test_mcp_servers.py
```

Expected output:
```
[PASS]: agileforagents
[PASS]: ai-rule-learning-mcp
All tests passed!
```

---

## Integration with planning-with-files Skill

These MCP servers work seamlessly with the `planning-with-files` skill:

1. **Start a project** with `init-session.sh` to create planning files
2. **Use agileforagents** to generate task boards from project ideas
3. **Use ai-rule-learning-mcp** to:
   - Record feedback during development
   - Save skills for repeated workflows
   - Remember project context across sessions
4. **Planning files** persist all decisions and progress on disk

### Example Workflow

```bash
# 1. Initialize planning for a new project
cd my-project
sh ~/.agents/skills/planning-with-files/scripts/init-session.sh "API Development"

# 2. Use agileforagents to generate task board
# (Call generate_agile_tasks via MCP)

# 3. During development, record preferences
# (Call record_feedback via MCP when AI makes mistakes)

# 4. Save reusable procedures
# (Call save_skill via MCP for common workflows)

# 5. Planning files track all progress on disk
# task_plan.md, findings.md, progress.md
```

---

## Troubleshooting

### Server Not Starting

1. Check Python is in PATH: `python --version`
2. Verify packages installed: `pip show agileforagents ai-rule-learning-mcp`
3. Test manually: `python -m agileforagents.server`

### Tools Not Available

1. Check config file syntax: `cat C:\Users\user\.goose\mcp.json`
2. Restart Goose to reload MCP configuration
3. Verify server modules load: `python -c "from agileforagents.server import app"`

### Memory/Rules Not Persisting

1. Check session paths exist: `dir C:\Users\user\.claude\projects`
2. Verify write permissions in agent config directories
3. Run `sync_sessions` to force a sync

---

## Security Notes

- **agileforagents:** Runs locally, no external API calls required
- **ai-rule-learning-mcp:** 
  - Works offline by default
  - Community contribution is opt-in (`ARL_CONTRIBUTE=false`)
  - Only anonymized gap patterns are shared (no raw text)
  - HF token required only for cloud backup

---

## Resources

- **agileforagents:** https://pypi.org/project/agileforagents/
- **ai-rule-learning-mcp:** https://github.com/faju85/ai_rule_learning
- **MCP Protocol:** https://modelcontextprotocol.io/
- **planning-with-files:** https://github.com/OthmanAdi/planning-with-files
