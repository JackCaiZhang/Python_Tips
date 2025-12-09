from abc import ABC, abstractmethod

class DBConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

class QueryBuilder(ABC):
    @abstractmethod
    def build_query_stmt(self, table: str):
        pass

class TransactionManager(ABC):
    @abstractmethod
    def begin_transaction(self, connection):
        pass    # 修改：传入连接以支持事务

    @abstractmethod
    def commit(self, connection):
        pass    # 新增：提交事务

    @abstractmethod
    def rollback(self, connection):
        pass    # 新增：回滚事务

class DBFactory(ABC):
    @abstractmethod
    def create_connector(self) -> DBConnector:
        pass

    @abstractmethod
    def create_query_builder(self) -> QueryBuilder:
        pass

    @abstractmethod
    def create_transaction_manager(self) -> TransactionManager:
        pass