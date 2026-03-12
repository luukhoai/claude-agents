---
name: code
description: Implement code based on approved analysis plan. Use when implementing new features, adding endpoints, or fixing bugs after analysis is approved.
argument-hint: <feature-description>
disable-model-invocation: true
allowed-tools: Read,Write,Edit,Glob,Grep,Bash,TaskUpdate,Skill
---

# Skill: /code

Implement code based on approved analysis plans.

## Task

$ARGUMENTS

## Steps

### 1. Implementation
- Read approved plan from conversation
- Implement code changes
- Follow project patterns:
  - Response format: `{ "success": true, "data": {...} }`
  - Blueprint pattern for routes
  - Use existing validators/helpers

### 2. Write Tests
- Add unit tests in `tests/test_contacts.py`
- Test success case
- Test error cases

### 3. Run Tests
- Execute: `venv/bin/python -m pytest tests/ -v`
- Fix any failures

### 4. Complete
- Mark Code task done
- Mark Test task in_progress
- Invoke /test skill

## Checklist

- [ ] Read approved plan
- [ ] Implement new feature/fix
- [ ] Follow project patterns
- [ ] Add error handling
- [ ] Write unit tests
- [ ] Run tests
- [ ] Fix any test failures
- [ ] Run linter
- [ ] Format code

## Files to Modify
- `app/routes/contacts.py` - endpoints
- `app/utils/validators.py` - validation
- `tests/test_contacts.py` - tests

## Commands
```bash
venv/bin/python run.py
venv/bin/python -m pytest tests/ -v
venv/bin/python -m flake8 app/ tests/
venv/bin/python -m black app/ tests/
```
