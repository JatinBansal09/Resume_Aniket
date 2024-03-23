from playwright.sync_api import sync_playwright
import os
import pathlib

filepath = os.path.abspath("F:\Study\Tslas-DESKTOP-G14D31O\Year 4\Sem 8\Online Courses\HTML and CSS\HTML\Projects\Resume_Aniket\Index.html")
fileUrl= pathlib.Path(filepath).as_uri()

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(fileUrl)
    page.emulate_media(media="screen")
    
    # Set the PDF generation options
    pdf_options = {
        'path': "Aniket_resume.pdf",
        'format': 'A4',  # Specify the page format
        'prefer_css_page_size': True,  # Use CSS page size definitions
        'print_background': True,  # Print background colors and images
        'width':'800px'
    }
    
    # Generate the PDF with specified options
    page.pdf(**pdf_options)
    
    browser.close()
