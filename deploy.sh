#!/bin/bash

# FastAPI Cloud Run Deployment Script
# Make sure you have gcloud CLI installed and authenticated

set -e

# Configuration
PROJECT_ID=${1:-"your-project-id"}
SERVICE_NAME="fastapi-backend"
REGION="us-central1"

echo "🚀 Deploying FastAPI to Google Cloud Run..."
echo "Project ID: $PROJECT_ID"
echo "Service Name: $SERVICE_NAME"
echo "Region: $REGION"

# Set the project
gcloud config set project $PROJECT_ID

# Enable required APIs
echo "📋 Enabling required APIs..."
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com

# Build and deploy using Cloud Build
echo "🔨 Building and deploying with Cloud Build..."
gcloud builds submit --config cloudbuild.yaml

echo "✅ Deployment completed!"
echo "🌐 Your API is available at:"
gcloud run services describe $SERVICE_NAME --region=$REGION --format="value(status.url)"

echo ""
echo "📚 API Documentation available at:"
echo "$(gcloud run services describe $SERVICE_NAME --region=$REGION --format="value(status.url)")/docs"