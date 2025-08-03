from crewai import Task
from agents.crew_agents import (
    database_agent, profile_analyzer, resume_writer, 
    cover_letter_generator, skill_gap_analyzer, ats_optimizer
)

# Database retrieval task
database_task = Task(
    description="Retrieve user data from MongoDB database, validate and format the data for processing. Ensure all required fields are present and properly formatted.",
    expected_output="Validated and formatted user data ready for analysis.",
    agent=database_agent
)

# Profile analysis task
analyze_profile_task = Task(
    description="Analyze the user's data and the job profile to determine what should be highlighted in the resume. Identify key strengths, relevant experience, and transferable skills.",
    expected_output="A comprehensive analysis of highlights, key strengths, and relevant experience for the resume.",
    agent=profile_analyzer
)

# Resume writing task
write_resume_task = Task(
    description="Write compelling resume sections (summary, experience, education, skills) in JSON format, tailored to the job profile and ATS requirements. Ensure keyword optimization and proper formatting.",
    expected_output="A JSON object with optimized resume sections ready for ATS processing.",
    agent=resume_writer
)

# Cover letter generation task
generate_cover_letter_task = Task(
    description="Generate a personalized cover letter that complements the resume and addresses specific job requirements. Create compelling narratives that connect candidate experience to job needs.",
    expected_output="A well-structured cover letter in markdown format that tells a compelling story.",
    agent=cover_letter_generator
)

# Skill gap analysis task
analyze_skill_gaps_task = Task(
    description="Analyze the gap between user skills and job requirements. Identify missing skills, provide actionable recommendations for skill development, and suggest learning resources.",
    expected_output="A detailed skill gap analysis with specific recommendations and learning paths.",
    agent=skill_gap_analyzer
)

# ATS optimization task
optimize_ats_task = Task(
    description="Optimize the resume and cover letter for Applicant Tracking Systems. Check keyword density, formatting compliance, and ensure maximum visibility to ATS algorithms.",
    expected_output="ATS-optimized resume and cover letter with keyword analysis and formatting recommendations.",
    agent=ats_optimizer
) 