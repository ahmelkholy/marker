#!/usr/bin/env python3
"""
Markdown to Reveal.js Converter
Converts the Chapter 8 Transmission Investment presentation from Markdown to Reveal.js HTML
"""

import re
import os
import shutil


def create_revealjs_html():
    """Create the base reveal.js HTML structure"""
    html_template = """<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>Chapter 8: Investing in Transmission</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/reset.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/theme/white.css">

    <!-- Theme used for syntax highlighted code -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/highlight/monokai.css">

    <!-- Custom CSS -->
    <style>
        .reveal {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .reveal h1 {
            color: #2980b9;
            border-bottom: 3px solid #3498db;
            padding-bottom: 20px;
            font-size: 2.5em;
        }

        .reveal h2 {
            color: #27ae60;
            border-left: 5px solid #2ecc71;
            padding-left: 20px;
            font-size: 1.8em;
        }

        .reveal h3 {
            color: #8e44ad;
            font-size: 1.4em;
        }

        .formula-box {
            background: #ecf0f1;
            padding: 20px;
            border-left: 4px solid #3498db;
            border-radius: 8px;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
        }

        .highlight-box {
            background: #fff3cd;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #ffc107;
            margin: 15px 0;
        }

        .key-point-box {
            background: #d4edda;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #28a745;
            margin: 15px 0;
        }

        .warning-box {
            background: #f8d7da;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #dc3545;
            margin: 15px 0;
        }

        .reveal img {
            max-width: 80%;
            max-height: 70vh;
            border: 2px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        .reveal table {
            font-size: 0.8em;
            margin: 20px auto;
            border-collapse: collapse;
        }

        .reveal table th {
            background: #3498db;
            color: white;
            padding: 10px;
            border: 1px solid #ddd;
        }

        .reveal table td {
            padding: 8px;
            border: 1px solid #ddd;
        }

        .reveal table tr:nth-child(even) {
            background: #f8f9fa;
        }

        .two-column {
            display: flex;
            gap: 2em;
        }

        .two-column > div {
            flex: 1;
        }

        .math-formula {
            font-size: 1.2em;
            background: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }

        .emoji {
            font-size: 1.2em;
        }
    </style>
</head>

<body>
    <div class="reveal">
        <div class="slides">
            {slides_content}
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/notes/notes.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/markdown/markdown.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/highlight/highlight.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/math/math.js"></script>

    <script>
        Reveal.initialize({
            hash: true,
            controls: true,
            progress: true,
            center: true,
            transition: 'slide',
            math: {
                mathjax: 'https://cdn.jsdelivr.net/gh/mathjax/mathjax@2.7.8/MathJax.js',
                config: 'TeX-AMS_HTML-full'
            },
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes, RevealMath ]
        });
    </script>
</body>
</html>"""
    return html_template


def clean_markdown_text(text):
    """Clean markdown formatting for HTML"""
    if not text:
        return ""

    # Convert markdown formatting to HTML
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)  # Bold
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)  # Italic
    text = re.sub(r"`(.*?)`", r"<code>\1</code>", text)  # Code
    text = re.sub(r"#{1,6}\s*", "", text)  # Headers

    return text.strip()


def process_formula_content(content):
    """Process formula content for reveal.js"""
    # Convert code blocks to formatted formulas
    content = re.sub(
        r"```\n(.*?)\n```",
        r'<div class="math-formula">\1</div>',
        content,
        flags=re.DOTALL,
    )
    content = re.sub(r"`([^`]+)`", r"<code>\1</code>", content)

    # Convert mathematical expressions
    content = re.sub(r"\$\$(.*?)\$\$", r"$$\1$$", content, flags=re.DOTALL)
    content = re.sub(r"\$(.*?)\$", r"$\1$", content)

    return content


