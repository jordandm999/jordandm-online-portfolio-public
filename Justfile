server:
  #!/usr/bin/env sh
  cd "$(git rev-parse --show-toplevel)/src/website"
  uvicorn src.website.website.asgi:application --reload

virtualenv:
  #!/usr/bin/env sh
  cd "$(git rev-parse --show-toplevel)"
  pwd
  source .venv/bin/activate

  # Justfile for deploying your Django app to ECR and Kubernetes

# Set these variables to match your setup
ECR_REPO := "886149544017.dkr.ecr.us-west-2.amazonaws.com/websites/jordan-online-portfolio"
DEPLOYMENT_NAME := "jordan-online-portfolio"
CONTAINER_NAME := "jordan-online-portfolio"
NAMESPACE := "default"  # Change if you use a different namespace

deploy:
  #!/usr/bin/env sh
  set -eux

  # Get the project root and cd to the Docker context directory
  ROOT="$(git rev-parse --show-toplevel)"
  cd "$ROOT/src/website"

  # Get the current git commit short hash for tagging
  TAG="$(git rev-parse --short HEAD)"

  # Build the Docker image
  echo "Building Docker image with tag: $TAG"
  docker buildx build --platform linux/amd64 -t "${ECR_REPO}:$TAG" .

  # Tag latest (optional, for convenience)
  docker tag "${ECR_REPO}:$TAG" "${ECR_REPO}:latest"

  # Authenticate to ECR
  echo "Logging in to ECR..."
  aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 886149544017.dkr.ecr.us-west-2.amazonaws.com

  # Push both tags
  echo "Pushing Docker images to ECR..."
  docker push "${ECR_REPO}:$TAG"
  docker push "${ECR_REPO}:latest"

  # Set the image in Kubernetes deployment
  echo "Updating Kubernetes deployment..."
  kubectl set image deployment/${DEPLOYMENT_NAME} ${CONTAINER_NAME}=${ECR_REPO}:$TAG -n ${NAMESPACE}

  # Wait for rollout to finish
  kubectl rollout status deployment/${DEPLOYMENT_NAME} -n ${NAMESPACE}

  echo "Deployment complete! Now running image: ${ECR_REPO}:$TAG"
