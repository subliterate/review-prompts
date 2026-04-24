# Contributing

## Repository Scope

This repository packages review prompts, supporting scripts, and install helpers for Linux kernel and systemd work. Keep pull requests tightly scoped and grounded in how the prompts are actually used.

## Before Opening a Pull Request

1. Update both project trees when the same convention applies to kernel and systemd.
2. Prefer additive documentation over broad rewrites.
3. Keep setup instructions and file layout references in sync with the repository.
4. Run the local validator or the exact script checks touched by your change.

## Content Guidelines

- Prompt text should stay direct, review-oriented, and bias toward evidence over speculation.
- New files should fit the existing directory conventions: `skills/`, `slash-commands/`, `scripts/`, `patterns/`, or top-level reference notes.
- Shell and Python helpers should remain dependency-light.

## Pull Request Checklist

- State whether the change affects kernel prompts, systemd prompts, or shared infrastructure.
- Mention any mirrored paths that were intentionally kept aligned.
- Include the local verification command when scripts or repository structure change.
