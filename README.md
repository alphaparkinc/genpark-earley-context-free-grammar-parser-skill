# genpark-earley-context-free-grammar-parser-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-earley-context-free-grammar-parser-skill?style=social)](https://github.com/alphaparkinc/genpark-earley-context-free-grammar-parser-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Earley Context-Free Grammar Chart Parser with Arbitrary Ambiguity & Recursion

Part of the **GenPark Autonomous Natural Language Processing & Automata Theory Architecture**.

## Architecture Overview

```mermaid
graph TD
    A[Context-Free Grammar Production Rules] --> B[Initialize Chart with Start Symbol S]
    B --> C[Predictor: Expand Non-Terminal Grammar Symbols]
    C --> D[Scanner: Advance Terminal Matches from Input Stream]
    D --> E[Completer: Reduce Completed Production Backwards]
    E --> F{All Tokens Consumed & Chart Populated?}
    F -->|No| C
    F -->|Yes| G[Check Completed Start Symbol State in Chart N]
    G --> H[Acceptance of Arbitrary/Ambiguous/Recursive CFG]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies.
- **Production-Grade Design**: Type annotations, robust chart parsing, multi-pattern matching.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-earley-context-free-grammar-parser-skill.git
cd genpark-earley-context-free-grammar-parser-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
