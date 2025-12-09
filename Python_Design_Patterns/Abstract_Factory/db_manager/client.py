import sys
from abstract_factory import DBFactory
from factories.mysql_factory import MySQLFactory
from factories.pg_factory import PostgreSQLFactory
import logging

logging.basicConfig(level=logging.INFO)

def get_factory(db_type: str) -> DBFactory:
    if db_type == 'mysql':
        return MySQLFactory()
    elif db_type == 'postgresql':
        return PostgreSQLFactory()
    else:
        raise ValueError('Unsupported database type.')
    
def application_service(factory: DBFactory):
    connector = factory.create_connector()
    query_builder = factory.create_query_builder()
    tx_manager = factory.create_transaction_manager()

    conn = None
    try:
        conn = connector.connect()
        tx_manager.begin_transaction(conn)
        query = query_builder.build_query_stmt(table='users')
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        logging.info(f'Query results: {results}')
        tx_manager.commit(conn)
    except Exception as e:
        logging.error(f'Service error: {e}')
        if conn:
            tx_manager.rollback(conn)
    finally:
        if conn:
            connector.close(conn)

if __name__ == '__main__':
    db_type = sys.argv[1] if len(sys.argv) > 1 else 'mysql'
    factory = get_factory(db_type=db_type)
    application_service(factory=factory)