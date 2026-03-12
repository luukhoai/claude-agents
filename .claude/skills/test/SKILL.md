---
name: test
description: Run tests to verify implementation. Use after code implementation to check if tests pass.
argument-hint: <feature-description>
disable-model-invocation: true
allowed-tools: Bash,Read,TaskUpdate,Skill
---

# Skill: /test

Run tests to verify the implementation.

## Task

$ARGUMENTS

## Steps

### 1. Run Tests
```bash
venv/bin/python -m pytest tests/ -v
```

### 2. Handle Results

**If tests pass:**
- Mark Test task done
- Mark Review task in_progress
- Invoke /review skill

**If tests fail:**
- Report failures
- Mark Test task done
- Mark Code task in_progress
- Invoke /code skill

## Checklist

- [ ] Run full test suite
- [ ] Verify all tests pass
- [ ] Check test coverage
- [ ] If tests fail - identify issues
- [ ] Report results to user
