from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd

# Parse the XML file into a DOM document object
DOMTree = xml.dom.minidom.parse('go_obo.xml')
obo = DOMTree.documentElement

# Extract 'is_a' nodes
nodes = obo.getElementsByTagName('is_a')

# Extract 'term' nodes
terms = obo.getElementsByTagName('term')

# Initialize lists and dictionaries
id_list = []
name_list = []
defstr_list = []
childnodes_list = []
parent_dict = {}

# Iterate through 'term' nodes
for term in terms:
    # Extract ID
    ids = term.getElementsByTagName('id')
    for id in ids:
        node_id = id.childNodes[0].data

    # Find parent node
    for child in term.getElementsByTagName('is_a'):
        parent_id = child.childNodes[0].data
        if parent_id not in parent_dict:
            parent_dict[parent_id] = []
        parent_dict[parent_id].append(node_id)

    # Extract 'defstr' and check for 'autophagosome'
    defstrs = term.getElementsByTagName('defstr')
    for defstr in defstrs:
        if 'autophagosome' in defstr.childNodes[0].data:
            defstr_ = defstr.childNodes[0].data
            term_id = term.getElementsByTagName('id')[0].childNodes[0].data
            term_name = term.getElementsByTagName('name')[0].childNodes[0].data

            # Append to respective lists
            id_list.append(term_id)
            defstr_list.append(defstr_)
            name_list.append(term_name)

# Recursive function to count child nodes
def count_child_nodes(node_id, parent_dict):
    count = 0
    if node_id in parent_dict:
        count += len(parent_dict[node_id])
        for child_id in parent_dict[node_id]:
            count += count_child_nodes(child_id, parent_dict)
    return count

# Count child nodes for each ID in the order of id_list
for nodeid in id_list:
    if nodeid in parent_dict:
        childnodes_list.append(count_child_nodes(nodeid, parent_dict))
    else:
        childnodes_list.append(0)

# Create a dictionary
data = {'id': id_list, 'name': name_list, 'definition': defstr_list, 'childnodes': childnodes_list}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to Excel
df.to_excel('autophagosome.xlsx', index=False)
