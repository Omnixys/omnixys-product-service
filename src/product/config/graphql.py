"""Konfiguration für GraphQL."""

from typing import Final

from strawberry.http.ides import GraphQL_IDE

from product.config.config import product_config

__all__ = ["graphql_ide"]


_graphql_toml: Final = product_config.get("graphql", {})
_graphiql_enabled: Final = bool(_graphql_toml.get("graphiql-enabled", False))

graphql_ide: Final[GraphQL_IDE | None] = "graphiql" if _graphiql_enabled else None
"""String 'graphiql', falls GraphiQL aktiviert ist, sonst None."""
