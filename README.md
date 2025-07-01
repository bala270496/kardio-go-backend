# FastAPI Backend for Google Cloud Run

A production-ready FastAPI backend application designed for deployment on Google Cloud Run.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Cloud Run Ready**: Optimized for Google Cloud Run deployment
- **Structured Architecture**: Clean separation of concerns with services, models, and utilities
- **Auto Documentation**: Interactive API docs with Swagger UI
- **Health Checks**: Built-in health monitoring endpoints
- **CORS Support**: Cross-origin resource sharing enabled
- **Environment Configuration**: Flexible configuration management

## 📁 Project Structure

```
├── app/
│   ├── api/v1/endpoints/    # API route handlers
│   ├── core/                # Core configuration
│   ├── models/              # Pydantic models
│   ├── services/            # Business logic
│   └── utils/               # Utility functions
├── cloudbuild.yaml          # Cloud Build configuration
├── Dockerfile               # Container configuration
├── deploy.sh                # Deployment script
└── requirements.txt         # Python dependencies
```

## 🛠️ Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

3. **Access the API:**
   - API: http://localhost:8000/api/v1/
   - Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/api/v1/health

## ☁️ Cloud Run Deployment

### Prerequisites

1. **Google Cloud SDK**: Install and authenticate
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

2. **Enable APIs**: The deployment script will enable required APIs automatically

### Quick Deployment

1. **Make deployment script executable:**
   ```bash
   chmod +x deploy.sh
   ```

2. **Deploy to Cloud Run:**
   ```bash
   ./deploy.sh YOUR_PROJECT_ID
   ```

### Manual Deployment

1. **Build and push container:**
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/fastapi-backend
   ```

2. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy fastapi-backend \
     --image gcr.io/YOUR_PROJECT_ID/fastapi-backend \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --port 8000 \
     --memory 512Mi \
     --cpu 1
   ```

## 📊 API Endpoints

### Health & Info
- `GET /api/v1/` - API information
- `GET /api/v1/health` - Health check

### Users
- `GET /api/v1/users` - List all users
- `POST /api/v1/users` - Create user
- `GET /api/v1/users/{id}` - Get user by ID
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

### Posts
- `GET /api/v1/posts` - List all posts
- `POST /api/v1/posts` - Create post
- `GET /api/v1/posts/{id}` - Get post by ID
- `PUT /api/v1/posts/{id}` - Update post
- `DELETE /api/v1/posts/{id}` - Delete post

## 🔧 Configuration

Environment variables can be set in Cloud Run:

- `PROJECT_NAME`: Application name
- `PROJECT_DESCRIPTION`: Application description
- `VERSION`: Application version
- `API_V1_STR`: API version prefix
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `ALLOWED_HOSTS`: CORS allowed hosts

## 🏥 Monitoring

- **Health Check**: `/api/v1/health`
- **Metrics**: Available through Google Cloud Monitoring
- **Logs**: Available through Google Cloud Logging

## 🔒 Security

- Non-root user in container
- CORS configuration
- Input validation with Pydantic
- HTTP security headers

## 📈 Scaling

Cloud Run automatically scales based on:
- CPU utilization (60% target)
- Memory usage
- Request concurrency
- Min instances: 0 (scales to zero)
- Max instances: 10

## 🐳 Docker

Build locally:
```bash
docker build -t fastapi-backend .
docker run -p 8000:8000 fastapi-backend
```

## 📝 License

This project is licensed under the MIT License.