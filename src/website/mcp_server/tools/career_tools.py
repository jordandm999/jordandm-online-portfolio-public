import json
import os
from mcp.server.fastmcp import FastMCP

def load_career_json(filename: str) -> dict:
    """Helper function to load JSON files from the career directory"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Navigate to the JSON files location
    base_path = os.path.join(current_dir, "..", "resources", "career")
    file_path = os.path.join(base_path, f"{filename}.json")
    print(f"Loading from: {file_path}")  # Debug print
    with open(file_path) as f:
        return json.load(f)

mcp = FastMCP()

@mcp.tool()
def get_work_experience() -> dict:
    """Get Jordan's work experience and job history"""
    return load_career_json("work_experience")

@mcp.tool()
def get_projects() -> dict:
    """Get information about Jordan's notable projects and achievements"""
    return load_career_json("projects")

@mcp.tool()
def get_certifications() -> dict:
    """Get information about Jordan's professional certifications"""
    return load_career_json("certifications")

@mcp.tool()
def get_professional_summary() -> dict:
    """Get Jordan's professional summary"""
    return load_career_json("professional_summary")

@mcp.tool()
def get_skills() -> dict:
    """Get Jordan's technical and professional skills"""
    return load_career_json("skills")