"""
Generic update function for all html files

Usage:
from update_func import update_section
update_section(section='Navbar', new_content=navbar)

"""
import logging
import os
import re


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s')


def update_section(section, new_content, directory='../'):
    """
    Update the content of a section in all HTML files in a directory
    Iterate over all HTML files in the directory
    :param section:
    :param new_content:
    :param directory:
    :return:
    """
    logging.info(f"update_func.update_section started with section={section}, directory={directory}")
    # Create start and end section tags
    start_section = f'<!-- {section} Start -->'
    end_section = f'<!-- {section} End -->'

    # Add new content to the start and end of the section if missing
    if not new_content.startswith(start_section):
        new_content = f'{start_section}\n{new_content}'
    if not new_content.endswith(end_section):
        new_content = f'{new_content}\n{end_section}'

    logging.info(f"update_func.update_section calculated start_section={start_section}, end_section={end_section}, "
                 f"working in directory={directory}")

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            logging.info(f"update_func.update_section working on file filename={filename}")
            with open(os.path.join(directory, filename), 'r') as file:
                file_content = file.read()

            # Replace the navbar content in each file with the new navbar content
            file_content = re.sub(f'{start_section}.*{end_section}', new_content,
                                  file_content, flags=re.DOTALL)

            # Write the updated content back to the file
            with open(os.path.join(directory, filename), 'w') as file:
                file.write(file_content)
    return True