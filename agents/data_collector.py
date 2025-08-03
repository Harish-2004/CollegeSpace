from pymongo import MongoClient
import os
import json
from typing import Dict, Any, Optional
from datetime import datetime

def serialize_datetime(obj):
    """Convert datetime objects to ISO format strings for CrewAI compatibility."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, dict):
        return {key: serialize_datetime(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [serialize_datetime(item) for item in obj]
    else:
        return obj

def collect_user_data(user_id: str) -> Dict[str, Any]:
    """
    Enhanced data collector for real-world scenarios.
    Retrieves user data from MongoDB with validation and error handling.
    
    Args:
        user_id: The user ID to retrieve data for
        
    Returns:
        Dict containing validated user data
        
    Raises:
        ValueError: If user not found or data is invalid
        ConnectionError: If database connection fails
    """
    try:
        # Connect to MongoDB with error handling
        client = MongoClient(
            os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'),
            serverSelectionTimeoutMS=5000  # 5 second timeout
        )
        
        # Test connection
        client.admin.command('ping')
        
        db = client['resume_builder']
        users = db['users']
        
        # Retrieve user data
        user_data = users.find_one({'_id': user_id})
        
        if not user_data:
            raise ValueError(f"No user found with id {user_id}")
        
        # Remove MongoDB's _id field for LaTeX compatibility
        user_data.pop('_id', None)
        
        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'summary', 'experience', 'education', 'skills']
        missing_fields = [field for field in required_fields if field not in user_data or not user_data[field]]
        
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")
        
        # Ensure data types are correct
        if not isinstance(user_data.get('experience'), list):
            user_data['experience'] = [user_data.get('experience', '')] if user_data.get('experience') else []
        
        if not isinstance(user_data.get('education'), list):
            user_data['education'] = [user_data.get('education', '')] if user_data.get('education') else []
        
        if not isinstance(user_data.get('skills'), list):
            user_data['skills'] = [user_data.get('skills', '')] if user_data.get('skills') else []
        
        # Serialize datetime objects for CrewAI compatibility
        user_data = serialize_datetime(user_data)
        
        # Add metadata for tracking
        user_data['_metadata'] = {
            'retrieved_at': datetime.now().isoformat(),
            'user_id': user_id,
            'data_source': 'mongodb'
        }
        
        return user_data
        
    except Exception as e:
        raise ConnectionError(f"Database connection failed: {str(e)}")
    finally:
        if 'client' in locals():
            client.close()

def validate_job_profile(job_profile: str) -> Dict[str, Any]:
    """
    Validate and parse job profile data.
    
    Args:
        job_profile: Job description or profile text
        
    Returns:
        Dict containing parsed job profile data
    """
    if not job_profile or not job_profile.strip():
        raise ValueError("Job profile cannot be empty")
    
    # Basic validation
    job_data = {
        'description': job_profile.strip(),
        'keywords': [],  # Will be extracted by agents
        'requirements': [],  # Will be extracted by agents
        'company': '',  # Will be extracted by agents
        'position': '',  # Will be extracted by agents
        '_metadata': {
            'validated_at': datetime.now().isoformat()
        }
    }
    
    return job_data 