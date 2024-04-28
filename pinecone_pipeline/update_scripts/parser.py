import os
from llama_parse import LlamaParse
from dotenv import load_dotenv
import glob

# Load environment variables
load_dotenv()

# Retrieve the API key from environment
llama_key = os.environ['LLAMA_PARSE_KEY']

# Initialize the LlamaParse with the appropriate settings
parser = LlamaParse(
    api_key=llama_key,  # This can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown"  # Options: "markdown" or "text"
)

# Define the directory containing HTML files
directory_path = "/home/dan/certorabot/pinecone_pipeline/update_scripts/html_output"

# Load all .html files from the directory
html_files = glob.glob(os.path.join(directory_path, "*.html"))
print(html_files)

# Iterate over each file, process it, and save the output
for html_file in html_files:
    try:
        # Load the HTML file data synchronously
        markdown_content = parser.load_data(html_file)

        # Check if the data is not a string (assuming it might be a list or another type)
        if not isinstance(markdown_content, str):
            markdown_content = ''.join(str(item) for item in markdown_content)

        # Define the output Markdown filename (same base name as the HTML file)
        markdown_file = os.path.splitext(os.path.basename(html_file))[0] + ".md"
        
        # Write the processed markdown content to a file
        with open(os.path.join(directory_path, markdown_file), 'w') as md_file:
            md_file.write(markdown_content)
            
    except Exception as e:
        print(f"Failed to process {html_file}: {str(e)}")
