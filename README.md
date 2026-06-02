# LAF AI

AI-Powered Content Generation Platform built with Flask and OpenRouter.

## Overview

LAF AI helps businesses generate:

- Marketing Captions
- Hashtags
- Content Ideas

using modern Large Language Models through OpenRouter.

The system is designed using a service-oriented architecture to improve maintainability, scalability, and testing.

---

## Features

### AI Content Generation

Generate:

- Captions
- Hashtags
- Marketing Ideas

### Multiple AI Modes

- Creative
- Professional
- Minimal
- Viral

### Audience-Aware Content

Generate content for:

- Students
- Families
- Professionals
- Tourists

### Language Styles

- English
- Japanese Style

### Analytics

Track:

- Generation Count
- Last Audience
- Last Business

### Export

Download generated content as text.

---

## Architecture

LAF AI follows a modular service architecture.

User
↓
Flask Application
↓
Validation Service
↓
Prompt Service
↓
Provider Layer
↓
OpenRouter API
↓
Parsing Service
↓
Response Schema
↓
Frontend

---

## Folder Structure

```text
LAF-AI/

app.py

config.py

ai_engine.py

analytics.py

content_engine.py

services/

├── validation_service.py

├── prompt_service.py

├── parsing_service.py

├── logging_service.py

models/

├── response_schema.py

static/

├── style.css

├── script.js

templates/

├── index.html

logs/

tests/
```

## Installation

```bash
git clone <repository-url>

cd LAF-AI

pip install -r requirements.txt
```

## Environment Variables

Create:

```env
OPENROUTER_API_KEY=your_key_here

SECRET_KEY=your_secret
```

## Run

```bash
python app.py
```

Application:

```text
http://127.0.0.1:5000
```

---

## Technologies

- Python
- Flask
- OpenRouter
- HTML
- CSS
- JavaScript

---

## Future Improvements

- Docker
- CI/CD
- Unit Testing
- Multiple AI Providers
- User Authentication
- Cloud Deployment

---

## Author

Lia Aleen Irshad