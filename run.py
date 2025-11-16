#!/usr/bin/env python3
"""Run the AI Traffic Management System"""

from app import app

if __name__ == '__main__':
    print("🚀 Starting AI Traffic Management System...")
    print("📍 Server will be available at: http://localhost:5000")
    print("📊 Dashboard: http://localhost:5000")
    print("📈 Analytics: http://localhost:5000/analytics")
    print("\n⚠️  Note: First run will download YOLOv8 model (~6MB)")
    print("🔄 Press Ctrl+C to stop the server\n")
    
    app.run(debug=False, host='0.0.0.0', port=5000)