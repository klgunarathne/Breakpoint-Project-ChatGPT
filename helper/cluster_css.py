from bs4 import BeautifulSoup
import html
import re

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