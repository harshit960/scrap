import re

def extract_links_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Regular expression pattern to match URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    links = re.findall(url_pattern, text)

    # Creating a dictionary with the links and their corresponding indices
    link_dict = {index + 1: link for index, link in enumerate(links)}

    return link_dict

# Example usage
file_path = 'D:/Working Stuff/url.txt'  
links_dict = extract_links_from_file(file_path)
print(links_dict)
