#!/usr/bin/env python3
"""
Generate markdown table of hackathon participants' portfolio information.

Usage:
    python generate_portfolio_table.py <csv_file> <start_date>

Example:
    python generate_portfolio_table.py attendee.csv 2025-12-22
"""

import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime
from typing import Optional


def get_github_user_info(username: str) -> Optional[dict]:
    """Fetch GitHub user information using gh CLI."""
    try:
        result = subprocess.run(
            ["gh", "api", f"users/{username}", "--jq", "{login, name, html_url}"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        pass
    return None


def get_user_repos(username: str, start_date: str) -> list[dict]:
    """Fetch user's repositories created after start_date."""
    try:
        result = subprocess.run(
            [
                "gh",
                "api",
                f"users/{username}/repos",
                "--jq",
                f'.[] | select(.created_at >= "{start_date}") | {{name, html_url, has_pages}}',
            ],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0 and result.stdout.strip():
            repos = []
            for line in result.stdout.strip().split("\n"):
                if line:
                    repos.append(json.loads(line))
            return repos
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        pass
    return []


def generate_github_pages_url(username: str, repo_name: str) -> str:
    """Generate GitHub Pages URL for a repository."""
    return f"https://{username.lower()}.github.io/{repo_name}/"


def parse_csv(csv_path: str) -> list[dict]:
    """Parse CSV file and return unique attendees."""
    attendees = {}
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            github_id = row.get("GitHub 어카운트 (Username)", "").strip()
            name = row.get("이름", "").strip()
            if github_id and " " not in github_id:  # Skip invalid IDs with spaces
                if github_id not in attendees:
                    attendees[github_id] = {"github_id": github_id, "name": name}
    return list(attendees.values())


def generate_markdown_table(attendees: list[dict], start_date: str) -> str:
    """Generate markdown table with portfolio information."""
    lines = [
        "| GitHub ID | 이름 | 포트폴리오 리포지토리 | GitHub Pages |",
        "|-----------|------|----------------------|--------------|",
    ]

    for attendee in attendees:
        github_id = attendee["github_id"]
        name = attendee["name"]

        # Check if user exists
        user_info = get_github_user_info(github_id)
        if not user_info:
            print(f"Warning: GitHub user '{github_id}' not found", file=sys.stderr)
            continue

        # Get repositories
        repos = get_user_repos(github_id, start_date)
        if not repos:
            print(
                f"Warning: No repos found for '{github_id}' after {start_date}",
                file=sys.stderr,
            )
            continue

        # Format repository links
        repo_links = []
        pages_links = []
        for repo in repos:
            repo_name = repo["name"]
            repo_url = repo["html_url"]
            repo_links.append(f"[{repo_name}]({repo_url})")

            if repo.get("has_pages"):
                pages_url = generate_github_pages_url(github_id, repo_name)
                pages_links.append(f"[{repo_name}]({pages_url})")

        github_profile = f"[{github_id}](https://github.com/{github_id})"
        repos_str = ", ".join(repo_links) if repo_links else "-"
        pages_str = ", ".join(pages_links) if pages_links else "-"

        lines.append(f"| {github_profile} | {name} | {repos_str} | {pages_str} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate markdown table of hackathon participants' portfolio information"
    )
    parser.add_argument("csv_file", help="Path to the CSV file with attendee information")
    parser.add_argument(
        "start_date",
        help="Start date for filtering repositories (YYYY-MM-DD format)",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file path (default: stdout)",
        default=None,
    )

    args = parser.parse_args()

    # Validate date format
    try:
        datetime.strptime(args.start_date, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{args.start_date}'. Use YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    # Parse CSV
    try:
        attendees = parse_csv(args.csv_file)
    except FileNotFoundError:
        print(f"Error: CSV file not found: {args.csv_file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(attendees)} unique attendees", file=sys.stderr)

    # Generate table
    table = generate_markdown_table(attendees, args.start_date)

    # Output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(table)
        print(f"Table written to {args.output}", file=sys.stderr)
    else:
        print(table)


if __name__ == "__main__":
    main()
