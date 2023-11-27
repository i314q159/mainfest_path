from xml.dom import minidom


def get_path(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines


def clean_path(lines):
    paths = []
    for line in lines:
        s = "/".join(line.strip().split("/")[1:-1])
        if s != "":
            paths.append(s)
    return paths


def get_xml(arr):
    doc = minidom.Document()

    manifest_node = doc.createElement('manifest')
    doc.appendChild(manifest_node)

    for item in arr:
        project_node = doc.createElement('project')

        path_attribute = doc.createAttribute('path')
        path_attribute.value = item
        project_node.setAttributeNode(path_attribute)

        name_attribute = doc.createAttribute('name')
        name_attribute.value = item
        project_node.setAttributeNode(name_attribute)

        manifest_node.appendChild(project_node)

    return doc.toprettyxml(indent="\t")


if __name__ == '__main__':
    file_path = f"./8mp_android11_path.txt"
    manifest_paths = clean_path(get_path(file_path))

    xml_str = get_xml(manifest_paths)
    with open('output.xml', 'w') as f:
        f.write(xml_str)
