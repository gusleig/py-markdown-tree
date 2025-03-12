# Markdown Tree Generator

A simple Python utility to generate Markdown-formatted directory trees for documentation purposes.

This is very usefull to add the project files and folder structure in a way that Artificial Ingelligence can read.

Whe using cursor or windsurf, add the generated file to your project readme.md and see the results for yourself.

ps: I found out that the tree command in macos works the same way, but this was fun to create.

## Features

- Creates well-formatted directory trees in Markdown syntax
- Customizable depth limits for large projects
- File/directory exclusion patterns
- Automatic skipping of common unnecessary files (`.git`, `__pycache__`, etc.)
- Output to file or stdout
- Pure Python - no external dependencies required

## Installation

No installation required! Just download the script and run it with Python 3.6+:

```bash
# Clone or download this repository
git clone https://github.com/gusleig/markdown-tree-generator.git

# Navigate to the directory
cd markdown-tree-generator

# Make the script executable (Linux/macOS)
chmod +x markdown_tree.py
```

## Usage

### Basic Usage

```bash
python markdown_tree.py /path/to/your/project
```

By default, this will scan the current directory and print the tree to stdout.

### Command Line Options

```
usage: markdown_tree.py [-h] [--exclude EXCLUDE] [--output OUTPUT] [directory] [max_depth]

Generate a Markdown-formatted directory tree.

positional arguments:
  directory          Directory to generate tree from (default: current directory)
  max_depth          Maximum depth to traverse (default: no limit)

optional arguments:
  -h, --help         show this help message and exit
  --exclude EXCLUDE  Comma-separated patterns of files/directories to exclude
  --output OUTPUT    Output file (default: stdout)
```

### Examples

**Generate tree with depth limit of 3:**
```bash
python markdown_tree.py /path/to/project 3
```

**Exclude specific patterns:**
```bash
python markdown_tree.py --exclude "*.log,*.tmp,node_modules"
```

**Save output to a file:**
```bash
python markdown_tree.py --output project_structure.md
```

**Combine options:**
```bash
python markdown_tree.py /path/to/project 4 --exclude "dist,build" --output docs/structure.md
```

## Example Output

```markdown
# my-project/

├── src/
│   ├── components/
│   │   ├── Button.js
│   │   └── Header.js
│   ├── utils/
│   │   └── helpers.js
│   └── index.js
├── tests/
│   └── unit/
│       └── helpers.test.js
├── .gitignore
├── package.json
└── README.md
```

## Default Exclusions

The script automatically excludes these common patterns:
- `__pycache__`
- `*.pyc`
- `.git`
- `.idea`
- `.vscode`
- `venv`
- `env`
- `*.egg-info`

You can override or add to these with the `--exclude` option.

## Use Cases

- Project documentation
- README files
- Onboarding new team members
- Code reviews
- Project structure planning

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## License

MIT License

## Author

Gustavo Leig