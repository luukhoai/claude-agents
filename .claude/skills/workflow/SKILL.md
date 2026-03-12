---
name: workflow
description: Manage the dev-workflow (create tasks and invoke skills). Use when starting a new feature or bug fix that requires analysis, implementation, testing, and review.
argument-hint: <command>
disable-model-invocation: true
allowed-tools: TaskCreate,TaskUpdate,TaskList,Skill
---

# Skill: /workflow

Manage the dev-workflow: create tasks and invoke skills.

## Commands

### /workflow start
Start workflow: create tasks and invoke /analyze

### /workflow status
Show workflow status: TaskList

### /workflow clear
Clear all tasks

## Workflow Flow
```
[Analysis] → [Code] → [Test] → [Review]
```

## Steps

### 1. Start Workflow
- Parse the task description from arguments
- Create 4 tasks:
  - Task 1: Analyze requirements
  - Task 2: Implement code
  - Task 3: Write and run tests
  - Task 4: Review code
- Set dependencies (2→3→4, 3→4)
- Mark first task in_progress
- Invoke /analyze skill with task description

### 2. After Analyze ( plan)
- MarkUser approves Task #1 (Analyze) done
- Mark Task #2 (Code) in_progress
- Invoke /code skill

### 3. After Code (Implementation done)
- Mark Task #2 (Code) done
- Mark Task #3 (Test) in_progress
- Invoke /test skill

### 4. After Test (Tests pass/fail)
**If tests pass:**
- Mark Task #3 (Test) done
- Mark Task #4 (Review) in_progress
- Invoke /review skill

**If tests fail:**
- Report failures
- Mark Task #3 (Test) done
- Mark Task #2 (Code) in_progress
- Invoke /code skill to fix issues

### 5. After Review
- Mark Task #4 (Review) done
- Show workflow complete summary

## Checklist

- [ ] Parse task description
- [ ] Create 4 tasks with proper names
- [ ] Set task dependencies
- [ ] Mark first task in_progress
- [ ] Invoke /analyze skill
- [ ] Track workflow progress
- [ ] Invoke /code after analyze approved
- [ ] Invoke /test after code done
- [ ] Handle test failures (re-invoke /code)
- [ ] Invoke /review after tests pass
- [ ] Mark all tasks completed

## Usage
```
/workflow start Add DELETE endpoint
/workflow status
/workflow clear
```
