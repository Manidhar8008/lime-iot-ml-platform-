"""
Automated data collector for Lime vehicles
Fetches real-time vehicle data and stores in database
"""

import requests
import json
from datetime import datetime
from src.data_collection.database import create_database, insert_vehicle, get_daily_stats

LIME_BASE_URL = "https://data.lime.bike/api/partners/v1/gbfs/seattle"
VEHICLE_STATUS_URL = f"{LIME_BASE_URL}/free_bike_status.json"

def collect_vehicles():
    """Collect vehicle data from Lime API and store in database"""
    
    print("🚀 Starting vehicle data collection...")
    print(f"⏰ Collection time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    try:
        # Create database
        conn = create_database()
        
        # Fetch data from API
        response = requests.get(VEHICLE_STATUS_URL, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ API Error: {response.status_code}")
            return False
        
        data = response.json()
        bikes = data.get('data', {}).get('bikes', [])
        
        print(f"📊 Found {len(bikes)} vehicles")
        print(f"Last update: {datetime.fromtimestamp(data.get('last_updated', 0))}")
        print("-" * 60)
        
        # Insert each vehicle into database
        inserted_count = 0
        for bike in bikes:
            success = insert_vehicle(
                bike_id=bike.get('bike_id'),
                lat=bike.get('lat'),
                lon=bike.get('lon'),
                vehicle_type=bike.get('jump_vehicle_type', 'unknown'),
                is_disabled=bike.get('is_disabled', 0),
                is_reserved=bike.get('is_reserved', 0),
                battery=bike.get('jump_ebike_battery_level', 0)
            )
            if success:
                inserted_count += 1
        
        print(f"✅ Successfully inserted: {inserted_count} vehicles")
        
        # Get daily statistics
        stats = get_daily_stats()
        print("-" * 60)
        print("📈 TODAY'S STATISTICS:")
        print(f"   Total: {stats['total']}")
        print(f"   Available: {stats['available']}")
        print(f"   Disabled: {stats['disabled']}")
        print(f"   Reserved: {stats['reserved']}")
        print(f"   Avg Battery: {stats['avg_battery']:.1f}%")
        print("-" * 60)
        
        print("🎉 Collection complete!")
        return True
        
    except Exception as e:
        print(f"❌ Collection error: {e}")
        return False

if __name__ == "__main__":
    collect_vehicles()
