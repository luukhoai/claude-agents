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

### 1. Read Plan & Analyze
- Read approved plan from conversation
- Identify files to modify
- Check existing code patterns in those files
- Determine if new helper functions are needed

### 2. Implement Code
- Add new endpoints/routes in `app/routes/contacts.py`
- Add new helper functions in `app/utils/helpers.py` if needed
- Add new validators in `app/utils/validators.py` if needed
- Follow project patterns:
  - Response format: `{ "success": true, "data": {...} }`
  - Blueprint pattern for routes
  - Use existing validators/helpers
  - Add proper error handling with try/except
  - Include logging

### 3. Update Imports
- Ensure all new functions are properly imported
- Remove any unused imports

### 4. Verify Code
- Run app to verify it starts without errors
- Run linter to check code quality

### 5. Complete
- Mark Code task done
- Mark Test task in_progress
- Invoke /test skill

## Checklist

- [ ] Read approved plan
- [ ] Analyze existing code patterns
- [ ] Implement new feature/fix
- [ ] Add helper functions in helpers.py if needed
- [ ] Add validators in validators.py if needed
- [ ] Update imports
- [ ] Follow project patterns
- [ ] Add error handling with try/except
- [ ] Add logging
- [ ] Verify app starts
- [ ] Run linter

## Files to Modify
- `app/routes/contacts.py` - endpoints
- `app/utils/validators.py` - validation
- `app/utils/helpers.py` - helper functions

## Commands
```bash
.venv/bin/python run.py
.venv/bin/python -m flake8 app/
```
