# Native libraries
from typing import Annotated

# Third-party libraries
from pydantic import Field
from sqlglot import parse_one, transpile, errors as sqlglot_errors
from mcp.server.fastmcp import FastMCP
from sqlglot.dialects import DIALECTS

# Local application imports
from utils.prompts import get_instructions

# Initialize the FastMCP server with instructions
mcp = FastMCP(
    name="SQL-Transpiler",
    instructions=get_instructions(),
)

# tool to list all available SQL dialects supported by sqlglot
@mcp.tool(
    name="Dialects",
    description="List all available SQL dialects supported by sqlglot.",
)
def avaible_dialects() -> dict:
    """
    Return all available SQL dialects supported by sqlglot wrapped in a 'response' key.

    Returns:
        dict: A dictionary with a root key 'response' that contains the list of supported dialects and their total count.
    """
    try:
        return {
            "response": {
                "dialects": DIALECTS,
                "total_dialects": len(DIALECTS)
            }
        }
    except Exception as e:
        return {
            "error": {
                "dialects": [],
                "total": 0,
                "error": str(e)
            }
        }
    
# tool to transpile SQL queries from one dialect to another using sqlglot
@mcp.tool(
    name="Transpiler",
    description="""Transpile SQL queries from one dialect to another using sqlglot. 
        First, run the Dialects tool to check if both the source and target dialects are supported.""",
)
def transpile_sql(
    sql_query: Annotated[str, Field(description="The SQL query to transpile.")],
    from_dialect: Annotated[str, Field(description="The dialect of the input SQL query.")],
    to_dialect: Annotated[str, Field(description="The target dialect for the output SQL query.")],
) -> dict:
    """
    Transpile a SQL query from one dialect to another using sqlglot.

    Args:
        sql_query: (str): The SQL query to transpile.
        from_dialect (str): The dialect of the input SQL query. Default is 'mysql'.
        to_dialect (str): The target dialect for the output SQL query. Default is 'postgresql'.

    Returns:
        dict: A dictionary with a root key 'response' that contains the transpiled SQL query.
    """

    # Check if the provided dialects are supported
    unsupported = {
        key: f"Unsupported dialect: {dialect}."
        for key, dialect in {
            "from_dialect": from_dialect,
            "to_dialect": to_dialect
        }.items() if dialect not in DIALECTS
    }

    if unsupported:
        # Return an error if any dialect is unsupported
        return {
            "error": {
                "supported_dialects": DIALECTS,
                "unsupported_dialects": unsupported
            }
        }
    
    try:
        # Parse the SQL query
        parsed = parse_one(sql_query, read=from_dialect.lower())

        # Transpile the SQL query to the target dialect
        transpile_query = transpile(sql=sql_query, read=from_dialect.lower(), write=to_dialect.lower())[0]
        
        # Return the transpiled query along with the dialects used
        return {
            "response": {
                "transpiled_sql": transpile_query,
                "from_dialect": from_dialect,
                "to_dialect": to_dialect
            }
        }
    except sqlglot_errors.ParseError as e:
        # Handle errors during transpilation
        return {
            "error": {
                "message": f"Failed to parse the SQL query. Your {from_dialect} query may have syntax errors.",
                "details": str(e),
                "from_dialect": from_dialect,
                "to_dialect": to_dialect
            }
        }
    except Exception as e:
        # Handle any unexpected errors
        return {
            "error": {
                "message": f"An unexpected error occurred during transpilation.",
                "details": str(e),
            }
        }

# Initialize and run the server
if __name__ == "__main__":
    mcp.run(transport='stdio')