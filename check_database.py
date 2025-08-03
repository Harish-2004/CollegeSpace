"""
Check and display database contents for verification.
"""

from pymongo import MongoClient
import os
import json
from datetime import datetime

def check_database():
    """Check and display current database contents."""
    
    try:
        # Connect to MongoDB
        client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
        db = client['resume_builder']
        users = db['users']
        
        print("🔍 Checking Database Contents...")
        print(f"📊 Database: {db.name}")
        print(f"📋 Collection: {users.name}")
        
        # Count total documents
        total_users = users.count_documents({})
        print(f"📈 Total users: {total_users}")
        
        if total_users == 0:
            print("❌ No users found in database!")
            print("💡 Run 'python setup_database.py' to create sample data")
            return
        
        # Display all users
        print("\n👥 Users in Database:")
        print("=" * 50)
        
        for user in users.find():
            print(f"\n🆔 User ID: {user['_id']}")
            print(f"👤 Name: {user['name']}")
            print(f"📧 Email: {user['email']}")
            print(f"📱 Phone: {user['phone']}")
            print(f"📝 Summary: {user['summary'][:100]}...")
            
            # Show experience count
            if 'experience' in user:
                exp_count = len(user['experience'])
                print(f"💼 Experience: {exp_count} positions")
                for i, exp in enumerate(user['experience'][:2], 1):  # Show first 2
                    if isinstance(exp, dict):
                        print(f"   {i}. {exp.get('title', 'N/A')} at {exp.get('company', 'N/A')}")
                    else:
                        print(f"   {i}. {exp}")
            
            # Show education count
            if 'education' in user:
                edu_count = len(user['education'])
                print(f"🎓 Education: {edu_count} entries")
            
            # Show skills count
            if 'skills' in user:
                if isinstance(user['skills'], dict):
                    total_skills = sum(len(skills) for skills in user['skills'].values())
                    print(f"🛠️ Skills: {total_skills} total skills across categories")
                else:
                    print(f"🛠️ Skills: {len(user['skills'])} skills")
            
            # Show projects count
            if 'projects' in user:
                print(f"🚀 Projects: {len(user['projects'])} projects")
            
            # Show achievements count
            if 'achievements' in user:
                print(f"🏆 Achievements: {len(user['achievements'])} achievements")
            
            print("-" * 50)
        
        # Test data retrieval
        print("\n🧪 Testing Data Retrieval...")
        try:
            demo_user = users.find_one({'_id': 'demo_user_id'})
            if demo_user:
                print("✅ Demo user found successfully")
                print(f"   Name: {demo_user['name']}")
                print(f"   Email: {demo_user['email']}")
            else:
                print("❌ Demo user not found")
        except Exception as e:
            print(f"❌ Error retrieving demo user: {e}")
        
        print("\n✅ Database check completed!")
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("💡 Make sure MongoDB is running: mongod")
    
    finally:
        if 'client' in locals():
            client.close()

def export_sample_data():
    """Export current database data to JSON file."""
    
    try:
        client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
        db = client['resume_builder']
        users = db['users']
        
        # Get all users
        all_users = list(users.find())
        
        # Convert ObjectId to string for JSON serialization
        for user in all_users:
            user['_id'] = str(user['_id'])
            if 'created_at' in user:
                user['created_at'] = user['created_at'].isoformat()
            if 'updated_at' in user:
                user['updated_at'] = user['updated_at'].isoformat()
        
        # Export to JSON
        export_data = {
            'database_name': db.name,
            'collection_name': users.name,
            'export_date': datetime.now().isoformat(),
            'users': all_users
        }
        
        with open('database_export.json', 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print("📤 Database exported to 'database_export.json'")
        
    except Exception as e:
        print(f"❌ Export failed: {e}")
    
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    check_database()
    
    # Ask if user wants to export data
    response = input("\n📤 Export database to JSON? (y/n): ").lower()
    if response == 'y':
        export_sample_data() 