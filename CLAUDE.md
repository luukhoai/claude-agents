# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Flask-based contact form REST API** that handles contact form submissions with optional file attachments. It uses an in-memory store for contacts.

## Project-Specific Guidelines

### Endpoint Structure
- Use RESTful conventions for all endpoints
- Return consistent JSON response format: `{ success: boolean, data?: any, error?: string }`
- Include appropriate HTTP status codes (200, 201, 400, 404, 500)

### Error Handling
- Catch and log all exceptions with appropriate context
- Return user-friendly error messages to clients
- Never expose internal error details or stack traces

### Validation
- Validate all input data before processing
- Sanitize user inputs to prevent injection attacks
- Use type hints for all function parameters and return values

### Database Operations
- Use parameterized queries to prevent SQL injection
- Handle connection errors gracefully
- Close connections properly after use

### Logging
- Log all API requests with timestamp and endpoint
- Log errors with full context for debugging
- Avoid logging sensitive user data (passwords, tokens)

## Comprehensive Backend Standards

For complete backend development standards including:
- **OOP/SOLID Principles** - Class design, inheritance, SOLID implementation
- **Database Architecture** - Schema design, migrations, optimization
- **API Architecture** - RESTful design, versioning, documentation
- **Security Architecture** - Authentication, authorization, data protection
- **Performance & Scalability** - Optimization, caching, scaling
- **System Architecture** - Microservices, messaging, monitoring
- **Deployment & DevOps** - Containerization, CI/CD, infrastructure
- **Error Handling & Resilience** - Exception handling, circuit breakers

## Common Commands

```bash
# Run the application
.venv/bin/python run.py

# Run tests
.venv/bin/python -m pytest tests/ -v

# Run a single test
.venv/bin/python -m pytest tests/test_contacts.py::test_submit_contact_success -v

# Run linting
.venv/bin/python -m flake8 app/ tests/

# Format code
.venv/bin/python -m black app/ tests/
```

Note: Always use `.venv/bin/python` (not system python) when running commands in this project.

## Architecture

The app follows the **Flask application factory pattern** with blueprint-based routing:

```
app/
├── __init__.py      # create_app() factory function
├── config.py        # Configuration classes (Config, Development, Testing, Production)
├── routes/
│   └── contacts.py  # Contact API blueprint with endpoints
├── utils/
│   ├── validators.py   # Input validation functions
│   └── helpers.py       # File handling utilities
└── models/
    └── __init__.py     # Model placeholders
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/contacts` | Submit contact form (JSON or multipart/form-data) |
| GET | `/api/contacts` | Get all contacts |
| GET | `/api/contacts/search?q=&field=&sort=&order=` | Search contacts with filtering and sorting |
| GET | `/api/contacts/check-email?email=` | Check if email exists |

### Response Format

All endpoints return JSON in this format:
```json
{ "success": true, "data": {...} }
{ "success": false, "error": "error message" }
```

### Configuration

Configuration is managed through environment variables:
- `FLASK_ENV` - Environment (development/testing/production)
- `UPLOAD_FOLDER` - Path for uploaded files (default: `uploads/`)
- `MAX_FILE_SIZE` - Max upload size in bytes (default: 5MB)
- `ALLOWED_EXTENSIONS` - Set of permitted file extensions

### Key Behaviors

- Duplicate email addresses are rejected (409 status)
- File uploads are validated for extension and size
- Search is case-insensitive and supports filtering by field (name/email/message/all)
- Contacts are stored in-memory in `app.config['CONTACTS_STORE']`
