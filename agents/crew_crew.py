from crewai import Crew, Process
from agents.crew_agents import (
    database_agent, profile_analyzer, resume_writer, 
    cover_letter_generator, skill_gap_analyzer, ats_optimizer
)
from agents.crew_tasks import (
    database_task, analyze_profile_task, write_resume_task,
    generate_cover_letter_task, analyze_skill_gaps_task, optimize_ats_task
)
from config.mcp_config import MCP_SERVER_CONFIG, MCP_TOOLS

# Main resume building crew with MCP protocol
resume_crew = Crew(
    agents=[
        database_agent, 
        profile_analyzer, 
        resume_writer, 
        cover_letter_generator, 
        skill_gap_analyzer, 
        ats_optimizer
    ],
    tasks=[
        database_task,
        analyze_profile_task, 
        write_resume_task,
        generate_cover_letter_task,
        analyze_skill_gaps_task,
        optimize_ats_task
    ],
    process=Process.sequential,
    verbose=True,
    # MCP Protocol Configuration
    mcp_server_params=MCP_SERVER_CONFIG,  # Enables MCP protocol
    # Tool sharing via MCP
    tools=MCP_TOOLS , # Agents can share tools via MCP
    output_format="json"
)

# Alternative crew for skill-focused analysis with MCP
skill_analysis_crew = Crew(
    agents=[database_agent, skill_gap_analyzer, profile_analyzer],
    tasks=[database_task, analyze_skill_gaps_task, analyze_profile_task],
    process=Process.sequential,
    verbose=True,
    mcp_server_params=MCP_SERVER_CONFIG,
    output_format="json"
)

# Alternative crew for ATS optimization only with MCP
ats_optimization_crew = Crew(
    agents=[ats_optimizer, resume_writer],
    tasks=[optimize_ats_task, write_resume_task],
    process=Process.sequential,
    verbose=True,
    mcp_server_params=MCP_SERVER_CONFIG,
    output_format="json"
) 

cover_letter_crew = Crew(
    agents=[database_agent, cover_letter_generator],
    tasks=[database_task, generate_cover_letter_task],
    process=Process.sequential,
    verbose=True,
    mcp_server_params=MCP_SERVER_CONFIG,
    output_format="json"
)   