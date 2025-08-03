"""
Run the agentic AI resume builder without Ollama (for testing).
This script uses mock LLM responses to test the workflow.
"""

import os
import sys
from agents.data_collector import collect_user_data, validate_job_profile
from agents.latex_generator import generate_latex_resume
from agents.compiler import compile_latex_to_pdf
from config.llm_config import get_mock_llm

def run_with_mock_llm():
    """
    Run the resume builder with mock LLM responses for testing.
    """
    print("🤖 Running Agentic Resume Builder with Mock LLM...")
    
    try:
        # Set up mock environment
        user_id = "demo_user_id"
        job_profile = "Software Engineer at TechCorp, focusing on backend development, Python, and cloud infrastructure."
        
        print(f"📋 User ID: {user_id}")
        print(f"🎯 Job Profile: {job_profile[:50]}...")
        
        # Collect user data
        print("📊 Collecting user data...")
        user_data = collect_user_data(user_id)
        print(f"✅ User data collected: {user_data['name']}")
        
        # Validate job profile
        print("📝 Validating job profile...")
        job_data = validate_job_profile(job_profile)
        print("✅ Job profile validated")
        
        # Mock LLM responses for testing
        mock_responses = {
            "profile_analysis": {
                "highlights": ["Python development", "Cloud infrastructure", "Microservices"],
                "key_strengths": ["Backend development", "System architecture", "Team leadership"],
                "relevant_experience": ["5+ years in software engineering", "Led microservices projects"]
            },
            "resume_sections": {
                "summary": "Experienced software engineer with 5+ years in backend development, specializing in Python, cloud infrastructure, and scalable systems.",
                "experience": [
                    "Senior Software Engineer at TechCorp (2022-2024): Led development of microservices architecture, improved system performance by 40%",
                    "Software Engineer at StartupXYZ (2020-2022): Built REST APIs and database systems, mentored junior developers"
                ],
                "education": [
                    "Bachelor of Science in Computer Science, University of Technology (2019)",
                    "Certification in AWS Cloud Practitioner (2021)"
                ],
                "skills": ["Python", "JavaScript", "Node.js", "AWS", "Docker", "Kubernetes", "Git", "REST APIs", "Microservices"]
            },
            "cover_letter": {
                "opening": "I am writing to express my strong interest in the Software Engineer position at TechCorp.",
                "body": "With 5+ years of experience in backend development and cloud infrastructure, I believe I would be a valuable addition to your team.",
                "closing": "I look forward to discussing how my skills can contribute to TechCorp's success."
            },
            "skill_gaps": {
                "missing_skills": ["React Native", "GraphQL"],
                "recommendations": ["Learn React Native for mobile development", "Study GraphQL for API design"],
                "timeline": "3-6 months for skill development"
            },
            "ats_optimization": {
                "keywords": ["Python", "AWS", "Microservices", "Docker", "Kubernetes"],
                "formatting": "ATS-friendly formatting applied",
                "score": "85% ATS compatibility"
            }
        }
        
        # Generate resume with mock data
        print("📄 Generating resume...")
        latex_file = generate_latex_resume(mock_responses["resume_sections"])
        
        # Compile to PDF
        print("🔄 Compiling to PDF...")
        pdf_file = compile_latex_to_pdf(latex_file)
        
        if pdf_file:
            print(f"✅ Resume PDF generated successfully: {pdf_file}")
        else:
            print("❌ PDF generation failed")
        
        # Display results
        print("\n📊 Mock Analysis Results:")
        print(f"🎯 Profile Analysis: {len(mock_responses['profile_analysis']['highlights'])} highlights identified")
        print(f"📝 Resume Sections: {len(mock_responses['resume_sections']['experience'])} experiences included")
        print(f"📄 Cover Letter: Generated with personalized content")
        print(f"🔍 Skill Gaps: {len(mock_responses['skill_gaps']['missing_skills'])} skills to develop")
        print(f"🎯 ATS Score: {mock_responses['ats_optimization']['score']}")
        
        return {
            "status": "success",
            "pdf_file": pdf_file,
            "mock_data": mock_responses
        }
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {
            "status": "error",
            "error": str(e)
        }

if __name__ == "__main__":
    result = run_with_mock_llm()
    
    if result["status"] == "success":
        print("\n🎉 Mock test completed successfully!")
        print("To run with real LLM, install Ollama and use: python main.py")
    else:
        print(f"\n❌ Mock test failed: {result['error']}") 