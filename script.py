import sys
import os
import json
import re
import unicodedata
import subprocess

data_path="data.json"
pdf_file_name="file.pdf"
latex_file_name="latex.tex"
text_file_name="text.txt"

def latex_create_pdf(text, pdf_file_name):
    # Generate LaTeX code with added packages
    latex_content = (
        "\\documentclass{article}\n"
        "\\usepackage[T1]{fontenc}\n"
        "\\usepackage[utf8]{inputenc}\n"
        "\\usepackage{lmodern}\n"
        "\\begin{document}\n"
        "\\begin{verbatim}\n"
    )

    # Escape special characters
    escaped_text = re.sub(r'([#$%&_{}])', r'\\\1', text)
    
    latex_content += escaped_text
    
    latex_content += "\\end{verbatim}"
    latex_content += "\\end{document}"

    # Write LaTeX content to a file
    with open(latex_file_name, "wb") as f:
        f.write(latex_content.encode('utf-8'))

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Specify the name of the PDF file
    pdf_file_name = os.path.join(script_dir, pdf_file_name)

    try:
        subprocess.run(['pdflatex', latex_file_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")        

if __name__ == "__main__":
    
    with open(data_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    json_formatted_str = json.dumps(json_data, indent=2)

    with open(text_file_name, "w") as file:
        file.write(json_formatted_str)

    # Generate the PDF file
    latex_create_pdf(json_formatted_str, pdf_file_name) #LaTeX