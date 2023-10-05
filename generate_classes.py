import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


from jinja2 import Environment, FileSystemLoader

ICON_SITE = 'https://ppalka-lingaro.github.io'
icons_directory = Path('icons')
classes_directory = Path('classes/lingaro/common')

def snake_to_pascal_with_space(s):
    return ' '.join(word.capitalize() for word in s.split('_'))

def snake_to_pascal(s):
    return ''.join(word.capitalize() for word in s.split('_'))

def render_class(type, url, svgs):
    """ Generate a class for the icon
        read the template from file
        render the template
        write the rendered template to file
    """
    # Create an Environment object with the current directory as the template path.
    env = Environment(loader=FileSystemLoader('./templates/'))
    env.filters['snake_to_pascal_with_space'] = snake_to_pascal_with_space

    # Load the template from file.
    template = env.get_template(f'icon_{type}.jinja')
    # Render the template with the required variables.
    rendered_class = template.render(url=url, icons_list=svgs)
    return(rendered_class)



def main():
    grouped_pages = {}
    type='d2'
    group_folders = [folder.name for folder in icons_directory.iterdir() if folder.is_dir()]
    print("gf: ", group_folders)
    for folder in group_folders:
        path=f"{icons_directory}\{folder}"
        group_body=''
        for subdir, _, files in os.walk(path):
            svgs = [file for file in files if file.endswith(".svg")]
            print("svgs: ", svgs)
            if svgs:
                #print("subdir: ", subdir)
                #print("path: ", path)
                dir = os.path.basename(subdir)
                #print(f"dir:{dir}")
                #print("rd: ", dir)
                url = f"{ICON_SITE}/{path}/{dir}"
                url = url.replace("\\","/")
                #print(f"url:{url}")
                rendered_classes = render_class(type,url,svgs)
                output_file_path = f'{subdir}\{dir}.{type}'
                print("ofp: ", output_file_path)
                # Write the rendered HTML to the file
                with open(output_file_path, 'w') as file:
                    file.write(rendered_classes)

if __name__ == "__main__":
    main()
