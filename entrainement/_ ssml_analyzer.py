# ssml_analyzer.py

import xml.etree.ElementTree as ET
from typing import List, Dict

# --- Partie 1 : Structure de base ---

class Node:
    def __init__(self, tag: str, attributes: dict = None, text: str = "", children: List['Node'] = None):
        self.tag = tag
        self.attributes = attributes if attributes else {}
        self.text = text.strip() if text else ""
        self.children = children if children else []

    def __repr__(self):
        return f"<{self.tag} {self.attributes} '{self.text}' children={len(self.children)}>"


# --- Partie 1 : Parsing SSML ---

def parse_element(element: ET.Element) -> Node:
    node = Node(
        tag=element.tag,
        attributes=element.attrib,
        text=element.text
    )
    for child in element:
        node.children.append(parse_element(child))
        if child.tail:
            # Ajoute le texte après une balise (ex: Hello <em>world</em> there)
            tail_node = Node(tag="text", text=child.tail)
            node.children.append(tail_node)
    return node


def parse_ssml(ssml_str: str) -> Node:
    root_element = ET.fromstring(ssml_str)
    return parse_element(root_element)


# --- Partie 2 : Extraction des sessions ---

def extract_sessions(root: Node) -> List[Dict]:
    sessions = []

    def traverse(node: Node):
        if node.tag == "session":
            user_id = int(node.attributes.get("user", -1))
            duration = int(node.attributes.get("duration", 0))
            content = node.text
            for child in node.children:
                content += " " + child.text
            sessions.append({
                "user": user_id,
                "duration": duration,
                "text": content.strip()
            })
        for child in node.children:
            traverse(child)

    traverse(root)
    return sessions


# --- Partie 3 : Analyse des données ---

def get_total_duration(sessions: List[Dict]) -> Dict[int, int]:
    totals = {}
    for session in sessions:
        user = session["user"]
        duration = session["duration"]
        totals[user] = totals.get(user, 0) + duration
    return totals


def top_n_users(sessions: List[Dict], n: int) -> List[int]:
    totals = get_total_duration(sessions)
    return [user for user, _ in sorted(totals.items(), key=lambda x: x[1], reverse=True)[:n]]


def average_session_duration(sessions: List[Dict]) -> float:
    if not sessions:
        return 0.0
    total = sum(s["duration"] for s in sessions)
    return total / len(sessions)


# --- Exemple d'exécution ---
if __name__ == "__main__":
    ssml = '''<speak>
      <session user="1" duration="60">Bonjour le monde</session>
      <session user="2" duration="120">Hello <emphasis>world</emphasis></session>
      <session user="1" duration="90">Comment ça va ?</session>
    </speak>'''

    root = parse_ssml(ssml)
    sessions = extract_sessions(root)

    print("Sessions extraites :", sessions)
    print("Durée totale par utilisateur :", get_total_duration(sessions))
    print("Top utilisateur(s) :", top_n_users(sessions, 1))
    print("Durée moyenne :", average_session_duration(sessions))
