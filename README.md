# AI Therapist

An intelligent conversational AI system designed to provide therapeutic support through advanced natural language processing and machine learning capabilities.

## 🌟 Features

- **Real-time Conversations**: Interactive chat interface with WebSocket support for seamless communication
- **Intelligent Memory Management**: Maintains conversation context and user history across sessions
- **Crisis Detection**: Advanced sentiment analysis and crisis detection using local ML models
- **Scalable Architecture**: Microservices-based design with containerization support
- **Secure & Private**: Enterprise-grade security with Firebase authentication and encrypted data storage

## 🏗️ Architecture

### Tech Stack

**Backend**
- **FastAPI**: High-performance Python web framework for API development
- **Redis**: In-memory data store for session management and caching
- **Celery**: Distributed task queue for background job processing
- **LangChain/LlamaIndex**: Conversation memory management and prompt engineering

**Machine Learning**
- **Gemini**: Primary large language model for conversational AI
- **Hugging Face Transformers**: Local sentiment analysis and crisis detection models

**Frontend**
- **Next.js**: React-based frontend framework
- **WebSockets**: Real-time bidirectional communication

**Infrastructure**
- **Docker**: Containerization for consistent deployment
- **Firebase**: Authentication, cloud functions, and additional cloud services

### System Components

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Next.js UI   │◄──►│   FastAPI API    │◄──►│   Gemini LLM    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        │                        │                        │
        │                        ▼                        │
        │               ┌──────────────────┐              │
        │               │      Redis       │              │
        │               │   (Sessions)     │              │
        │               └──────────────────┘              │
        │                        │                        │
        ▼                        ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Firebase      │    │   Celery Tasks   │    │  HuggingFace    │
│ (Auth & Cloud)  │    │  (Background)    │    │   (Local ML)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- Docker & Docker Compose
- Redis Server
- Firebase Account

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-therapist.git
   cd ai-therapist
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Environment Configuration**
   ```bash
   # Backend (.env)
   cp .env.example .env
   # Configure your environment variables:
   # - GEMINI_API_KEY
   # - REDIS_URL
   # - FIREBASE_CONFIG
   # - CELERY_BROKER_URL
   ```

5. **Docker Setup**
   ```bash
   docker-compose up -d
   ```

### Running the Application

**Development Mode:**

1. **Start Redis & Celery**
   ```bash
   # Terminal 1: Redis
   redis-server
   
   # Terminal 2: Celery Worker
   cd backend
   celery -A app.celery worker --loglevel=info
   ```

2. **Start Backend**
   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Start Frontend**
   ```bash
   cd frontend
   npm run dev
   ```

**Production Mode:**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 📁 Project Structure

```
ai-therapist/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── api/                 # API routes
│   │   ├── core/                # Core configurations
│   │   ├── models/              # Data models
│   │   ├── services/            # Business logic
│   │   │   ├── llm_service.py   # Gemini integration
│   │   │   ├── memory_service.py # LangChain/LlamaIndex
│   │   │   └── ml_service.py    # HuggingFace models
│   │   └── utils/               # Utility functions
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/          # React components
│   │   ├── pages/               # Next.js pages
│   │   ├── hooks/               # Custom hooks
│   │   └── utils/               # Utility functions
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml
└── README.md
```

## 🔧 Configuration

### Environment Variables

**Backend (.env)**
```env
# LLM Configuration
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-pro

# Database
REDIS_URL=redis://localhost:6379/0

# Firebase
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_PRIVATE_KEY=your_private_key
FIREBASE_CLIENT_EMAIL=your_client_email

# Celery
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

# Security
SECRET_KEY=your_secret_key
CORS_ORIGINS=http://localhost:3000
```

**Frontend (.env.local)**
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws
NEXT_PUBLIC_FIREBASE_CONFIG=your_firebase_config
```

## 🛡️ Safety Features

- **Crisis Detection**: Real-time monitoring using sentiment analysis and keyword detection
- **Content Filtering**: Advanced filtering to ensure appropriate therapeutic responses
- **Session Management**: Secure session handling with automatic timeout
- **Data Privacy**: End-to-end encryption and HIPAA-compliant data handling
- **Emergency Protocols**: Automated escalation for high-risk situations

## 📊 API Documentation

Once the backend is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Key Endpoints

```
POST /api/v1/chat/message     # Send message to AI therapist
GET  /api/v1/chat/history     # Retrieve conversation history
POST /api/v1/auth/login       # User authentication
GET  /api/v1/health           # System health check
```

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test

# Integration tests
docker-compose -f docker-compose.test.yml up --abort-on-container-exit
```

## 🚀 Deployment

### Docker Deployment
```bash
# Build and deploy
docker-compose -f docker-compose.prod.yml up -d

# Scale services
docker-compose -f docker-compose.prod.yml up -d --scale api=3
```

### Cloud Deployment
- **Backend**: Deploy FastAPI to cloud platforms (AWS, GCP, Azure)
- **Frontend**: Deploy Next.js to Vercel, Netlify, or similar
- **Database**: Use managed Redis services (AWS ElastiCache, Google Cloud Memory Store)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint and Prettier for JavaScript/TypeScript
- Write comprehensive tests for new features
- Update documentation for API changes
- Ensure all safety checks pass before PR submission

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Ethical Considerations

This AI therapist is designed to provide supportive conversations and is **not a replacement for professional mental health care**. Users experiencing crisis situations should contact emergency services or professional mental health providers immediately.

- **Emergency Contacts**: 988 (Suicide & Crisis Lifeline)
- **Professional Help**: Always recommend consulting licensed therapists for serious mental health concerns
- **Data Privacy**: All conversations are encrypted and stored securely
- **Transparency**: Users are informed they are interacting with an AI system

## 📞 Support

- **Documentation**: [Wiki](https://github.com/yourusername/ai-therapist/wiki)
- **Issues**: [GitHub Issues](https://github.com/yourusername/ai-therapist/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/ai-therapist/discussions)

## 🔄 Roadmap

- [ ] Multi-language support
- [ ] Voice conversation capabilities
- [ ] Advanced analytics dashboard
- [ ] Mobile app development
- [ ] Integration with healthcare providers
- [ ] Advanced ML model fine-tuning

---

**⚠️ Disclaimer**: This AI system is for supportive purposes only and should not replace professional mental health treatment. If you're experiencing a mental health emergency, please contact your local emergency services immediately.
