import os
import subprocess

# Use raw string for Windows path to avoid escape character issues
filepath = r"D:\Project_ETAP\06.WTIIRA\Attachments\PB Guide 2015_PFCED111008EN_V1.pdf"

output_folder = r"D:\Proj.Other\Marker_pdf\Output"
output_file = os.path.join(output_folder, "extracted_text.txt")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Run marker_single command and save output to file
print(f"Processing {filepath}...")
try:
    # Using subprocess to call marker_single and redirect output to a file
    with open(output_file, "w", encoding="utf-8") as f:
        result = subprocess.run(
            ["marker_single", filepath], stdout=f, text=True, check=True
        )

    print(f"Extraction complete. Results saved to {output_file}")
    print(
        f"Note: This version doesn't extract images. To save images, consider using marker_single with additional options."
    )
except subprocess.CalledProcessError as e:
    print(f"Error processing the PDF: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
