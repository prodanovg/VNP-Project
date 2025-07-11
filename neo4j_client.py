from neo4j import GraphDatabase

class Neo4jClient:
    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="12345678"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_triples(self, triples):
        with self.driver.session() as session:
            for subj, pred, obj in triples:
                session.execute_write(self._create_single_triple, subj, pred, obj)

    @staticmethod
    def _create_single_triple(tx, subj, pred, obj):
        query = """
        MERGE (s:Entity {name: $subj})
        MERGE (o:Entity {name: $obj})
        MERGE (s)-[r:RELATION {type: $pred}]->(o)
        RETURN s, r, o
        """
        tx.run(query, subj=subj, pred=pred, obj=obj)