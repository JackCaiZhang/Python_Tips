import logging
from db_manager.abstract_factory import TransactionManager

class PostgreSQLTransactionManager(TransactionManager):
    def begin_transaction(self, connection):
        try:
            connection.autocommit = False
            logging.info('PostgreSQL transaction begun.')
        except Exception as e:
            logging.error(f'Failed to begin transaction: {e}')
            raise

    def commit(self, connection):
        try:
            connection.commit()
            connection.autocommit = True
            logging.info('PostgreSQL transaction commited.')
        except Exception as e:
            logging.error(f'Failed to commit: {e}')
            self.rollback(connection)
            raise

    def rollback(self, connection):
        try:
            connection.rollback()
            connection.autocommit = True
            logging.info('PostgreSQL transaction rollback.')
        except Exception as e:
            logging.error(f'Failed to rollback: {e}')
            raise