from neo4j import GraphDatabase

neo4j_uri = "neo4j+s://af421f35.databases.neo4j.io"
neo4j_user = "neo4j"
neo4j_password = "C7lGNGNUB8OS0EbryefTxTP4-Gj8iXz6M1YwxG53-LA"


def main():
    try:
        driver = GraphDatabase.driver(
            "neo4j+s://af421f35.databases.neo4j.io",
            auth=(neo4j_user, neo4j_password)
        )

        with driver.session() as session:
            result = session.run("RETURN 1 AS test")
            record = result.single()
            print("Test query result:", record["test"])
        driver.close()
        print("Connection successful!")
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    main()
