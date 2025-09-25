from jinja2 import Environment, FileSystemLoader
import os
from typing import Dict, Any, Optional

def generate_latex_resume(data: Dict[str, Any], output_file: str = "resumeofperson.tex") -> str:
    """
    Generate LaTeX resume from data.
    
    Args:
        data: Dictionary containing resume data
        output_file: Output file name
        
    Returns:
        Path to generated LaTeX file
    """
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('resume.tex')
    latex_code = template.render(**data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_code)
    
    return output_file

def generate_latex_cover_letter(data: Dict[str, Any], output_file: str = "cover_letter.tex") -> str:
    """
    Generate LaTeX cover letter from data.
    
    Args:
        data: Dictionary containing cover letter data
        output_file: Output file name
        
    Returns:
        Path to generated LaTeX file
    """
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('resume.tex')
    latex_code = template.render(**data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_code)
    
    return output_file

def generate_latex_skill_report(data: Dict[str, Any], output_file: str = "skill_report.tex") -> str:
    """
    Generate LaTeX skill gap analysis report.
    
    Args:
        data: Dictionary containing skill analysis data
        output_file: Output file name
        
    Returns:
        Path to generated LaTeX file
    """
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('resume.tex')
    latex_code = template.render(**data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_code)
    
    return output_file 