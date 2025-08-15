# DPO Dataset Generation Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Language:** [中文](README.md) | **English**

A simple and easy-to-use web tool for generating DPO (Direct Preference Optimization) datasets. Users can configure large language model APIs through the frontend interface, generate two responses with different temperatures, and then select the better response to build high-quality DPO training datasets.

## Features

1. **Dynamic Configuration**: Frontend-configurable LLM API address, keys, model names, and temperature parameters
2. **Connection Testing**: One-click test to verify LLM API connection
3. **Dual Response Generation**: Automatically generates two candidate responses with different temperatures
4. **Multiple Options**: Support for selecting responses, editing responses, regenerating, skipping, etc.
5. **Real-time Saving**: Automatically saves user choices to DPO format JSON files
6. **Dataset Management**: Built-in dataset viewing and editing functionality
7. **Streaming Display**: Real-time display of model generation process
8. **System Prompt Editor**: Visual editor for system prompts with multiple preset templates

## System Requirements

- Python 3.7+
- LLM service compatible with OpenAI API format
- Modern browsers (Chrome, Firefox, Edge, etc.)

## Quick Start

### 1. Clone the Project

```bash
git clone https://github.com/your-username/dpo-dataset-generator.git
cd dpo-dataset-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Security Configuration

**Important: Please configure your API information first**

The project provides a configuration example file `config.example.json` with configuration templates for various LLM services. Please configure according to your actual environment.

**Security Recommendations:**
- Do not hardcode API keys in code
- Recommend storing sensitive information in environment variables
- Use HTTPS in production environments
- Regularly rotate API keys

## Starting the System

### 1. Start Backend API Server

```bash
cd backend
python app.py
```

The backend service will run on http://localhost:5000.

### 2. Open Frontend Interface

You can use any static file server to serve frontend files, for example:

```bash
# If Python is installed
cd frontend
python -m http.server 8080
```

Then visit http://localhost:8080 in your browser.

Or use tools like VS Code's Live Server plugin.

## Usage Instructions

### 1. Configure LLM Connection

1. In the "LLM Configuration" area at the top of the page, enter your API parameters:
   - **API Address**: e.g., `http://localhost:8888/v1` (vLLM) or `https://api.openai.com/v1` (OpenAI)
   - **API Key**: Your API key (please keep it safe and do not leak)
   - **Model Name**: e.g., `Qwen2-7B-Instruct`, `gpt-3.5-turbo`, etc.
   - **Temperature A**: Temperature for generating first candidate response (recommended 0.2, lower temperature, more deterministic)
   - **Temperature B**: Temperature for generating second candidate response (recommended 1.0, higher temperature, more diverse)

2. Click "Edit System Prompt" to customize AI behavior and response style:
   - Choose from preset templates: Default Assistant, Creative Writing, Technical Expert, Educational Tutor, Business Professional
   - Or write custom system prompts
   - Real-time preview of system prompt effects

3. Configuration management options:
   - **Test Connection**: Verify if API configuration is correct
   - **Save Configuration**: Save configuration to browser local storage
   - **Reset Configuration**: Restore to default configuration values
   - **Clear Configuration**: Delete all saved configuration data
   - **Export Configuration**: Export configuration as JSON file (API key not included)
   - **Import Configuration**: Import configuration from JSON file

**Note**: Configuration information is saved in the browser's local storage. Please ensure use in a trusted environment.

### 2. Generate DPO Data

1. Enter your question in the question input box and click "Submit Question"
2. The system will simultaneously generate two candidate responses and display them in real-time
3. Select the response you think is better:
   - **Select This Response**: Directly select this response as preferred
   - **Edit This Response**: Edit and then use as preferred
   - **Regenerate**: Regenerate two responses
   - **Both Similar**: Skip saving this data pair
   - **Undo**: Undo the last operation

### 3. Dataset Format

