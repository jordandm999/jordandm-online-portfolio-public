# Jordan Morgan's Portfolio Website

A modern portfolio website built with Django and FastAPI, featuring a unique AI-powered chatbot that uses OpenAI's GPT models and the MCP (Model Control Protocol) framework.

## Features

- 🎨 Modern, responsive portfolio design
- 🤖 AI Chatbot powered by OpenAI's GPT models
- 🔧 MCP (Model Control Protocol) integration for extensible AI tools
- 🚀 Kubernetes deployment with AWS ALB Ingress
- 🔒 HTTPS support with automatic SSL/TLS
- ⚡ Fast static file serving with WhiteNoise

## Tech Stack

- **Backend**: Django 5.2, FastAPI
- **AI/ML**: OpenAI API, MCP Framework
- **Deployment**: Docker, Kubernetes, AWS ECR
- **Server**: Gunicorn (WSGI)
- **Dependencies**: Poetry for Python package management

## Local Development

### Prerequisites

- Python 3.10 or higher
- Poetry for dependency management
- Docker for containerization
- AWS CLI configured with appropriate credentials
- kubectl configured with your Kubernetes cluster

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jordandm_online_portfolio.git
   cd jordandm_online_portfolio
   ```

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Run migrations:
   ```bash
   cd src/website
   python manage.py migrate
   ```

### Running Locally

Use the provided Justfile commands:

```bash
# Run the development server
just server

# Activate virtual environment
just virtualenv
```

## Deployment

The project is deployed to Kubernetes using AWS services (ECR, ALB). 

### Prerequisites

- AWS ECR repository
- Kubernetes cluster with ALB Ingress Controller
- Required secrets in Kubernetes:
  - `openai-api-key`
  - `django-secret-key`
  - `regcred` for ECR access

### Deployment Steps

1. Build and push Docker image:
   ```bash
   just deploy
   ```

2. Apply Kubernetes configurations:
   ```bash
   just apply-k8s
   ```

### Infrastructure

- **Docker**: Multi-stage build for optimized images
- **Kubernetes**: 
  - Deployment with 2 replicas
  - NodePort service
  - ALB Ingress for HTTPS
- **Domains**: Configured for jordan-morgan.com and www.jordan-morgan.com

## Project Structure

```
.
├── src/
│   └── website/
│       ├── main/           # Main portfolio app
│       ├── chatbot/        # AI chatbot implementation
│       ├── mcp_server/     # MCP server for AI tools
│       └── website/        # Django project settings
├── k8s/                    # Kubernetes configurations
├── tests/                  # Test suite
├── pyproject.toml         # Poetry dependencies
└── Justfile              # Development commands
```

## Environment Variables

Required environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `DJANGO_SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 