def create_slide_content(slide_data):
    """Create HTML content for a slide"""
    if slide_data["type"] == "title":
        return f"""
<section>
    <h1><span class="emoji">📊</span> Chapter 8: Investing in Transmission</h1>
    <h2><span class="emoji">🎯</span> Fundamentals of Power System Economics</h2>
    <h3><em>Coordinating Generation and Transmission in Competitive Markets</em></h3>
</section>
"""

    elif slide_data["type"] == "toc":
        content_html = "<ul>"
        for item in slide_data["content"]:
            clean_item = clean_markdown_text(item.replace("- ", ""))
            content_html += f"<li>{clean_item}</li>"
        content_html += "</ul>"

        return f"""
<section>
    <h1><span class="emoji">📋</span> Table of Contents</h1>
    {content_html}
</section>
"""

    elif slide_data["type"] == "content":
        title_html = clean_markdown_text(slide_data["title"])

        content_html = ""
        current_level = 0
        in_list = False

        for item in slide_data["content"]:
            if not item.strip():
                continue

            # Determine content type and formatting
            if item.strip().startswith("### "):
                if in_list:
                    content_html += "</ul>"
                    in_list = False
                heading = clean_markdown_text(item.replace("### ", ""))
                content_html += f"<h3>{heading}</h3>"
            elif item.strip().startswith("## "):
                if in_list:
                    content_html += "</ul>"
                    in_list = False
                heading = clean_markdown_text(item.replace("## ", ""))
                content_html += f"<h2>{heading}</h2>"
            elif item.strip().startswith("- "):
                if not in_list:
                    content_html += "<ul>"
                    in_list = True
                list_item = clean_markdown_text(item.replace("- ", ""))
                content_html += f"<li>{list_item}</li>"
            elif item.strip().startswith("  - "):
                if not in_list:
                    content_html += "<ul>"
                    in_list = True
                list_item = clean_markdown_text(item.replace("  - ", ""))
                content_html += f'<li style="margin-left: 20px;">{list_item}</li>'
            else:
                if in_list:
                    content_html += "</ul>"
                    in_list = False
                clean_item = clean_markdown_text(item)
                if clean_item:
                    content_html += f"<p>{clean_item}</p>"

        if in_list:
            content_html += "</ul>"

        return f"""
<section>
    <h1>{title_html}</h1>
    {content_html}
</section>
"""

    elif slide_data["type"] == "formula":
        title_html = clean_markdown_text(slide_data["title"])
        formula_html = process_formula_content(slide_data["content"])

        return f"""
<section>
    <h1>{title_html}</h1>
    <div class="formula-box">
        {formula_html}
    </div>
</section>
"""

    elif slide_data["type"] == "image":
        title_html = clean_markdown_text(slide_data["title"])

        images_html = ""
        for img_path in slide_data["images"]:
            # Convert absolute path to relative path for web
            img_filename = os.path.basename(img_path)
            images_html += (
                f'<img src="images/{img_filename}" alt="{img_filename}" /><br>'
            )

        content_html = ""
        if slide_data.get("content"):
            content_html = "<ul>"
            for item in slide_data["content"]:
                clean_item = clean_markdown_text(item.replace("- ", ""))
                content_html += f"<li>{clean_item}</li>"
            content_html += "</ul>"

        return f"""
<section>
    <h1>{title_html}</h1>
    <div class="two-column">
        <div>
            {images_html}
        </div>
        <div>
            {content_html}
        </div>
    </div>
</section>
"""

    elif slide_data["type"] == "table":
        title_html = clean_markdown_text(slide_data["title"])

        # Parse table
        rows = slide_data["content"].strip().split("\n")
        if len(rows) < 3:
            return f"""
<section>
    <h1>{title_html}</h1>
    <p>Table data not available</p>
</section>
"""

        headers = [col.strip() for col in rows[0].split("|")[1:-1]]
        data_rows = []

        for row in rows[2:]:  # Skip header separator
            if "|" in row:
                data_rows.append([col.strip() for col in row.split("|")[1:-1]])

        table_html = "<table><thead><tr>"
        for header in headers:
            table_html += f"<th>{clean_markdown_text(header)}</th>"
        table_html += "</tr></thead><tbody>"

        for row_data in data_rows:
            table_html += "<tr>"
            for cell_data in row_data:
                table_html += f"<td>{clean_markdown_text(cell_data)}</td>"
            table_html += "</tr>"

        table_html += "</tbody></table>"

        return f"""
<section>
    <h1>{title_html}</h1>
    {table_html}
</section>
"""

    return ""


