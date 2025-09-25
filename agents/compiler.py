import subprocess
import os
from typing import Optional

def compile_latex_to_pdf(latex_file: str, output_dir: str = ".") -> Optional[str]:
    """
    Compile LaTeX file to PDF with enhanced error handling.
    
    Args:
        latex_file: Path to LaTeX file
        output_dir: Output directory for PDF
        
    Returns:
        Path to generated PDF file, or None if compilation failed
    """
    try:
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Change to output directory for compilation
        original_dir = os.getcwd()
        os.chdir(output_dir)
        
        # Run pdflatex with error handling
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', latex_file],
            capture_output=True,
            text=True,
            timeout=60  # 60 second timeout
        )
        
        # Check if compilation was successful
        if result.returncode == 0:
            pdf_file = latex_file.replace('.tex', '.pdf')
            if os.path.exists(pdf_file):
                print(f"✅ PDF generated successfully: {pdf_file}")
                return pdf_file
            else:
                print(f"❌ PDF file not found after compilation: {pdf_file}")
                return None
        else:
            print(f"❌ LaTeX compilation failed with return code {result.returncode}")
            print(f"Error output: {result.stderr}")
            return None
            
    except subprocess.TimeoutExpired:
        print(f"❌ LaTeX compilation timed out for {latex_file}")
        return None
    except FileNotFoundError:
        print(f"❌ pdflatex not found. Please install a LaTeX distribution.")
        return None
    except Exception as e:
        print(f"❌ Error compiling LaTeX: {e}")
        return None
    finally:
        # Return to original directory
        os.chdir(original_dir)

def compile_multiple_documents(latex_files: list, output_dir: str = ".") -> dict:
    """
    Compile multiple LaTeX files to PDF.
    
    Args:
        latex_files: List of LaTeX file paths
        output_dir: Output directory for PDFs
        
    Returns:
        Dictionary with compilation results
    """
    results = {}
    
    for latex_file in latex_files:
        if os.path.exists(latex_file):
            pdf_file = compile_latex_to_pdf(latex_file, output_dir)
            results[latex_file] = {
                "success": pdf_file is not None,
                "pdf_file": pdf_file
            }
        else:
            results[latex_file] = {
                "success": False,
                "error": "LaTeX file not found"
            }
    #print(results)
    return results 