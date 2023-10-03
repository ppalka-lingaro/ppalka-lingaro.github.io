import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


from jinja2 import Environment, FileSystemLoader

ICON_SITE = 'https://ppalka-lingaro.github.io'
icons_directory = Path('icons')
classes_directory = Path('classes/lingaro/common')

def render_class(type, url, svgs):
    """ Generate a class for the icon
        read the template from file
        render the template
        write the rendered template to file
    """
    # Create an Environment object with the current directory as the template path.
    env = Environment(loader=FileSystemLoader('./templates/'))

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
                rel_dir = os.path.relpath(subdir,path)
                print("rd: ", rel_dir)
                main_folder = rel_dir.split(os.path.sep)[0]
                print("mf: ", main_folder)
                url = f"{ICON_SITE}/{path}/{rel_dir}"
                url = url.replace("\\","/")
                print(f"url:{url}")
                rendered_classes = render_class(type,url,svgs)

                #subgroup_body = generate_body_sec(rel_dir,svgs)
                #group_body = f"{group_body}\n{subgroup_body}"
                #rendered_html = generate_page("icons_index",folder,group_body )
                # split the main_folder to get the group name
                output_file_path = f'{path}\{main_folder}\{main_folder}.{type}'
                print("ofp: ", output_file_path)
                # Write the rendered HTML to the file
                with open(output_file_path, 'w') as file:
                    file.write(rendered_classes)

if __name__ == "__main__":
    main()