The generated dataset uses **Sharegpt format**, fully compatible with mainstream DPO training frameworks, including but not limited to:
- LLaMA-Factory
- Axolotl
- DeepSpeed-Chat
- TRL (Transformers Reinforcement Learning)

**Data Format Example:**
```json
[
  {
    "conversations": [
      {
        "from": "system",
        "value": "You are a helpful AI assistant..."
      },
      {
        "from": "human", 
        "value": "User's question"
      }
    ],
    "chosen": {
      "from": "gpt",
      "value": "High-quality response (user's preferred choice)"
    },
    "rejected": {
      "from": "gpt", 
      "value": "Lower-quality response (user's non-preferred choice)"
    }
  }
]
```

**LLaMA-Factory Configuration:**
```json
{
  "dataset_name": {
    "file_name": "dpo_simple_dataset.json",
    "formatting": "sharegpt",
    "ranking": true,
    "columns": {
      "messages": "conversations",
      "chosen": "chosen", 
      "rejected": "rejected"
    }
  }
}
```

4. After selection, data will be automatically saved to the DPO dataset

### 4. Manage Dataset

- Click the "Edit Dataset" button to view generated data
- Support viewing, editing, and deleting individual records
- Can load and save different JSON files

## Dataset Format

The generated DPO dataset is saved as a JSON file in ShareGPT format:

```json
[
  {
    "conversations": [
      {"from": "system", "value": "You are a helpful AI assistant..."},
      {"from": "human", "value": "User's question..."}
    ],
    "chosen": {"from": "gpt", "value": "Better response..."},
    "rejected": {"from": "gpt", "value": "Worse response..."}
  }
]
```

## Supported LLM Services

This tool supports any service compatible with OpenAI ChatCompletions API format:

- **OpenAI API**: GPT-3.5, GPT-4 series
- **Local vLLM Service**: Open-source models like Qwen, LLaMA, Mistral
- **Ollama Service**: Locally deployed various open-source models
- **Other Compatible Services**: Any inference service implementing OpenAI API format

## Configuration Examples

### vLLM Local Service
```
API Address: http://localhost:8000/v1
API Key: your-key
Model Name: Qwen/Qwen2-7B-Instruct
```

### OpenAI API
```
API Address: https://api.openai.com/v1
API Key: sk-your-openai-key
Model Name: gpt-3.5-turbo
```

### Ollama Service
```
API Address: http://localhost:11434/v1
API Key: ollama
Model Name: qwen2:7b
```

## Troubleshooting

If you encounter problems, please check:

1. **Backend Service**: Ensure backend/app.py is running normally on port 5000
2. **API Configuration**: Ensure LLM API address, key, and model name are correct
3. **Network Connection**: Ensure access to the configured API service
4. **Browser Console**: Check for JavaScript errors
5. **CORS Issues**: If cross-domain access has problems, check CORS settings

## Contributing

We welcome contributions in any form! Please check [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to participate in project development.

### Reporting Issues

If you find bugs or have feature suggestions, please report through [GitHub Issues](https://github.com/your-username/dpo-dataset-generator/issues).

### Development Guide

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thanks to all developers who contributed to this project.

## Security Notes

- Please do not commit code containing real API keys to public repositories
- In production environments, recommend using environment variables to manage sensitive configurations
- Regularly update dependency packages for security patches
- If security vulnerabilities are found, please contact maintainers privately

## Changelog

### v1.2.0
- Added complete configuration management features
- Support for configuration export/import (JSON format)
- Added clear configuration functionality
- Improved temperature parameter label descriptions
- Optimized configuration button layout
- Enhanced security (API keys not included in exports)

### v1.1.0
- Added visual system prompt editor
- Support for multiple preset system prompt templates (Default Assistant, Creative Writing, Technical Expert, Educational Tutor, Business Professional)
- Real-time system prompt preview
- Character count and smart reminders
- Persistent system prompt configuration

### v1.0.0
- Initial release
- Support for multiple LLM APIs
- Streaming response display
- DPO dataset generation and management
- Visual data editing interface
