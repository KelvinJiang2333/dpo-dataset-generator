# Contributing Guide

**Language:** [中文](CONTRIBUTING.md) | **English**

Thank you for your interest in the DPO Dataset Generation Tool! We welcome all forms of contributions, including but not limited to:

- Reporting bugs
- Suggesting new features
- Submitting code improvements
- Improving documentation
- Sharing usage experiences

## Development Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dpo-dataset-generator.git
cd dpo-dataset-generator
```

### 2. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt
```

### 3. Start Development Environment

```bash
# Start backend service
cd backend
python app.py

# In another terminal, start frontend service
cd frontend
python -m http.server 8080
```

Then visit `http://localhost:8080` in your browser.

## Code Contribution Process

### 1. Fork the Repository

Click the "Fork" button in the top right corner of the repository page to fork the project to your GitHub account.

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Development

- Ensure code follows the project's coding standards
- Add necessary comments
- If it's a new feature, please update related documentation

### 4. Testing

```bash
# Ensure backend API works properly
cd backend
python app.py

# Test frontend functionality in browser
# Test main features:
# - Configure LLM connection
# - Generate DPO data
# - Edit dataset
# - Undo operations
```

### 5. Commit Code

```bash
git add .
git commit -m "feat: add new feature description"
# or
git commit -m "fix: fix bug description"
```

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Code Standards

### Python Code Standards

- Use 4 spaces for indentation
- Use snake_case for function and class naming
- Add appropriate docstrings
- Import statements should be ordered: standard library, third-party library, local modules

Example:
```python
def generate_dpo_data(question: str, temperature_a: float, temperature_b: float) -> dict:
    """
    Generate DPO data pair
    
    Args:
        question: User question
        temperature_a: Temperature for generating chosen response
        temperature_b: Temperature for generating rejected response
    
    Returns:
        Dictionary containing chosen and rejected responses
    """
    # Implementation code...
```

### JavaScript Code Standards

- Use 2 spaces for indentation
- Use const/let instead of var
- Use camelCase for function naming
- Add appropriate comments

### CSS Code Standards

- Use 2 spaces for indentation
- Use hyphen-separated class names
- Group properties by functionality

## Commit Message Standards

Please use the following format for commit messages:

```
<type>: <short description>

[optional detailed description]

[optional related issue]
```

Types include:
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation updates
- `style`: Code formatting adjustments
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Build process or auxiliary tool changes

Example:
```
feat: add streaming response support

Implemented streaming display of model generation process to improve user experience.
Includes frontend EventSource handling and backend streaming response.

Closes #123
```

## Reporting Issues

If you find bugs or have feature suggestions, please report through GitHub Issues:

1. Check if similar issues already exist
2. Use a clear title to describe the problem
3. Provide detailed reproduction steps
4. Include your environment information (OS, Python version, etc.)
5. If it's a bug, please provide error logs

### Bug Report Template

```markdown
**Description**
A brief description of the bug.

**Reproduction Steps**
1. Go to page...
2. Click button...
3. See error...

**Expected Behavior**
Describe the expected normal behavior.

**Actual Behavior**
Describe what actually happened.

**Environment Information**
- OS: [e.g., Windows 10]
- Python Version: [e.g., 3.9.0]
- Browser: [e.g., Chrome 91.0]

**Screenshots**
If applicable, add screenshots to help explain the problem.

**Additional Information**
Add any other relevant information.
```

### Feature Request Template

```markdown
**Feature Description**
A brief description of the feature you'd like to add.

**Use Case**
Describe the use case and value of this feature.

**Implementation Suggestions**
If you have implementation ideas, please describe them.

**Alternatives**
Describe other solutions you've considered.

**Additional Information**
Add any other relevant information, screenshots, or reference links.
```

## Documentation Contributions

We also welcome documentation contributions:

- Improve README.md
- Update API documentation
- Add usage examples
- Translate documentation to other languages

## Community Guidelines

Please follow these guidelines to create a friendly community environment:

- Respect all contributors
- Use friendly and inclusive language
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards other community members

## License

By contributing code, you agree that your contributions will be licensed under the MIT License.

## Contact

If you have any questions, you can contact us through:

- Create a GitHub Issue
- Send email to [maintainer email]

Thank you for your contribution!