def parse_markdown_file(file_path):
    """Parse the markdown file and extract slides with images"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split content by slide separators
    slides = content.split("\n---\n")

    parsed_slides = []

    # Add title slide
    parsed_slides.append(
        {
            "type": "title",
            "title": "Chapter 8: Investing in Transmission",
            "content": [],
        }
    )

    for slide_content in slides:
        if not slide_content.strip():
            continue

        lines = slide_content.strip().split("\n")

        # Skip YAML front matter
        if lines[0].strip() == "---":
            continue

        # Find title (first # heading)
        title = ""
        content_lines = []
        images = []
        in_table = False
        table_content = ""
        in_formula = False
        formula_content = ""

        for line in lines:
            line = line.strip()

            if line.startswith("# "):
                title = line[2:].strip()

                # Special handling for Table of Contents
                if "Table of Contents" in title:
                    # Look ahead for the TOC content
                    toc_content = []
                    for next_line in lines[lines.index(line) + 1 :]:
                        if next_line.strip().startswith(
                            "1."
                        ) or next_line.strip().startswith("-"):
                            clean_line = next_line.strip()
                            if clean_line.startswith("1.") or clean_line.startswith(
                                "2."
                            ):
                                clean_line = "- " + clean_line[2:].strip()
                            toc_content.append(clean_line)
                        elif next_line.strip().startswith("8."):
                            toc_content.append("- " + next_line.strip()[2:].strip())
                        elif not next_line.strip():
                            break

                    parsed_slides.append(
                        {"type": "toc", "title": title, "content": toc_content}
                    )
                    continue

            elif line.startswith("!["):
                # Extract image path
                img_match = re.search(r"!\[.*?\]\((.*?)\)", line)
                if img_match:
                    img_path = img_match.group(1)
                    images.append(img_path)

            elif line.startswith('<div class="formula">'):
                in_formula = True
                formula_content = ""
            elif line.startswith("</div>") and in_formula:
                in_formula = False
                if formula_content and title:
                    parsed_slides.append(
                        {"type": "formula", "title": title, "content": formula_content}
                    )
                    formula_content = ""
            elif in_formula:
                if line and not line.startswith("<"):
                    formula_content += line + "\n"

            elif "|" in line and (
                "---" in line or "MW" in line or "Period" in line or "Line" in line
            ):
                if not in_table:
                    in_table = True
                    table_content = line + "\n"
                else:
                    table_content += line + "\n"
            elif in_table and "|" in line:
                table_content += line + "\n"
            elif in_table and not line:
                if table_content and title:
                    parsed_slides.append(
                        {"type": "table", "title": title, "content": table_content}
                    )
                in_table = False
                table_content = ""

            elif (
                line.startswith("- ")
                or line.startswith("  - ")
                or line.startswith("### ")
                or line.startswith("## ")
                or (
                    line
                    and not line.startswith("<")
                    and not line.startswith("![]")
                    and not line.startswith("```")
                    and not line.startswith("#")
                )
            ):
                if not any(
                    skip in line
                    for skip in [
                        "mermaid",
                        "graph TD",
                        "<div",
                        "</div>",
                        "marp:",
                        "theme:",
                    ]
                ):
                    content_lines.append(line)

        # Handle any remaining table content
        if in_table and table_content and title:
            parsed_slides.append(
                {"type": "table", "title": title, "content": table_content}
            )

        # Add slide with images if we have them
        if images and title:
            parsed_slides.append(
                {
                    "type": "image",
                    "title": title,
                    "content": content_lines,
                    "images": images,
                }
            )
        # Add regular content slide if we have content
        elif title and content_lines and not in_formula:
            parsed_slides.append(
                {"type": "content", "title": title, "content": content_lines}
            )

    return parsed_slides


def copy_images(source_dir, target_dir):
    """Copy all image files to the target directory"""
    os.makedirs(target_dir, exist_ok=True)

    for filename in os.listdir(source_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_dir, filename)
            shutil.copy2(source_path, target_path)
            print(f"📷 Copied image: {filename}")


def main():
    """Main function to convert markdown to Reveal.js"""
    input_file = "d:/Proj.Other/Marker_pdf/marker-env/Lib/site-packages/conversion_results/ch8/Ch8_Transmission_Investment_Presentation.md"
    output_file = "d:/Proj.Other/Marker_pdf/Ch8_Transmission_Investment_RevealJS.html"
    source_images_dir = (
        "d:/Proj.Other/Marker_pdf/marker-env/Lib/site-packages/conversion_results/ch8"
    )
    target_images_dir = "d:/Proj.Other/Marker_pdf/images"

    print("🚀 Starting Markdown to Reveal.js conversion...")

    # Copy images
    copy_images(source_images_dir, target_images_dir)
    print("✅ Images copied to presentation directory")

    # Parse markdown file
    slides_data = parse_markdown_file(input_file)
    print(f"📖 Parsed {len(slides_data)} slides from markdown")

    # Generate slides HTML
    slides_html = ""
    for i, slide_data in enumerate(slides_data):
        try:
            slide_html = create_slide_content(slide_data)
            slides_html += slide_html + "\n"

            if (i + 1) % 5 == 0:
                print(f"📊 Processed {i + 1} slides...")

        except Exception as e:
            print(f"⚠️ Warning: Error processing slide {i+1}: {str(e)}")
            continue

    # Create final HTML
    html_template = create_revealjs_html()
    final_html = html_template.replace("{slides_content}", slides_html)

    # Save HTML file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"🎉 Successfully created Reveal.js presentation: {output_file}")
    print(f"📈 Total slides created: {len(slides_data)}")
    print("🌐 Open the HTML file in a web browser to view the presentation")
    print("💡 Use arrow keys to navigate, 'F' for fullscreen, 'ESC' for overview")


if __name__ == "__main__":
    main()
