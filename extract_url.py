import re
import os
from bs4 import BeautifulSoup

# Function to extract the URL
def extract_url(line):
    # Regular expression to match the value inside clickIcon("...")
    pattern = re.compile(r'clickIcon\("([^"]+)"\)')
    match = pattern.search(line)
    if match:
        return match.group(1)
    else:
        return None

    # Regular expression to match the value inside data-search="..."

def extract_title(line):
    match = re.search('data-search=\"(.*?)\".*?oneclick', line)
    if match:
        title = match.group(1)
        return title
    else:
        return None

def extract_icon(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='icon')

    if div and 'onclick' in div.attrs:
        onclick_value = div.attrs['onclick']
        match = re.search(r'\"(.*?)\"', onclick_value)
        if match:
            url = match.group(1)
        title = div.attrs['data-search']
        return(title,url)

# Open the file in read mode
with open('source.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Check if the line starts with <div class
        if line.strip().startswith('<div class=icon data-search'):
            # Call the function to extract the URL
            title,url = extract_icon(line)
            # Print the URL if it is not None
            if url:
                group = url.split('%2')[0]
                filename = group + ".csv"
                with open(filename, 'a') as f:
                    f.write(f"{group},{title},{url} \n")
