import os

svg_dir = "icons"  # replace with the path to your directory containing SVGs and subdirectories.
output_dir = "pages"  # Output directory for the generated web pages.


def create_index_page(grouped_pages):
    index_content = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<title>Index</title>\n</head>\n<body>\n"
    index_content += "<h1>Index Page</h1>\n"
    for group, pages in grouped_pages.items():
        index_content += f"<h2>{group}</h2>\n<ul>\n"
        for page in pages:
            relative_page_path = os.path.join(output_dir, page)
            index_content += f"<li><a href='{relative_page_path}'>{page}</a></li>\n"
        index_content += "</ul>\n"
    index_content += "</body>\n</html>"
    with open("index.html", "w") as f:
        f.write(index_content)


def create_sub_page(directory, svgs):
    page_name = directory.replace(os.path.sep, "_") + ".html"
    page_content = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<title>{}</title>\n</head>\n<body>\n".format(
        page_name)
    page_content += f"<h1>{directory}</h1>\n<ul>\n"
    for svg in svgs:
        relative_svg_path = os.path.relpath(os.path.join(directory, svg), output_dir)
        page_content += f"<li><img src='{relative_svg_path}' alt='{svg}' title='{svg}'/></li>\n"
    page_content += "</ul>\n</body>\n</html>"
    with open(os.path.join(output_dir, page_name), "w") as f:
        f.write(page_content)
    return page_name


def main():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    grouped_pages = {}
    for subdir, _, files in os.walk(svg_dir):
        svgs = [file for file in files if file.endswith(".svg")]
        if svgs:
            rel_dir = os.path.relpath(subdir, svg_dir)
            first_folder = rel_dir.split(os.path.sep)[0]
            page_name = create_sub_page(rel_dir, svgs)
            if first_folder in grouped_pages:
                grouped_pages[first_folder].append(page_name)
            else:
                grouped_pages[first_folder] = [page_name]
    create_index_page(grouped_pages)


if __name__ == "__main__":
    main()
