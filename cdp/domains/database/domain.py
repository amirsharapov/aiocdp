from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.database.types import (
    Database,
    DatabaseId,
    Error
)


@dataclass
class Database(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Database.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Database.enable",
            params
        )

    def execute_sql(
        self,
        database_id: DatabaseId,
        query: str
    ):
        params = {
            "databaseId": database_id,
            "query": query,
        }

        return self._send_command(
            "Database.executeSQL",
            params
        )

    def get_database_table_names(
        self,
        database_id: DatabaseId
    ):
        params = {
            "databaseId": database_id,
        }

        return self._send_command(
            "Database.getDatabaseTableNames",
            params
        )

