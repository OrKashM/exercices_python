# _test_ssml_parser

class Node:
    def __init__(self, tag, attributes=None, children=None, text=""):
        self.tag = tag
        self.attributes = attributes or {}
        self.children = children or []
        self.text = text

    def __repr__(self):
        return f"<{self.tag}>{self.text} {self.children}</{self.tag}>"
    
    def pretty_print(self, indent=0):
        space = "  " * indent
        attrs = " " + " ".join(f'{k}="{v}"' for k, v in self.attributes.items()) if self.attributes else ""
        print(f"{space}<{self.tag}{attrs}>")

        if self.text.strip():
            print(f"{space}  {self.text.strip()}")

        for child in self.children:
            child.pretty_print(indent + 1)

        print(f"{space}</{self.tag}>")

def parse_ssml(ssml):
    from xml.etree import ElementTree as ET
    def build_tree(elem):
        node = Node(
            tag=elem.tag,
            attributes=elem.attrib,
            children=[build_tree(child) for child in elem],
            text=elem.text.strip() if elem.text else ""
        )
        return node
    root = ET.fromstring(ssml)
    return build_tree(root)



# --- Exemple d'exécution ---
if __name__ == "__main__":
    xssml = '''<speak><p>Hello <emphasis level="strong">world</emphasis></p></speak>'''

    olivier=parse_ssml(xssml)

    print("extraites :", olivier)

    olivier.pretty_print()
