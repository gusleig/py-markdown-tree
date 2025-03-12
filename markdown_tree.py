#!/usr/bin/env python3
"""
Generate a Markdown-formatted directory tree structure.

This script traverses a directory and creates a Markdown-compatible
representation of the directory structure, which can be used in
documentation files.

Usage:
    python markdown_tree.py [directory_path] [max_depth] [--exclude pattern1,pattern2]

Arguments:
    directory_path: Path to the directory to scan (default: current directory)
    max_depth: Maximum depth of directories to show (default: no limit)
    --exclude: Comma-separated patterns of files/directories to exclude
"""

import os
import argparse
import fnmatch


def generate_markdown_tree(directory, exclude_patterns=None, prefix="", is_last=True, max_depth=None, current_depth=0):
    """
    Recursively generate a markdown-formatted directory tree.
    
    Args:
        directory (Path): Directory to process
        exclude_patterns (list): List of patterns to exclude
        prefix (str): Prefix to use for the current line
        is_last (bool): Whether this is the last item in the current directory
        max_depth (int): Maximum depth to traverse
        current_depth (int): Current depth in the traversal
        
    Returns:
        str: Markdown-formatted tree
    """
    if exclude_patterns is None:
        exclude_patterns = []
    
    # Check if we've reached the maximum depth
    if max_depth is not None and current_depth > max_depth:
        return ""
    
    # Get the name of the directory
    name = os.path.basename(directory)
    
    # Create the current line
    if current_depth == 0:
        # Root directory
        line = f"# {name}/\n\n```markdown\n"
        child_prefix = ""
    else:
        if is_last:
            branch = "└── "
            child_prefix = prefix + "    "
        else:
            branch = "├── "
            child_prefix = prefix + "│   "
            
        line = f"{prefix}{branch}{name}/\n"
    
    # Get all subdirectories and files
    try:
        entries = list(os.scandir(directory))
    except PermissionError:
        return line + f"{child_prefix}[Permission Denied]\n"
    
    # Separate directories and files
    directories = []
    files = []
    
    for entry in entries:
        # Skip entries matching exclude patterns
        skip = False
        for pattern in exclude_patterns:
            if fnmatch.fnmatch(entry.name, pattern):
                skip = True
                break
        if skip:
            continue
            
        if entry.is_dir() and not entry.name.startswith('.'):
            directories.append(entry.path)
        elif entry.is_file():
            files.append(entry.name)
    
    # Sort directories and files
    directories.sort()
    files.sort()
    
    # Process all subdirectories
    for i, subdir in enumerate(directories):
        is_last_dir = (i == len(directories) - 1) and not files
        line += generate_markdown_tree(
            subdir, 
            exclude_patterns, 
            child_prefix, 
            is_last_dir, 
            max_depth, 
            current_depth + 1
        )
    
    # Process all files
    for i, file in enumerate(files):
        is_last_file = (i == len(files) - 1)
        if is_last_file:
            branch = "└── "
        else:
            branch = "├── "
        line += f"{child_prefix}{branch}{file}\n"
    
    # Add closing marker for root
    if current_depth == 0:
        line += "```\n"
        
    return line


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Generate a Markdown-formatted directory tree.")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to generate tree from (default: current directory)")
    parser.add_argument("max_depth", nargs="?", type=int, default=None, help="Maximum depth to traverse (default: no limit)")
    parser.add_argument("--exclude", default="", help="Comma-separated patterns of files/directories to exclude")
    parser.add_argument("--output", help="Output file (default: stdout)")
    
    args = parser.parse_args()
    
    directory = os.path.abspath(args.directory)
    exclude_patterns = [pattern.strip() for pattern in args.exclude.split(',')] if args.exclude else []
    
    # Default patterns to exclude
    default_exclude = ['__pycache__', '*.pyc', '.git', '.idea', '.vscode', 'venv', 'env', '*.egg-info']
    exclude_patterns.extend([p for p in default_exclude if p not in exclude_patterns])
    
    # Generate the markdown tree
    markdown_tree = generate_markdown_tree(
        directory,
        exclude_patterns=exclude_patterns,
        max_depth=args.max_depth
    )
    
    # Output the result
    if args.output:
        with open(args.output, 'w') as f:
            f.write(markdown_tree)
        print(f"Tree written to {args.output}")
    else:
        print(markdown_tree)


if __name__ == "__main__":
    main()