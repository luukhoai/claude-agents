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

### 2. Analyze Codebase
Explore Flask app:
- `app/__init__.py` - app factory
- `app/config.py` - configuration
- `app/routes/contacts.py` - API endpoints
- `app/utils/*.py` - utilities

### 3. Create Implementation Plan
Include:
- What to build/modify
- Files to change
- Dependencies
- Potential issues
- Implementation approach

### 4. Present to User
- Output plan clearly in markdown
- Wait for approval

### 5. Complete
- Mark Analysis task done
- Mark Code task in_progress
- Invoke /code skill

## Checklist

- [ ] Understand requirements
- [ ] Ask clarifying questions if needed
- [ ] Read relevant source files
- [ ] Identify files to modify
- [ ] Identify dependencies
- [ ] Consider edge cases
- [ ] Create implementation plan
- [ ] Present plan to user
- [ ] Wait for user approval
