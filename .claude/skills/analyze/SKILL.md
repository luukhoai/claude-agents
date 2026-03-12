---
name: analyze
description: Analyze requirements and create implementation plan for Flask backend. Use when starting a new feature, adding API endpoint, or fixing bugs that need implementation planning.
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
- `tests/test_contacts.py` - test patterns

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
