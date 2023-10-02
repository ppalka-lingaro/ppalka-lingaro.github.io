import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


from jinja2 import Environment, FileSystemLoader

ICON_SITE = 'https://icons.terrastruct.com/'

def generate_class(type, name, url):
    """ Generate a class for the icon
        read the template from file
        render the template
        write the rendered template to file
    """
    # Create an Environment object with the current directory as the template path.
    env = Environment(loader=FileSystemLoader('.'))

    # Load the template from file.
    template = env.get_template(f'{type}.jinja')

    # Render the template with the required variables.
    rendered_class = template.render(name=name, url=url)
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
        rendered_html = generate_page("icons_index",folder,group_body )
        output_file_path = f'{path}\{folder}.html'
        print("ofp: ", output_file_path)
        # Write the rendered HTML to the file
        with open(output_file_path, 'w') as file:
            file.write(rendered_html)

if __name__ == "__main__":
    main()
