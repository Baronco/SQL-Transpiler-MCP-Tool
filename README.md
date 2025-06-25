# 🚀 SQL-Transpiler MCP Tool

**SQL-Transpiler** is a MCP tool designed to transpile SQL queries between different dialects using the [`sqlglot`](https://github.com/tobymao/sqlglot) library. This tool helps you convert SQL code from one dialect (e.g., MySQL) to another (e.g., PostgreSQL) with ease, ensuring compatibility across various database systems.

---

## 🛠️ Features

- **Dialect Support:** Lists all SQL dialects supported by `sqlglot`.
- **SQL Transpilation:** Converts SQL queries from one dialect to another.
- **Error Handling:** Informs you if a dialect is unsupported or if there are syntax errors.

---

## 📦 Library Used

- [`sqlglot`](https://github.com/tobymao/sqlglot)  
  **Version:** _Check your `pyproject.toml` or `uv.lock` for the exact version used in this project._

---

## ⚙️ Prerequisites

- **Python 3.13+** (if running locally)
- **[UV](https://github.com/astral-sh/uv)** package manager (for dependency management)
- **Docker** (if running via container)

---

## 🚀 Installation

### Option 1: Using UV (Locally)

1. **Clone the repository**  
   ```sh
   git clone https://github.com/Baronco/SQL-Transpiler-MCP-Tool.git
   cd sql-transpiler
   ```

1. **Install UV**  
   ```sh
   pip install uv

1. **Sync dependencies (using `uv.lock`)**  
   ```sh
   uv sync --frozen

1. **Run the server**  
   ```sh
   uv run server.py

### Option 2:  Using Docker

1. **Clone the repository**  
   ```sh
   git clone https://github.com/your-username/sql-transpiler.git
   cd sql-transpiler
   ```

1. **Build the Docker image**  
   ```sh
   docker build -t sql-transpiler .

## 📄 Usage

- Use the `Dialects` tool to list all supported SQL dialects.
- Use the `Transpiler` tool to convert SQL queries from one dialect to another.

*For more details, see the instructions in `src/instructions.md`.*

### 🖥️ Integration with Claude Desktop

To add the SQL-Transpiler MCP tool to your Claude Desktop configuration using the Docker image, update your `claude_desktop_config.json` as follows:


```json
{
  "mcpServers": {
    "sql-transpiler": 
    {
      "command": "docker",
      "args": ["run", "-i", "--rm", "--init", "-e", "DOCKER_CONTAINER=true", "sql-transpiler"]
    }
  }
}
```

If you want to use your local environment with [UV](https://github.com/astral-sh/uv) instead of Docker, configure your `claude_desktop_config.json` like this (adjust the path as needed):

```json
{
  "mcpServers": {
    "sql-transpiler": 
    {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/sql-transpiler",
        "run",
        "server.py"
      ]
    }
  }
}
```

## 📝 License
MIT License