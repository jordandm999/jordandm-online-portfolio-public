server:
  #!/usr/bin/env sh
  cd "$(git rev-parse --show-toplevel)/src/website"
  uvicorn src.website.website.asgi:application --reload

virtualenv:
  #!/usr/bin/env sh
  cd "$(git rev-parse --show-toplevel)"
  pwd
  source .venv/bin/activate