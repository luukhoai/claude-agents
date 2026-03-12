---
name: review
description: Review code for quality, security, and best practices. Use after tests pass to perform code review.
argument-hint: <feature-description>
disable-model-invocation: true
allowed-tools: Read,Glob,Grep,TaskUpdate
---

# Skill: /review

Review code for quality, security, and best practices.

## Task

$ARGUMENTS

## Steps

### 1. Read Modified Files
- `app/routes/contacts.py`
- `app/utils/validators.py`
- `app/utils/helpers.py`
- `tests/test_contacts.py`

### 2. Review Code
- Check code conventions
- Verify error handling
- Check security vulnerabilities:
  - SQL injection
  - XSS
  - Input validation
  - No sensitive data exposure
- Check performance
- Verify tests are adequate

### 3. Provide Feedback
- What is good
- What needs improvement
- Specific suggestions

### 4. Complete
- Mark Review task done
- Show workflow complete summary

## Checklist

- [ ] Read modified files
- [ ] Check code conventions
- [ ] Verify error handling
- [ ] Check security vulnerabilities
- [ ] Check performance
- [ ] Verify tests are adequate
- [ ] Provide specific feedback
