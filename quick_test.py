"""
Quick test to verify all components are working.
"""

import os
import sys

def test_components():
    """Test all components of the agentic AI system."""
    
    print("🧪 Testing Agentic AI Components...")
    
    # Test 1: Import dependencies
    try:
        from agents.data_collector import collect_user_data, validate_job_profile
        print("✅ Data collector imported successfully")
    except Exception as e:
        print(f"❌ Data collector import failed: {e}")
        return False
    
    # Test 2: Import LaTeX components
    try:
        from agents.latex_generator import generate_latex_resume
        from agents.compiler import compile_latex_to_pdf
        print("✅ LaTeX components imported successfully")
    except Exception as e:
        print(f"❌ LaTeX components import failed: {e}")
        return False
    
    # Test 3: Import CrewAI components
    try:
        from agents.crew_agents import profile_analyzer, resume_writer
        from agents.crew_tasks import analyze_profile_task, write_resume_task
        from agents.crew_crew import resume_crew
        print("✅ CrewAI components imported successfully")
    except Exception as e:
        print(f"❌ CrewAI components import failed: {e}")
        return False
    
    # Test 4: Test database connection
    try:
        user_data = collect_user_data("demo_user_id")
        print(f"✅ Database connection successful - User: {user_data['name']}")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("💡 Make sure MongoDB is running: mongod")
        return False
    
    # Test 5: Test job profile validation
    try:
        job_data = validate_job_profile("Software Engineer at TechCorp")
        print("✅ Job profile validation successful")
    except Exception as e:
        print(f"❌ Job profile validation failed: {e}")
        return False
    
    # Test 6: Test LaTeX generation
    try:
        test_data = {
            "name": "Test User",
            "email": "test@email.com",
            "phone": "123-456-7890",
            "summary": "Test summary",
            "experience": ["Test experience"],
            "education": ["Test education"],
            "skills": ["Python", "JavaScript"]
        }
        latex_file = generate_latex_resume(test_data, "test_resume.tex")
        print("✅ LaTeX generation successful")
        
        # Clean up test file
        if os.path.exists("test_resume.tex"):
            os.remove("test_resume.tex")
            
    except Exception as e:
        print(f"❌ LaTeX generation failed: {e}")
        return False
    
    print("\n🎉 All components are working correctly!")
    print("📋 Next steps:")
    print("   1. Install Ollama: https://ollama.com/download")
    print("   2. Start Ollama: ollama serve")
    print("   3. Pull model: ollama pull mistral")
    print("   4. Run project: python main.py")
    
    return True

if __name__ == "__main__":
    success = test_components()
    if success:
        print("\n✅ System is ready for agentic AI resume building!")
    else:
        print("\n❌ Some components need attention.") 