# Anthropic Economic Index Analysis

This repository contains code and analysis for working with Anthropic's Economic Index dataset, which provides insights into how AI is being incorporated into real-world tasks across the modern economy.

## About the Anthropic Economic Index

The Anthropic Economic Index is a dataset that explores:
- How AI is impacting different occupations and tasks
- Patterns of automation vs. augmentation across different job sectors
- The use of "extended thinking" features in AI assistants across different tasks
- Hierarchical clustering of AI-assisted tasks across the economy

The dataset is published by Anthropic and available on [Hugging Face](https://huggingface.co/datasets/Anthropic/EconomicIndex).

## Repository Structure

- `data/`: Directory for downloaded datasets (not committed to GitHub)
- `notebooks/`: Jupyter notebooks for analysis
- `scripts/`: Utility scripts for data downloading and processing
- `visualizations/`: Generated visualizations and figures

## Getting Started

### Prerequisites

- Python 3.8+
- Required packages: pandas, numpy, matplotlib, seaborn, jupyterlab, huggingface_hub

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/keshav84652/anthropic-economic-index-analysis.git
   cd anthropic-economic-index-analysis
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Download the dataset:
   ```
   python scripts/download_data.py
   ```

4. Start exploring the data with Jupyter notebooks:
   ```
   jupyter lab
   ```

## Analysis Examples

The `notebooks/` directory contains example analyses:

- `01_exploratory_analysis.ipynb`: Initial exploration of the Economic Index dataset
- `02_automation_augmentation_analysis.ipynb`: Analysis of automation vs. augmentation patterns
- `03_cluster_analysis.ipynb`: Working with the hierarchical cluster data

## Data Dictionary

The dataset includes several key files:

### Automation vs. Augmentation by Task

This file maps tasks to different collaboration patterns:

- **directive**: Automation pattern where AI directly performs the task
- **feedback_loop**: Automation pattern with human-AI interaction loops
- **validation**: Augmentation pattern where AI assists with verification
- **task_iteration**: Augmentation pattern where AI helps refine work
- **learning**: Augmentation pattern where AI provides educational support

### Cluster Level Data

Hierarchical clustering of tasks with metrics including:

- Percentage of records and users associated with each cluster
- Mapping to O*NET occupational tasks
- Collaboration pattern ratios
- Usage of "extended thinking" features

## Model Context Protocol (MCP)

This project uses a "Model Context Protocol" approach, which means:

1. We're analyzing how AI models utilize and interpret their context to perform different tasks
2. We're exploring patterns of human-AI collaboration across different occupational contexts
3. We're examining how the "extended thinking" mode in Claude 3.7 Sonnet is used across different tasks

## License

This project is MIT licensed. The original Anthropic Economic Index dataset is licensed under CC-BY.

## Acknowledgements

- Anthropic for creating and publishing the Economic Index dataset
- The Hugging Face team for hosting the dataset
