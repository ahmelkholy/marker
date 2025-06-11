# 🎯 Ultimate Marp Template System

**Created by:** Ahmed M. Elkholy
**Email:** ahmed_elkholy@f-eng.tanta.edu.eg
**Version:** 1.0
**Date:** June 2025

## 📋 Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Template Files](#template-files)
4. [Installation & Setup](#installation--setup)
5. [Export to PPTX](#export-to-pptx)
6. [Export to PDF](#export-to-pdf)
7. [Font Scaling System](#font-scaling-system)
8. [Customization Guide](#customization-guide)
9. [Content Blocks Reference](#content-blocks-reference)
10. [Layout System](#layout-system)
11. [Troubleshooting](#troubleshooting)
12. [Examples](#examples)

---

## 🌟 Overview

This repository contains a comprehensive, professional Marp presentation template system designed for:

- **Academic presentations** (lectures, research)
- **Business presentations** (meetings, proposals)
- **Technical presentations** (code, documentation)
- **Educational content** (training, workshops)

### ✨ Key Features

- **🎛️ Universal Font Scaling**: One variable controls all font sizes
- **🎨 Professional Content Blocks**: Pre-styled components for any content type
- **📱 Responsive Design**: Works on all screen sizes and export formats
- **🎯 Export Ready**: Perfect PPTX, PDF, and HTML output
- **🛠️ Easy Customization**: Change colors, fonts, and spacing with CSS variables

---

## 🚀 Quick Start

### 1. Choose Your Template

- **`Ultimate_Marp_Template_Fixed.md`** - Full-featured template with all components
- **`Marp_Quick_Start_Template.md`** - Simplified template for basic presentations

### 2. Copy and Rename

```bash
# Copy the template
cp Ultimate_Marp_Template_Fixed.md my-presentation.md

# Edit with your favorite editor
code my-presentation.md
```

### 3. Customize Content

Replace the example content with your own while keeping the template structure.

### 4. Export

```bash
# Export to PowerPoint
marp my-presentation.md --pptx

# Export to PDF
marp my-presentation.md --pdf
```

---

## 📁 Template Files

| File Name                                 | Description                         | Best For                   |
| ----------------------------------------- | ----------------------------------- | -------------------------- |
| `Ultimate_Marp_Template_Fixed.md`         | Complete template with all features | Professional presentations |
| `Marp_Quick_Start_Template.md`            | Simplified template                 | Quick presentations        |
| `PSE_Lecture7_Transmission_Investment.md` | Academic example                    | Technical/academic content |

---

## ⚙️ Installation & Setup

### Prerequisites

1. **Install Marp CLI**

   ```bash
   npm install -g @marp-team/marp-cli
   ```

2. **Verify Installation**

   ```bash
   marp --version
   ```

3. **Install Chromium (for PDF export)**

   ```bash
   # Windows
   npm install -g puppeteer

   # Or install Chrome/Edge browser
   ```

### VS Code Extension (Optional)

1. Install "Marp for VS Code" extension
2. Open any `.md` file with Marp frontmatter
3. Press `Ctrl+Shift+P` → "Marp: Export slide deck"

---

## 📊 Export to PPTX

### Method 1: Command Line

```bash
# Basic export
marp presentation.md --pptx

# With custom output name
marp presentation.md --pptx -o "My_Presentation.pptx"

# High quality export
marp presentation.md --pptx --allow-local-files
```

### Method 2: VS Code Extension

1. Open your `.md` file in VS Code
2. Press `Ctrl+Shift+P`
3. Type "Marp: Export slide deck"
4. Select "PowerPoint (.pptx)"
5. Choose output location

### Method 3: Batch Export

```bash
# Export all .md files in current folder
for file in *.md; do
    marp "$file" --pptx -o "${file%.md}.pptx"
done
```

### PPTX Export Tips

- ✅ **Content blocks render perfectly**
- ✅ **Fonts scale properly**
- ✅ **Images maintain quality**
- ✅ **Mathematical formulas work**
- ⚠️ **Some CSS animations may not transfer**

---

## 📄 Export to PDF

### Method 1: Command Line

```bash
# Basic PDF export
marp presentation.md --pdf

# High quality PDF
marp presentation.md --pdf --allow-local-files

# Custom page size
marp presentation.md --pdf --pdf-notes --pdf-outlines
```

### Method 2: Browser Method

```bash
# Export to HTML first
marp presentation.md --html -o presentation.html

# Open in browser and print to PDF
# Use browser's print function for best quality
```

### PDF Export Options

```bash
# A4 page size
marp presentation.md --pdf --theme-set custom-theme.css

# With speaker notes
marp presentation.md --pdf --pdf-notes

# With bookmarks
marp presentation.md --pdf --pdf-outlines
```

---

## 🎛️ Font Scaling System

### How It Works

The template uses a single CSS variable `--base-scale` to control ALL font sizes:

```css
:root {
  --base-scale: 1; /* Change this ONE value */
}
```

### Scaling Options

| Scale Value | Result      | Best For                         |
| ----------- | ----------- | -------------------------------- |
| `0.8`       | 20% smaller | Dense content, technical details |
| `1.0`       | Normal size | Standard presentations           |
| `1.2`       | 20% larger  | Better readability               |
| `1.5`       | 50% larger  | Accessibility, large rooms       |

### Changing Font Scale

1. Open your presentation file
2. Find the `:root` section in the CSS
3. Change `--base-scale: 1.0` to your desired value
4. Save and export

**Example:**

```css
:root {
  --base-scale: 1.2; /* 20% larger fonts */
}
```

---

## 🎨 Customization Guide

### Quick Color Changes

```css
:root {
  --primary-color: #0288d1; /* Main theme color */
  --success-color: #27ae60; /* Green for success */
  --warning-color: #f39c12; /* Orange for warnings */
  --accent-color: #e74c3c; /* Red for emphasis */
}
```

### Brand Colors Example

```css
/* Corporate Blue Theme */
--primary-color: #003366;
--secondary-color: #0066cc;

/* Academic Green Theme */
--primary-color: #2e7d32;
--secondary-color: #4caf50;

/* Tech Dark Theme */
--primary-color: #1a1a1a;
--secondary-color: #333333;
```

### Font Family Changes

```css
section {
  font-family: "Your Font", "Fallback Font", sans-serif;
}
```

---

## 📦 Content Blocks Reference

### Available Blocks

```markdown
<!-- Primary Information -->
<div class="primary-box">
**🔵 Important Information**
Your content here
</div>

<!-- Success Messages -->
<div class="success-box">
**✅ Success Message**
Achievement or completion
</div>

<!-- Warning Messages -->
<div class="warning-box">
**⚠️ Warning**
Caution or attention needed
</div>

<!-- Critical/Danger -->
<div class="danger-box">
**🚨 Critical**
Urgent action required
</div>

<!-- Information -->
<div class="info-box">
**ℹ️ Additional Info**
Supplementary details
</div>

<!-- Highlights -->
<div class="highlight-box">
**💡 Key Insight**
Important points
</div>

<!-- Quotes -->
<div class="quote-box">
"Your quote here"
— Author Name
</div>
```

---

## 🏗️ Layout System

### Two-Column Layout

```markdown
<div class="two-column">
<div class="column">

### Left Column

- Point 1
- Point 2

</div>
<div class="column">

### Right Column

- Point A
- Point B

</div>
</div>
```

### Three-Column Layout

```markdown
<div class="three-column">
<div>

### Column 1

Content here

</div>
<div>

### Column 2

Content here

</div>
<div>

### Column 3

Content here

</div>
</div>
```

### Utility Classes

```markdown
<!-- Text alignment -->
<div class="text-center">Centered text</div>
<div class="text-right">Right-aligned text</div>

<!-- Font sizes -->
<div class="large-text">Large text</div>
<div class="small-text">Small text</div>

<!-- Image centering -->

![Image](image.jpg)
{.img-center}
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Fonts Not Scaling

**Problem:** Only some fonts change when adjusting `--base-scale`

**Solution:** Make sure all font sizes use `calc()` with the variable:

```css
font-size: calc(24px * var(--base-scale));
```

#### 2. Export Fails

**Problem:** Marp export command fails

**Solutions:**

```bash
# Install dependencies
npm install -g @marp-team/marp-cli puppeteer

# Check file path
marp "path/to/file.md" --pptx

# Use absolute paths
marp "C:\full\path\to\presentation.md" --pptx
```

#### 3. Content Blocks Not Styled

**Problem:** Content blocks appear unstyled

**Solution:** Ensure the CSS is in the `style: |` section:

```yaml
---
marp: true
style: |
  /* Your CSS here */
---
```

#### 4. Images Not Showing

**Problem:** Images don't appear in exports

**Solutions:**

```bash
# Use --allow-local-files flag
marp presentation.md --pptx --allow-local-files

# Use relative paths
![Image](./images/photo.jpg)

# Use online images
![Image](https://example.com/image.jpg)
```

#### 5. Mathematical Formulas Not Rendering

**Problem:** LaTeX math doesn't show

**Solution:** Ensure KaTeX is enabled:

```yaml
---
marp: true
math: katex
---
```

### Performance Tips

1. **Optimize Images**: Use compressed images (< 1MB each)
2. **Limit Slides**: Keep presentations under 100 slides for best performance
3. **Use Web Fonts Sparingly**: Stick to system fonts when possible
4. **Test Early**: Export frequently during development

---

## 📚 Examples

### Academic Presentation Structure

```markdown
---
marp: true
math: katex
# ... (CSS styles)
---

# Course Title

## Lecture 1: Introduction

**Instructor:** Your Name
**Date:** June 2025

---

## Learning Objectives

<div class="primary-box">
By the end of this lecture, you will:
- Understand concept A
- Apply technique B
- Solve problems of type C
</div>

---

## Key Concept

<div class="two-column">
<div class="column">

### Theory

Mathematical foundation:
$$E = mc^2$$

</div>
<div class="column">

### Application

Real-world examples and case studies

</div>
</div>
```

### Business Presentation Structure

```markdown
---
marp: true
# ... (CSS styles)
---

# Project Proposal

## Q3 2025 Initiative

**Presented by:** Your Name
**Date:** June 12, 2025

---

## Executive Summary

<div class="highlight-box">
**💡 Key Opportunity**
Market analysis shows 25% growth potential in our target sector
</div>

---

## Success Metrics

<div class="success-box">
**✅ Target Goals**
- Revenue: +$2M annually
- Market share: +15%
- Customer satisfaction: >90%
</div>
```

---

## 📞 Support & Contact

### Template Creator

- **Name:** Ahmed M. Elkholy
- **Email:** ahmed_elkholy@f-eng.tanta.edu.eg
- **Institution:** Faculty of Engineering, Tanta University

### Resources

- **Marp Documentation:** https://marp.app/
- **Marp CLI:** https://github.com/marp-team/marp-cli
- **VS Code Extension:** https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode

### License

This template system is free to use and modify for any purpose. Attribution appreciated but not required.

---

## 🚀 Quick Reference Commands

```bash
# Install Marp
npm install -g @marp-team/marp-cli

# Export to PowerPoint
marp presentation.md --pptx

# Export to PDF
marp presentation.md --pdf

# Export to HTML
marp presentation.md --html

# Watch and auto-export
marp -w presentation.md --pptx

# High quality with local files
marp presentation.md --pptx --allow-local-files

# Export all files
marp *.md --pptx

# Custom output name
marp input.md --pptx -o "Custom Name.pptx"
```

---

**Happy Presenting! 🎯✨**

_This README covers everything you need to create professional presentations with the Ultimate Marp Template System. For additional help or feature requests, please contact the template creator._
