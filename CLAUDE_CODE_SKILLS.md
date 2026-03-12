# Claude Code Skills Workshop

Learn how to extend Claude Code with custom skills to automate your development workflow.

---

## What is Claude Code Skills?

Skills are **custom commands** that extend Claude Code's capabilities. They let you:
- Define reusable workflows
- Automate repetitive tasks
- Create team conventions
- Share best practices across projects

Skills become available as **slash commands** (e.g., `/analyze`, `/code`, `/workflow`)

---

## How Skills Work

```
You type: /skill-name arguments
           ↓
Claude Code loads the skill
           ↓
Executes with your instructions
           ↓
Returns result
```

---

## Skill File Structure

Skills live in `.claude/skills/` folder:

```
.claude/skills/
├── workflow/
│   └── SKILL.md
├── analyze/
│   └── SKILL.md
├── code/
│   └── SKILL.md
├── test/
│   └── SKILL.md
└── review/
    └── SKILL.md
```

Each skill is a **directory** with `SKILL.md` inside.

---

## SKILL.md Format

```yaml
---
name: skill-name
description: What this skill does
argument-hint: <expected-args>
disable-model-invocation: true
allowed-tools: Tool1,Tool2,Tool3
---

# Skill Title

## Task
$ARGUMENTS

## Steps
1. Do this
2. Do that

## Checklist
- [ ] Step 1
- [ ] Step 2
```

---

## Example: /analyze Skill

```yaml
---
name: analyze
description: Analyze requirements and create plan
argument-hint: <description>
disable-model-invocation: true
allowed-tools: Read,Glob,Grep,TaskUpdate,Skill
---

# Skill: /analyze

Analyze requirements and create detailed implementation plans for Flask backend.

## Task

$ARGUMENTS

## Steps

### 1. Understand Requirements
- Read the task description from $ARGUMENTS
- Ask clarifying questions if needed
- Identify scope: new feature, bug fix, or refactor

### 2. Analyze Codebase
Explore Flask app structure:
- `app/__init__.py` - app factory, config setup
- `app/config.py` - configuration classes
- `app/routes/contacts.py` - API endpoints, current patterns
- `app/utils/validators.py` - existing validators
- `app/utils/helpers.py` - existing helpers

### 3. Design Solution
- Define endpoint (method, URL, params)
- Define request/response format
- Identify helper functions needed
- Identify validators needed
- Consider edge cases and error handling

### 4. Create Implementation Plan
Document:
- Endpoint design (URL, method, params)
- Request/response format
- Files to modify
- Helper functions to add
- Validators to add
- Edge cases to handle
- Potential issues

### 5. Present to User
- Output plan clearly in markdown
- Include code examples if helpful
- Wait for approval

### 6. Complete
- Mark Analysis task done
- Mark Code task in_progress
- Invoke /code skill

## Checklist

- [ ] Understand requirements
- [ ] Ask clarifying questions if needed
- [ ] Identify scope
- [ ] Read relevant source files
- [ ] Analyze existing patterns
- [ ] Design solution
- [ ] Define endpoint design
- [ ] Identify files to modify
- [ ] Identify helper functions needed
- [ ] Consider edge cases
- [ ] Create implementation plan
- [ ] Present plan to user
- [ ] Wait for user approval
```

---

## Complete Skill Set

| Skill | Purpose |
|-------|---------|
| `/analyze` | Analyze requirements and create plan |
| `/code` | Implement code based on plan (routes, helpers, validators) |
| `/test` | Write and run tests to verify implementation |
| `/review` | Code review for quality, security & best practices |
| `/workflow` | Manage full workflow (create tasks, invoke skills) |

### Workflow
```
[Analysis] → [Code] → [Test] → [Review]
     ↓           ↓         ↓
  Understand  Implement  Write tests
  Design      Add helpers  Run tests
  Plan        Verify      Handle results
```

### Each Skill Scope

- `/analyze`: Understand requirements → Analyze codebase → Design solution → Create plan
- `/code`: Read plan → Implement → Update imports → Verify → Complete
- `/test`: Read code → Identify cases → Write tests → Run → Handle results
- `/review`: Review quality → Review security → Review performance → Review tests → Feedback

---

## Advanced Features

### Dynamic Context with `!`command``
```yaml
---
name: pr-summary
---

PR diff: !`gh pr diff`
```

### Run in Subagent with `context: fork`
```yaml
---
name: research
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly...
```

### String Substitutions

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | All arguments passed |
| `$ARGUMENTS[0]` | First argument |
| `$0` | Shorthand for first arg |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_SKILL_DIR}` | Skill directory path |

---

## Best Practices

1. **Keep SKILL.md under 500 lines** - Move details to supporting files
2. **Write clear descriptions** - Help Claude know when to use
3. **Use `disable-model-invocation`** - For workflows you want to control
4. **Define allowed-tools** - Security boundary
5. **Put Steps before Checklist** - Detailed first, summary after

---

## Summary

- Skills = Custom slash commands
- `.claude/skills/<name>/SKILL.md` = Definition
- Frontmatter configures behavior
- Markdown body = Instructions
- `$ARGUMENTS` = User input
- Steps → Checklist

---

## Next Steps

1. Create your first skill in `.claude/skills/`
2. Define your team's conventions
3. Automate repetitive tasks

**Resources:**
- Claude Code Docs: https://code.claude.com/docs/skills

---

# Thank You!

Questions?
