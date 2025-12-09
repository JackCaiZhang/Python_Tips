import logging
from db_manager.abstract_factory import TransactionManager

class MySQLTransactionManager(TransactionManager):
    def begin_transaction(self, connection):
        try:
            connection.start_transaction()
            logging.info('MySQL transaction begun.')
        except Exception as e:
            logging.error(f'Failed to begin transaction: {e}')
            raise

    def commit(self, connection):
        try:
            connection.commit()
            logging.info('MySQL transaction commited.')
        except Exception as e:
            logging.error(f'Failed to commit: {e}')
            self.rollback(connection)
            raise

    def rollback(self, connection):
        try:
            connection.rollback()
            logging.info('MySQL transaction rollback.')
        except Exception as e:
            logging.error(f'Failed to rollback: {e}')
            raise