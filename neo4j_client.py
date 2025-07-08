from neo4j import GraphDatabase, basic_auth

neo4j_uri = "neo4j+s://af421f35.databases.neo4j.io"
neo4j_user = "neo4j"
neo4j_password = "C7lGNGNUB8OS0EbryefTxTP4-Gj8iXz6M1YwxG53-LA"

class Neo4jClient:
    def __init__(self):
        self.driver = GraphDatabase.driver(neo4j_uri, auth=basic_auth(neo4j_user, neo4j_password))

    def close(self):
        self.driver.close()

    def create_triples(self, triples):
        with self.driver.session() as session:
            for subj, pred, obj in triples:
                session.write_transaction(self._create_single_triple, subj, pred, obj)

    @staticmethod
    def _create_single_triple(tx, subj, pred, obj):
        query = """
        MERGE (a:Entity {name: $subj})
        MERGE (b:Entity {name: $obj})
        MERGE (a)-[r:RELATION {type: $pred}]->(b)
        RETURN a, r, b
        """
        tx.run(query, subj=subj, obj=obj, pred=pred)
