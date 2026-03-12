---
name: test
description: Write and run tests. Use after code implementation is done.
argument-hint: <feature-description>
disable-model-invocation: true
allowed-tools: Bash,Read,Write,Edit,Glob,Grep,TaskUpdate,Skill
---

# Skill: /test

Write and run tests to verify implementation.

## Task

$ARGUMENTS

## Steps

### 1. Read Implemented Code
- Read the code in `app/routes/contacts.py` to understand what needs testing
- Identify the endpoint logic, parameters, and response formats
- Check what helper functions are used

### 2. Identify Test Cases
Based on the implementation, identify:
- Success cases (valid input, expected behavior)
- Error cases (missing params, invalid format, not found)
- Edge cases (empty values, special characters, case sensitivity)

### 3. Write Tests
- Add unit tests in `tests/test_contacts.py`
- Follow existing test patterns in the file
- Test success cases first
- Test error cases
- Test edge cases

### 4. Run Tests
```bash
.venv/bin/python -m pytest tests/ -v
```

### 5. Handle Results

**If tests pass:**
- Mark Test task done
- Mark Review task in_progress
- Invoke /review skill

**If tests fail:**
- Report failures with details
- Mark Test task done
- Mark Code task in_progress
- Invoke /code skill

## Checklist

- [ ] Read implemented code
- [ ] Identify test cases needed
- [ ] Write success case tests
- [ ] Write error case tests
- [ ] Write edge case tests
- [ ] Run full test suite
- [ ] Verify all tests pass
- [ ] If tests fail - identify and report issues
- [ ] Report results to user
