# Taiko Web

A modern web-based Taiko no Tatsujin rhythm game simulator built with Flask and JavaScript.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0.3-lightgrey.svg)](https://flask.palletsprojects.com)

## Features

- **Full Taiko Experience**: Complete rhythm game mechanics with authentic gameplay
- **Multiplayer Support**: Real-time multiplayer sessions via WebSocket
- **User Accounts**: Registration, profiles, and score tracking
- **Custom Songs**: Support for custom song imports and management
- **Responsive Design**: Optimized for desktop and mobile browsers
- **Plugin System**: Extensible architecture for custom functionality

## Quick Start

### Prerequisites

- Python 3.7 or higher
- MongoDB (for user data and scores)
- Redis (for sessions and caching)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/L3ne/taiko-web-master.git
   cd taiko-web-master
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the application**
   ```bash
   cp config.example.py config.py
   # Edit config.py with your settings
   ```

4. **Start the services**
   ```bash
   # Start MongoDB and Redis services
   # Then run the application
   python server.py
   ```

5. **Access the game**
   Open your browser and navigate to `http://localhost:5000`

## Configuration

Key configuration options in `config.py`:

- **Database**: MongoDB connection settings
- **Cache**: Redis configuration for sessions
- **Accounts**: Enable/disable user registration
- **Multiplayer**: WebSocket URL for real-time gameplay
- **Assets**: Base URLs for songs and game assets

## Adding Custom Songs

1. Place song files in the appropriate directory structure
2. Ensure proper metadata and difficulty files are included
3. Restart the server to load new songs

## Browser Compatibility

- **Recommended**: Chrome/Chromium (best performance)
- **Supported**: Firefox, Safari, Edge
- **Mobile**: iOS Safari, Chrome Mobile

## Deploy on Vercel

Déploiement serverless sur Vercel (fonctionnalités limitées) :

### Prérequis externes

1. **MongoDB Atlas** : Créer un cluster gratuit sur [mongodb.com](https://mongodb.com)
2. **Upstash Redis** : Créer une base Redis gratuite sur [upstash.com](https://upstash.com)

### Déploiement

1. **Fork ce repository** sur GitHub
2. **Connecte-toi sur [Vercel](https://vercel.com)**
3. **Import ton repository** GitHub
4. **Configure les variables d'environnement** :
   - `MONGODB_URI` : Connection string MongoDB Atlas
   - `MONGODB_DB` : Nom de la base de données
   - `REDIS_URL` : URL Redis d'Upstash
   - `SECRET_KEY` : Clé secrète aléatoire
5. **Deploy** !

### Limitations Vercel

- **Pas de multijoueur** (WebSocket non supporté)
- **Comptes utilisateurs désactivés** (sessions limitées)
- **Timeout 30s** par requête

## Deploy on Railway (Recommandé)

Railway supporte toutes les fonctionnalités :

1. **Fork ce repository** sur GitHub
2. **Connecte-toi sur [Railway](https://railway.app)**
3. **"New Project" → "Deploy from GitHub"**
4. **Ajoute MongoDB et Redis** depuis leur interface
5. **Déploiement automatique** avec toutes les fonctionnalités !

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.