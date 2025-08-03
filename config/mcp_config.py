# MCP (Model Context Protocol) Configuration
# This shows how MCP protocol is used for agent communication and tool orchestration

MCP_SERVER_CONFIG = {
    "enabled": True,
    "servers": [
        {
            "type": "stdio",
            "command": "npx",
            "args": ["@modelcontextprotocol/server-filesystem"]
        }
    ]
}

# MCP Tools Configuration
MCP_TOOLS = {
    "database_tools": [
        "read_user_data",
        "validate_user_data",
        "update_user_data"
    ],
    "analysis_tools": [
        "analyze_job_profile",
        "extract_keywords",
        "identify_skill_gaps"
    ],
    "generation_tools": [
        "generate_resume_sections",
        "create_cover_letter",
        "optimize_for_ats"
    ]
}

# MCP Protocol enables:
# 1. Agent-to-agent communication
# 2. Tool sharing between agents
# 3. Dynamic workflow orchestration
# 4. Context sharing across agents 