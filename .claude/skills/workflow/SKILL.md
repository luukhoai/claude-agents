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
- Create 4 tasks with dependencies
- Mark first task in_progress
- Invoke /analyze skill

### 2. After Analyze
- User approves plan
- Mark #1 done, #2 in_progress
- Invoke /code

### 3. After Code
- Code implementation done
- Mark #2 done, #3 in_progress
- Invoke /test

### 4. After Test
- If pass: mark #3 done, #4 in_progress → invoke /review
- If fail: mark #3 done, #2 in_progress → invoke /code

### 5. After Review
- Mark #4 done
- Show workflow complete summary

## Checklist

- [ ] Create 4 tasks
- [ ] Set dependencies
- [ ] Mark first task in_progress
- [ ] Invoke /analyze skill
- [ ] Track workflow progress
- [ ] Invoke next skill at each step
- [ ] Mark tasks completed

## Usage
```
/workflow start Add DELETE endpoint
/workflow status
/workflow clear
```
