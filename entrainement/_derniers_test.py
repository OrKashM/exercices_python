# derniers_test.py

# 1. Créer une classe pour les balises

class Node:
    def __init__(self, tag, attributes=None, text="", parent=None, children=None):
        self.tag = tag
        self.attributes = attributes or {}
        self.text = text
        self.children = children or []

    def __repr__(self):
        return f"<{self.tag}>{self.text}{self.children}</{self.tag}>"
    
    def traverse(self, indent = 0):
        space = "  " * indent
        attrs = " " + " ".join(f'{k}="{v}"' for k, v in self.attributes.items()) if self.attributes else ""
        print(f"{space}<{self.tag}{attrs}>")

        if self.text.strip():
            print(f"{space}  {self.text.strip()}")
        for child in self.children :
            child.traverse(indent + 1)
        print(f"{space}</{self.tag}>")
    
# 2. Parser une chaîne ssml en la transformant en un élément ET puis en appliquant buildtree sur l'élément

def parserssml(ssml)-> Node :
    from xml.etree import ElementTree as ET
    def buildtree(elem_tree):
        node = Node(
            tag=elem_tree.tag,
            attributes=elem_tree.attrib,
            children=[buildtree(child) for child in elem_tree],
            text=elem_tree.text.strip() if elem_tree.text else "",
        )
        return node
    root_tree = ET.fromstring(ssml)
    return buildtree(root_tree)

# 3. Créer un noeud pour les balises en voulant effectuer une traversée DOM

class NodeDOM:
    def __init__(self, tag, attributes=None, text="", parent=None, children=None):
        self.tag = tag
        self.attributes = attributes or {}
        self.text = text
        self.children = children or []
        self.parent = parent

    def addchild(self, childnode):
        childnode.parent = self
        self.children.append(childnode)

    def traverse_dom(self):
        print(f"<{self.tag}>")
        for child in self.children :
            child.traverse()


# --- Exemple d'exécution ---
if __name__ == "__main__":
    xssml = '''<speak><p>Hello <emphasis level="strong">world</emphasis></p></speak>'''

    olivier=parserssml(xssml)

    print("extraites :", olivier)

    olivier.traverse()