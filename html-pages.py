import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

# Specify the directory you want to search
directory = Path('icons')

#svg_dir = "icons"  # replace with the path to your directory containing SVGs and subdirectories.
output_dir = "pages"  # Output directory for the generated web pages.

def generate_body_sec(path,svgs):
    """ Generate a table for the icon
        read the template from file
        render the template
        write the rendered template to file
    """
    for name in svgs:
        # extract the name of the icon from the filename

    # Create an Environment object with the current directory as the template path.
        env = Environment(loader=FileSystemLoader('./templates/'))

    # Load the template from file.
        template = env.get_template('body_section.jinja')

    # Render the template with the required variables.
        linux_path = path.replace("\\","/")
        rendered_table = template.render(path=linux_path, icons_list=svgs)
    return(rendered_table)

def generate_page(type, name, body):
    """ Generate a class for the icon
        read the template from file
        render the template
        write the rendered template to file
    """
    # Create an Environment object with the current directory as the template path.
    env = Environment(loader=FileSystemLoader('./templates/'))

    # Load the template from file.
    template = env.get_template(f'{type}.jinja')

    # Render the template with the required variables.
    rendered_class = template.render(name=name, body=body)
    return(rendered_class)

def main():
    grouped_pages = {}
    group_folders = [folder.name for folder in directory.iterdir() if folder.is_dir()]
    print("gf: ", group_folders)
    for folder in group_folders:
        path=f"{directory}\{folder}"
        group_body=''
        for subdir, _, files in os.walk(path):
            print("subdir: ", subdir)
            print("files: ", files)
            svgs = [file for file in files if file.endswith(".svg")]
            print("svgs: ", svgs)
            if svgs:
                rel_dir = os.path.relpath(subdir,path)
                print("rd: ", rel_dir)
                main_folder = rel_dir.split(os.path.sep)[0]
                print("mf: ", main_folder)
                subgroup_body = generate_body_sec(rel_dir,svgs)
                group_body = f"{group_body}\n{subgroup_body}"
        rendered_html = generate_page("icons_index",main_folder,group_body )
        output_file_path = f'{path}\{folder}.html'
        print("ofp: ", output_file_path)
        # Write the rendered HTML to the file
        with open(output_file_path, 'w') as file:
            file.write(rendered_html)

if __name__ == "__main__":
    main()
