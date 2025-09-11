from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.

    Args:
        location (str): The location to get the weather for.

    Returns:
        str: The current weather for the location.
    """
    return f"The current weather in {location} is sunny."

if __name__ == "__main__":
    mcp.run()