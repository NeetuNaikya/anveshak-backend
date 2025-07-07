def build_knowledge_graph(entities, relationships):
    from neo4j import GraphDatabase

    uri = "bolt://localhost:7687"  # Update if deploying
    driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

    with driver.session() as session:
        for entity in entities:
            session.run("MERGE (e:Entity {name: $name})", {"name": entity})

        for rel in relationships:
            session.run("""
                MATCH (a:Entity {name: $from}), (b:Entity {name: $to})
                MERGE (a)-[:RELATIONSHIP {type: $type}]->(b)
            """, {
                "from": rel["from"],
                "to": rel["to"],
                "type": rel["type"]
            })

    driver.close()
