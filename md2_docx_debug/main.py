from md2docx_python.src.docx2md_python import word_to_markdown

# Define the paths to your files
word_file = "sample_files/test_document.docx"
markdown_file = "sample_files/test_document_output.md"

# Convert the Word document to a Markdown file
word_to_markdown(word_file, markdown_file)