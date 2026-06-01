import React, { useEffect, useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import io from 'socket.io-client'
import Dashboard from './pages/Dashboard'
import Navigation from './components/Navigation'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function App() {
  const [connected, setConnected] = useState(false)
  const [darkMode, setDarkMode] = useState(true)

  useEffect(() => {
    // Connect to WebSocket for live updates
    const socket = io(API_URL, {
      reconnectionDelay: 1000,
      reconnectionDelayMax: 5000,
      reconnectionAttempts: 5
    })

    socket.on('connect', () => {
      console.log('✓ Connected to live updates')
      setConnected(true)
    })

    socket.on('disconnect', () => {
      console.log('✗ Disconnected from live updates')
      setConnected(false)
    })

    socket.on('error', (error) => {
      console.error('WebSocket error:', error)
    })

    return () => socket.close()
  }, [])

  return (
    <div className={`min-h-screen ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-50 text-gray-900'}`}>
      <Router>
        <Navigation darkMode={darkMode} setDarkMode={setDarkMode} connected={connected} />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<Dashboard />} />
          </Routes>
        </main>
      </Router>
    </div>
  )
}

export default App
