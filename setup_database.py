from pymongo import MongoClient
import os
from datetime import datetime

def setup_sample_data():
    """Set up comprehensive sample user data in MongoDB for testing."""
    
    # Connect to MongoDB
    client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
    db = client['resume_builder']
    users = db['users']
    
    # Comprehensive sample user data
    sample_user = {
        '_id': 'demo_user_id',
        'name': 'John Doe',
        'email': 'john.doe@email.com',
        'phone': '+1-555-0123',
        'address': '123 Main Street, Tech City, TC 12345',
        'summary': 'Experienced software engineer with 5+ years in backend development, specializing in Python, cloud infrastructure, and scalable systems. Proven track record of leading teams and delivering high-impact projects.',
        'experience': [
            {
                'title': 'Senior Software Engineer',
                'company': 'TechCorp',
                'duration': '2022-2024',
                'description': 'Led development of microservices architecture, improved system performance by 40%, mentored 3 junior developers, implemented CI/CD pipelines'
            },
            {
                'title': 'Software Engineer',
                'company': 'StartupXYZ',
                'duration': '2020-2022',
                'description': 'Built REST APIs and database systems, designed scalable architecture, mentored junior developers, reduced deployment time by 60%'
            },
            {
                'title': 'Junior Developer',
                'company': 'BigTech',
                'duration': '2019-2020',
                'description': 'Contributed to web applications, learned best practices, participated in code reviews, implemented unit tests'
            }
        ],
        'education': [
            {
                'degree': 'Bachelor of Science in Computer Science',
                'institution': 'University of Technology',
                'year': '2019',
                'gpa': '3.8/4.0'
            },
            {
                'certification': 'AWS Cloud Practitioner',
                'issuer': 'Amazon Web Services',
                'year': '2021',
                'expiry': '2024'
            },
            {
                'certification': 'Python Programming',
                'issuer': 'Python Institute',
                'year': '2020',
                'expiry': '2023'
            }
        ],
        'skills': {
            'programming_languages': ['Python', 'JavaScript', 'TypeScript', 'Java', 'Go'],
            'frameworks': ['Django', 'Flask', 'React', 'Node.js', 'Express'],
            'databases': ['MongoDB', 'PostgreSQL', 'Redis', 'MySQL'],
            'cloud_platforms': ['AWS', 'Google Cloud', 'Azure', 'Docker', 'Kubernetes'],
            'tools': ['Git', 'Jenkins', 'Jira', 'Confluence', 'Postman'],
            'methodologies': ['Agile', 'Scrum', 'CI/CD', 'Microservices', 'REST APIs']
        },
        'projects': [
            {
                'name': 'E-commerce Platform',
                'description': 'Built scalable e-commerce platform serving 10K+ users',
                'technologies': ['Python', 'Django', 'PostgreSQL', 'AWS'],
                'impact': 'Increased sales by 25%'
            },
            {
                'name': 'Real-time Analytics Dashboard',
                'description': 'Developed real-time analytics dashboard for business intelligence',
                'technologies': ['React', 'Node.js', 'MongoDB', 'Socket.io'],
                'impact': 'Improved decision-making speed by 40%'
            }
        ],
        'achievements': [
            'Led team of 5 developers to deliver project 2 weeks ahead of schedule',
            'Reduced system downtime by 90% through improved monitoring',
            'Mentored 3 junior developers who were promoted within 1 year',
            'Received \'Employee of the Year\' award in 2023'
        ],
        'languages': ['English (Native)', 'Spanish (Fluent)', 'French (Intermediate)'],
        'interests': ['Open Source', 'Machine Learning', 'Cloud Architecture', 'System Design'],
        'social_links': {
            'linkedin': 'https://linkedin.com/in/johndoe',
            'github': 'https://github.com/johndoe',
            'portfolio': 'https://johndoe.dev'
        },
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }
    
    # Additional user for testing
    additional_user = {
        '_id': 'user_2',
        'name': 'Sarah Johnson',
        'email': 'sarah.johnson@email.com',
        'phone': '+1-555-0456',
        'summary': 'Frontend developer with 3+ years experience in React and modern web technologies.',
        'experience': [
            {
                'title': 'Frontend Developer',
                'company': 'WebTech Solutions',
                'duration': '2021-2024',
                'description': 'Developed responsive web applications using React, improved user experience scores by 35%'
            }
        ],
        'education': [
            {
                'degree': 'Bachelor of Arts in Web Design',
                'institution': 'Design Institute',
                'year': '2021'
            }
        ],
        'skills': {
            'programming_languages': ['JavaScript', 'TypeScript', 'HTML', 'CSS'],
            'frameworks': ['React', 'Vue.js', 'Angular', 'Next.js'],
            'tools': ['Figma', 'Adobe Creative Suite', 'Git', 'Webpack']
        },
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }
    
    # Insert or update sample users
    users.replace_one({'_id': 'demo_user_id'}, sample_user, upsert=True)
    users.replace_one({'_id': 'user_2'}, additional_user, upsert=True)
    
    print("✅ Sample user data created successfully!")
    print(f"📊 Database: {db.name}")
    print(f"📋 Collection: {users.name}")
    print(f"👤 Users created:")
    print(f"   - {sample_user['name']} (ID: {sample_user['_id']})")
    print(f"   - {additional_user['name']} (ID: {additional_user['_id']})")
    print(f"📧 Emails: {sample_user['email']}, {additional_user['email']}")
    
    # Show database stats
    user_count = users.count_documents({})
    print(f"📈 Total users in database: {user_count}")
    
    client.close()

if __name__ == "__main__":
    setup_sample_data() 