from .hello_world import hello_world
from .career_tools import (
    get_work_experience,
    get_projects,
    get_certifications,
    get_professional_summary,
    get_skills
)

# Registry of all tools
tool_registry = [
    hello_world,
    get_work_experience,
    get_projects,
    get_certifications,
    get_professional_summary,
    get_skills
]