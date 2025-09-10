## Prerequisites for Installing uv

Before installing `uv`, ensure you have the following prerequisites:

- **Python 3.8 or newer** installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
- **pip** (Python package manager) should be available. It comes bundled with most Python installations.
- **Windows users:** Add Python and pip to your system PATH for easy access from the command line.
- **Recommended:** Upgrade pip to the latest version:

```bash
python -m pip install --upgrade pip
```

Once prerequisites are met, you can install `uv` using pip:

```bash
pip install uv
```

---

## Building First MCP Server using Python

### 1. Create project structure

```bash
uv init
```

### 2. Adding virtual environment

```bash
uv venv
```

### 3. Activating Virtual Environment

```bash
.\.venv\Scripts\activate
```

### 4. Installing MCP Cli 

```bash
uv add mcp[cli]
```

### 5. Create weather.py file in current solution or project

```bash
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

```

### 6. Debug MCP server using MCP Inspector

```bash
mcp dev
```