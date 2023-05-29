import os
import re
import csv


def clusterCSSCode(css_data):
    # Remove comments from CSS data
    css_data = re.sub(r"/\*.*?\*/", "", css_data, flags=re.DOTALL)

    css_blocks = css_data.split('}')  # Split into individual CSS blocks

    css_groups = []
    current_group = ''
    for block in css_blocks:
        block = block.strip()
        if block:
            current_group += block + '}'
            if '{' in block:
                css_groups.append(current_group)
                current_group = ''

    # Filter out CSS groups with empty selectors
    filtered_groups = []
    for group in css_groups:
        selector_start = group.find('{') + 1
        selector_end = group.find('}')
        selector = group[selector_start:selector_end].strip()
        if selector:
            filtered_groups.append(group)

    return filtered_groups

file_paths = [
    "./testing_sites/3. Amazon/css/style.css",
    "./testing_sites/3. Cash App/css/style.css",
    "./testing_sites/3. Clearbit - responsive/css/style.css",
    "./testing_sites/3. Glamnetic/assets/css/style.css",
    "./testing_sites/3. Gmail/css/index.css",
    "./testing_sites/3. Grammarly/css/d1200.css",
    "./testing_sites/3. Gymshark - responsive/css/style.css",
    "./testing_sites/3. Huel/style.css",
    "./testing_sites/3. LegalZoom/css/style.css",
    "./testing_sites/3. Lemonade/assets/css/style.css",
    "./testing_sites/3. Netlify/style.css",
    "./testing_sites/3. Pipedrive/style.css",
    ]

for path in file_paths:
    # Replace with the actual file path
    print(path)
    file_path = path
    file_contents = ""

    csv_file_path = "./datasets/dataset.csv"

    # List of dictionaries representing each row in the CSV
    rows = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

    css_data = clusterCSSCode(file_contents)

    prompt = ''
    completion = ''

    for group in css_data:
        grop = str(group).strip().replace('\n', '')
        prompt = f"""
        Below is the CSS attributes for a media query with a width of X. Give me the CSS attributes for media queries for widths of 375px, 480px, 620px, 768px, 990px, 1200px, 1400px, 1600px, and 1920px.\n{grop}"""

        completion = "@media (max-width: 375px) {\n" + grop + "\n}\n"
        completion += "@media (min-width: 376px) and (max-width: 480px) {\n" + grop + "\n}\n"
        completion += "@media (min-width: 481px) and (max-width: 620px) {\n" + grop + "\n}\n"
        completion += "@media (min-width: 621px) and (max-width: 768px) {\n" + grop + "\n}\n"
        completion += "@media (min-width: 769px) and (max-width: 990px) {\n" + grop + "\n}\n"
        completion += "@media (min-width: 991px) and (max-width: 1200px) {\n" + grop + "\n}\n"
        completion += "@media (min-width: 1201px) and (max-width: 1400px) {\n" + grop + "\n}\n"
        completion += "@media (min-width: 1401px) and (max-width: 1600px) {\n" + grop + "\n}\n"
        completion += "@media (min-width: 1601px) and (max-width: 1920px) {\n" + grop + "\n}"
        
        # completion = """
        # @media (max-width: 375px) {\n""" + grop + """
        # }
        # @media (min-width: 376px) and (max-width: 480px) {\n""" + grop + """
        # }
        # @media (min-width: 481px) and (max-width: 620px) {\n""" + grop + """
        # }
        # @media (min-width: 621px) and (max-width: 768px) {\n""" + grop + """
        # }
        # @media (min-width: 769px) and (max-width: 990px) {\n""" + grop + """
        # }
        # @media (min-width: 991px) and (max-width: 1200px) {\n""" + grop + """
        # }
        # @media (min-width: 1201px) and (max-width: 1400px) {\n""" + grop + """
        # }
        # @media (min-width: 1401px) and (max-width: 1600px) {\n""" + grop + """
        # }
        # @media (min-width: 1601px) and (max-width: 1920px) {\n""" + grop + """
        # }
        # """
        
        rows.append([prompt.strip(), completion.strip()])  # Remove extra whitespace
        
    # Check if the CSV file exists
    file_exists = os.path.isfile(csv_file_path)

    # Read existing rows if the file exists
    existing_rows = []
    if file_exists:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            existing_rows = list(reader)

    # Combine existing rows and new rows
    combined_rows = existing_rows + rows

    # Write the combined rows to the CSV file
    try:
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["prompt", "completion"])  # Write header row
            writer.writerows(combined_rows)  # Write the combined rows
        print("CSV file created/updated successfully.")
    except IOError:
        print("Error creating/updating the CSV file.")