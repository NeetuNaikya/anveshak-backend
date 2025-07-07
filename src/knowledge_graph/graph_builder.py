def build_knowledge_graph(entities, relationships):
    """
    Build and update the knowledge graph using extracted entities and relationships.

    Args:
        entities (list): A list of entities to be added to the graph.
        relationships (list): A list of relationships to be added to the graph.

    Returns:
        None
    """
    from neo4j import GraphDatabase

    # Initialize the Neo4j driver
    uri = "bolt://localhost:7687"  # Update with your Neo4j URI
    driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))  # Update with your credentials

    with driver.session() as session:
        # Create entities in the graph
        for entity in entities:
            session.run("MERGE (e:Entity {name: $name})", name=entity)

        # Create relationships in the graph
        for rel in relationships:
            session.run("""
                MATCH (a:Entity {name: $from}), (b:Entity {name: $to})
                MERGE (a)-[:RELATIONSHIP {type: $type}]->(b)
            """, from=rel['from'], to=rel['to'], type=rel['type'])

    driver.close()

def update_knowledge_graph(new_entities, new_relationships):
    """
    Update the existing knowledge graph with new entities and relationships.

    Args:
        new_entities (list): A list of new entities to be added to the graph.
        new_relationships (list): A list of new relationships to be added to the graph.

    Returns:
        None
    """
    build_knowledge_graph(new_entities, new_relationships)  # Reuse the build function for updates

# Example usage
if __name__ == "__main__":
    entities = ["INSAT-3D", "Rainfall Estimates"]
    relationships = [{"from": "INSAT-3D", "to": "Rainfall Estimates", "type": "provides"}]
    build_knowledge_graph(entities, relationships)