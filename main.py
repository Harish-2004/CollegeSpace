from agents.data_collector import collect_user_data, validate_job_profile
from agents.latex_generator import generate_latex_resume
from agents.compiler import compile_latex_to_pdf
from agents.crew_crew import resume_crew, skill_analysis_crew, ats_optimization_crew, cover_letter_crew
import json
import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def serialize_for_crewai(data: Any) -> Any:
    """Ensure data is compatible with CrewAI by converting datetime objects."""
    if isinstance(data, dict):
        return {key: serialize_for_crewai(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [serialize_for_crewai(item) for item in data]
    elif hasattr(data, 'isoformat'):  # datetime objects
        return data.isoformat()
    else:
        return data

def run_resume_builder(user_id: str, job_profile: str, crew_type: str = "full") -> Dict[str, Any]:
    """
    Run the agentic resume builder with specified crew type.
    
    Args:
        user_id: User ID for database retrieval
        job_profile: Job description/profile
        crew_type: Type of crew to run ("full", "skill_analysis", "ats_optimization")
        
    Returns:
        Dict containing results from the crew execution
    """
    try:
        # Validate inputs
        if not user_id or not job_profile:
            raise ValueError("User ID and job profile are required")
        
        # Collect and validate data
        user_data = collect_user_data(user_id)
        job_data = validate_job_profile(job_profile)
        
        # Ensure all data is CrewAI compatible
        user_data = serialize_for_crewai(user_data)
        job_data = serialize_for_crewai(job_data)
        
        # Prepare inputs for crew
        inputs = {
            "user_data": user_data,
            "job_profile": job_data,
            "user_id": user_id
        }
        
        # Select crew based on type
      
        if crew_type == "full":
            crew = resume_crew
            print("Running full resume builder crew...")
        elif crew_type == "skill_analysis":
            crew = skill_analysis_crew
            print("Running skill analysis crew...")
        elif crew_type == "ats_optimization":
            crew = ats_optimization_crew
            print("Running ATS optimization crew...")
        elif crew_type == "cover_letter":
            crew = cover_letter_crew
            print("Running cover letter generation crew...")
        else:
            raise ValueError(f"Unknown crew type: {crew_type}")
        
        # Run the crew
        result = crew.kickoff(inputs=inputs)
        print("------------------------",result,"------------------------")
        # Generate LaTeX and PDF if resume data is available
        if isinstance(result, dict) and 'resume_sections' in result:
            latex_file = generate_latex_resume(result['resume_sections'])
            compile_latex_to_pdf(latex_file)
            print("Resume PDF generated successfully!")
        
        return {
            "status": "success",
            "crew_type": crew_type,
            "result": result,
            "user_id": user_id
        }
        
    except Exception as e:
        print(f"Error in resume builder: {str(e)}")
        return {
            "status": "error",
            "error": str(e),
            "crew_type": crew_type,
            "user_id": user_id
        }

if __name__ == "__main__":
    # Configuration
    user_id = os.getenv("USER_ID", "demo_user_id")
    job_profile = os.getenv("JOB_PROFILE", 
        "Software Engineer at TechCorp, focusing on backend development, Python, and cloud infrastructure.")
    crew_type = os.getenv("CREW_TYPE", "full")  # full, skill_analysis, ats_optimization
    
    print(f"🤖 Starting Agentic Resume Builder...")
    print(f"👤 User ID: {user_id}")
    print(f"🎯 Crew Type: {crew_type}")
    print(f"💼 Job Profile: {job_profile[:100]}...")
    
    # Check which API is being used
    if os.getenv("HUGGINGFACE_API_KEY"):
        print("🎯 Using Hugging Face with model - Excellent for resume building!")
    else:
        print("🆓 Using local Ollama or Mock LLM - Basic functionality")
    
    # Run the resume builder
    result = run_resume_builder(user_id, job_profile, crew_type)
    
    # Output results
    #print(result)
    if result["status"] == "success":
        print("✅ Resume builder completed successfully!")
    
        # Handle CrewOutput object properly
        if hasattr(result['result'], '__dict__'):
            # Convert CrewOutput to dict if possible
            try:
                #result_data = result['result'].__dict__

                #print(f"📊 Results: {json.dumps(result_data, indent=2, default=str)}")
                print("results")
            except:
                #print(f"📊 Results: {str(result['result'])}")
                print("results-except")
        else:
            # Try to serialize normally
            try:
                #print(f"📊 Results: {json.dumps(result['result'], indent=2, default=str)}")
                print("serializable issue")
            except:
                #print(f"📊 Results: {str(result['result'])}")
                print("not serializable issue")
    else:
        print(f"❌ Resume builder failed: {result['error']}") 