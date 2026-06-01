# Sports Betting Intelligence Dashboard

A comprehensive, production-ready sports betting analysis platform with live odds updates, AI-powered probability models, and prediction market tracking.

## Features

- **Live Odds Integration**: Real-time odds from multiple sportsbooks
- **Advanced Statistical Models**: ELO-based predictions for NBA, NFL, UFC, and Boxing
- **Prediction Markets**: Polymarket tracking with live pricing
- **Expected Value Analysis**: Automatic EV calculations and Kelly Criterion sizing
- **WebSocket Live Updates**: Real-time score updates without page refresh
- **Responsive Design**: Mobile-optimized interface
- **Dark Mode**: Eye-friendly dark theme for extended viewing

## Tech Stack

### Backend
- **Python 3.11+** with FastAPI
- **PostgreSQL** for persistent storage
- **Redis** for caching and live updates
- **WebSockets** for real-time data
- **Celery** for background tasks

### Frontend
- **React 18** with TypeScript
- **TailwindCSS** for styling
- **Socket.io** for real-time updates
- **Recharts** for data visualization
- **Zustand** for state management

## Quick Start

### Prerequisites
```bash
Python 3.11+
Node.js 18+
PostgreSQL 14+
Redis 7+
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your API keys

# Run migrations
alembic upgrade head

# Start server
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Docker Setup
```bash
docker-compose up -d
```

## API Keys Required

1. **The Odds API** - https://the-odds-api.com (free: 500 req/month)
2. **ESPN API** - Free, unofficial
3. **Polymarket API** - Free

## Architecture

```
┌─────────────────────────────────────────────┐
│         Frontend (React + TypeScript)       │
│   WebSocket listeners for live updates      │
└────────────────┬────────────────────────────┘
                 │ REST API + WebSocket
┌────────────────▼────────────────────────────┐
│      Backend (FastAPI + Python)             │
│  • Odds fetching & caching (Redis)         │
│  • Statistical models & calculations        │
│  • WebSocket broadcast for live data        │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│   Data Layer (PostgreSQL + Redis)           │
│  • Persistent storage                       │
│  • Live odds cache                          │
│  • User preferences                         │
└─────────────────────────────────────────────┘
```

## Project Structure

```
sports-betting/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── nba.py
│   │   │   ├── ufc.py
│   │   │   ├── boxing.py
│   │   │   ├── nfl.py
│   │   │   └── polymarket.py
│   │   ├── models/
│   │   │   ├── nba_model.py
│   │   │   ├── ufc_model.py
│   │   │   ├── boxing_model.py
│   │   │   └── nfl_model.py
│   │   ├── services/
│   │   │   ├── odds_service.py
│   │   │   ├── cache_service.py
│   │   │   └── websocket_service.py
│   │   ├── database/
│   │   │   ├── models.py
│   │   │   └── session.py
│   │   └── main.py
│   ├── migrations/
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── store/
│   │   ├── services/
│   │   └── types/
│   ├── public/
│   ├── package.json
│   ├── tailwind.config.js
│   ├── Dockerfile
│   └── .env.example
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Key Improvements Over Original

### Bug Fixes
✅ Fixed EV calculation formula (was missing parentheses)
✅ Added error handling for missing API data
✅ Fixed Poisson probability edge cases (division by zero)
✅ Added timeout protection for all API calls
✅ Fixed type hints and validation

### Performance
✅ Redis caching for odds and scores
✅ Database connection pooling
✅ Lazy loading of market data
✅ Debounced WebSocket updates
✅ CDN-ready frontend assets

### Features
✅ Real-time live updates without refresh
✅ User accounts with saved bets
✅ Bet tracking and ROI calculations
✅ Advanced filtering and sorting
✅ Mobile-responsive design
✅ Dark mode toggle
✅ Export functionality (CSV, PDF)

### Reliability
✅ Circuit breaker pattern for external APIs
✅ Graceful degradation when APIs fail
✅ Comprehensive error logging
✅ Health checks and monitoring
✅ Rate limiting and throttling

## Testing

```bash
# Backend tests
cd backend
pytest -v

# Frontend tests
cd frontend
npm test

# Integration tests
cd backend
pytest tests/integration/ -v
```

## Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for:
- AWS deployment
- DigitalOcean deployment
- GCP deployment
- GitHub Actions CI/CD

## License

MIT

## Disclaimer

⚠️ **For educational and research purposes only**. This tool provides analysis based on statistical models. All probabilities are estimates. Gambling involves risk. Please gamble responsibly and verify odds before placing bets.

## Support

Open an issue on GitHub for bugs and feature requests.
