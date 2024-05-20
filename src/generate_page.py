from markdown_blocks import (markdown_to_html_node,
                             extract_title
                             )
import os
# from pathlib import Path


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        from_path = os.path.join(dir_path_content, file)
        if file.endswith('.md'):
            file = file.replace('.md', '.html')
        dest_path = os.path.join(dest_dir_path, file)

        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page form {from_path} to {
          dest_path} using {template_path}")
    f = open(from_path, "r")
    t = open(template_path, "r")

    from_contents = f.read()
    template_contents = t.read()

    f.close()
    t.close()

    html_node = markdown_to_html_node(from_contents)

    title = extract_title(from_contents)
    print(html_node)
    html = html_node.to_html()

    final_html = template_contents.replace(
        "{{ Title }}", title).replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_html)

    print(f"Page generate succesfully at {dest_path}")
