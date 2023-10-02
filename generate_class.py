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


# Call the function to generate the class
# read file from group.csv

group = "azure"
# Open the csv in read mode
with open(f'{group}.csv', 'r') as file:
    """ Iterate over each line in the file
    call the generate_class function
    """
    for line in file:
        # Split the line to get the name and url
        group_name, name, url = line.split(',')
        url = ICON_SITE + url
        # Call the function to generate the class
        component = generate_class('d2', name, url)

        # Write the rendered template  to file
        filename = f'{group}.d2'
        with open(filename, 'a') as file:
            file.write(component + '\n')

