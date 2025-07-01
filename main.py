import os
import uvicorn
from app.main import app
from app.core.config import settings

if __name__ == "__main__":
    # Use PORT environment variable for Cloud Run
    port = int(os.environ.get("PORT", settings.PORT))
    
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=port,
        reload=False,  # Disable reload in production
        workers=1
    )