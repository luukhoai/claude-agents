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
- `app/routes/contacts.py` - endpoints
- `app/utils/validators.py` - validation
- `app/utils/helpers.py` - helper functions
- `tests/test_contacts.py` - tests

### 2. Review Code Quality
- Check code conventions (naming, formatting)
- Verify consistent response format
- Check for code duplication
- Verify proper error handling with try/except
- Check logging is appropriate

### 3. Review Security
- Verify input validation
- Check for SQL injection (parameterized queries)
- Check for XSS (output sanitization)
- Verify no sensitive data exposure
- Check file upload security

### 4. Review Performance
- Check for N+1 queries
- Verify pagination if applicable
- Check for unnecessary operations

### 5. Review Tests
- Verify test coverage for new features
- Check success case tests
- Check error case tests
- Check edge case tests

### 6. Provide Feedback
- Summarize what is good
- List what needs improvement
- Provide specific suggestions with code examples

### 7. Complete
- Mark Review task done
- Show workflow complete summary

## Checklist

- [ ] Read modified files
- [ ] Review code quality (conventions, formatting, duplication)
- [ ] Review error handling
- [ ] Review security (injection, validation, exposure)
- [ ] Review performance
- [ ] Review test coverage
- [ ] Provide specific feedback
- [ ] Mark Review task done
