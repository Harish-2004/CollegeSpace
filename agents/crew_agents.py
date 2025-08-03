from crewai import Agent, LLM
from config.llm_config import get_llm_config

# Configure LLM for reasoning
llm = get_llm_config()

# Database Agent for data retrieval and management
database_agent = Agent(
    role="Database Manager",
    goal="Retrieve and manage user data from MongoDB, handle data validation and transformation",
    backstory="Expert in database operations, data validation, and user profile management. Ensures data integrity and proper formatting for downstream agents.",
    verbose=True,
    llm=llm  # LLM reasoning enabled
)

# Profile Analysis Agent
profile_analyzer = Agent(
    role="Profile Analyzer",
    goal="Analyze user data and job profile to determine resume highlights and key strengths",
    backstory="Expert in resume optimization and job matching. Specializes in identifying transferable skills and relevant experience for specific job profiles.",
    verbose=True,
    llm=llm  # LLM reasoning enabled
)

# Resume Writer Agent
resume_writer = Agent(
    role="Resume Writer",
    goal="Write compelling resume sections tailored to the job profile and ATS requirements",
    backstory="Professional resume writer with extensive experience in tech recruiting. Expert in crafting ATS-optimized content that passes screening systems.",
    verbose=True,
    llm=llm  # LLM reasoning enabled
)

# Cover Letter Generator Agent
cover_letter_generator = Agent(
    role="Cover Letter Specialist",
    goal="Generate personalized cover letters that complement the resume and address specific job requirements",
    backstory="Experienced cover letter writer who creates compelling narratives that connect candidate experience to job requirements. Expert in storytelling and persuasion.",
    verbose=True,
    llm=llm  # LLM reasoning enabled
)

# Skill Gap Analysis Agent
skill_gap_analyzer = Agent(
    role="Skill Gap Analyst",
    goal="Analyze the gap between user skills and job requirements, provide actionable recommendations",
    backstory="Expert in skills assessment and career development. Specializes in identifying skill gaps and recommending learning paths for career advancement.",
    verbose=True,
    llm=llm  # LLM reasoning enabled
)

# ATS Optimization Checker Agent
ats_optimizer = Agent(
    role="ATS Optimization Specialist",
    goal="Optimize resume and cover letter for Applicant Tracking Systems, ensure maximum visibility",
    backstory="Expert in ATS systems and resume optimization. Deep understanding of keyword optimization, formatting requirements, and screening algorithms used by major ATS platforms.",
    verbose=True,
    llm=llm  # LLM reasoning enabled
) 