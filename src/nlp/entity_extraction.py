from typing import List, Tuple
import spacy

# Load the spaCy model for entity recognition
nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str) -> List[Tuple[str, str]]:
    """
    Extract entities from the given text using spaCy.

    Args:
        text (str): The input text from which to extract entities.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing the entity text and its label.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def extract_relationships(entities: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """
    Extract relationships between entities. This is a placeholder function that can be expanded.

    Args:
        entities (List[Tuple[str, str]]): A list of extracted entities.

    Returns:
        List[Tuple[str, str]]: A list of tuples representing relationships between entities.
    """
    relationships = []
    # Example logic for relationship extraction can be added here
    # For now, we will return an empty list
    return relationships

def main():
    # Example usage
    text = "INSAT-3D provides Rainfall Estimates."
    entities = extract_entities(text)
    relationships = extract_relationships(entities)
    print("Entities:", entities)
    print("Relationships:", relationships)

if __name__ == "__main__":
    main()