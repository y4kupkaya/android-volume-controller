# 🤝 Contributing to Android Volume Controller

Thank you for your interest in contributing to Android Volume Controller! 🎉 We welcome contributions from developers of all skill levels. This guide will help you get started.

## 🌟 Ways to Contribute

### 🐛 Bug Reports
- Report bugs through [GitHub Issues](https://github.com/y4kupkaya/android-volume-controller/issues)
- Include detailed reproduction steps
- Provide system information (Windows version, Python version, Android device)
- Attach relevant log files

### ✨ Feature Requests
- Suggest new features through [GitHub Issues](https://github.com/y4kupkaya/android-volume-controller/issues)
- Explain the use case and benefits
- Provide mockups or examples if applicable

### 💻 Code Contributions
- Fix bugs and implement new features
- Improve documentation
- Add tests and examples
- Optimize performance

### 📚 Documentation
- Improve README files
- Add code comments
- Create tutorials and guides
- Translate documentation

## 🚀 Getting Started

### 1. 🍴 Fork the Repository

Click the "Fork" button on the [GitHub repository](https://github.com/y4kupkaya/android-volume-controller) to create your own copy.

### 2. 🔄 Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/android-volume-controller.git
cd android-volume-controller
```

### 3. 🌿 Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-number
```

### 4. 🛠️ Set Up Development Environment

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks (optional but recommended)
pre-commit install
```

## 📝 Development Guidelines

### 🐍 Python Code Style

- Follow **PEP 8** style guidelines
- Use **type hints** where appropriate
- Write **descriptive variable names**
- Add **docstrings** to all functions and classes

```python
def set_android_volume(self, volume_level: int) -> bool:
    """
    Set the Android device volume level.
    
    Args:
        volume_level (int): Target volume level (0-max_volume)
        
    Returns:
        bool: True if successful, False otherwise
    """
    # Implementation here
```

### 🧪 Testing

- Write tests for new features and bug fixes
- Ensure all existing tests pass
- Test on different Android devices when possible
- Include both unit tests and integration tests

```bash
# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=android_volume_controller
```

### 📋 Code Review Checklist

Before submitting your pull request, ensure:

- [ ] ✅ Code follows PEP 8 style guidelines
- [ ] 📝 All functions have proper docstrings
- [ ] 🧪 Tests are included and passing
- [ ] 📚 Documentation is updated if needed
- [ ] 🔍 No debugging code or print statements left behind
- [ ] ⚡ Code is efficient and handles errors gracefully
- [ ] 🔒 Security considerations are addressed

## 🔄 Pull Request Process

### 1. 📤 Submit Your Changes

```bash
# Add and commit your changes
git add .
git commit -m "feat: add support for wireless connection"

# Push to your fork
git push origin feature/your-feature-name
```

### 2. 🎯 Create Pull Request

1. Go to the original repository on GitHub
2. Click "New Pull Request"
3. Select your branch and provide a clear description
4. Link any related issues

### 3. 📋 Pull Request Template

Use this template for your pull request description:

```markdown
## 📝 Description
Brief description of changes

## 🔧 Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 💥 Breaking change
- [ ] 📚 Documentation update

## 🧪 Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Manual testing completed

## 📋 Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

## 🏷️ Commit Message Guidelines

Use **conventional commits** format:

```bash
# Format: type(scope): description

feat: add wireless connection support
fix: resolve volume synchronization issue
docs: update installation instructions
test: add unit tests for volume mapping
refactor: improve error handling logic
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `style`: Code style changes
- `perf`: Performance improvements
- `ci`: CI/CD changes

## 🐛 Issue Guidelines

### 🔴 Bug Reports

**Title**: Clear, descriptive summary
```
Volume sync fails with Samsung Galaxy S21
```

**Description Template**:
```markdown
## 🐛 Bug Description
Clear description of the bug

## 🔄 Steps to Reproduce
1. Step one
2. Step two
3. Step three

## 📱 Expected Behavior
What should happen

## 💥 Actual Behavior
What actually happens

## 🖥️ Environment
- OS: Windows 11
- Python: 3.9.7
- Device: Samsung Galaxy S21
- Android: 12

## 📋 Additional Context
Any other relevant information
```

### ✨ Feature Requests

**Title**: Descriptive feature summary
```
Add support for iOS devices
```

**Description Template**:
```markdown
## 🎯 Feature Description
Clear description of the requested feature

## 💡 Motivation
Why this feature would be useful

## 📋 Detailed Design
How you imagine this feature working

## 🔄 Alternatives Considered
Other approaches you've thought about

## 📊 Additional Context
Any other relevant information
```

## 🏗️ Project Structure

```
android-volume-controller/
├── android_volume_controller.py    # Main application
├── tests/                         # Test files
│   ├── test_volume_controller.py
│   └── test_android_connection.py
├── docs/                          # Documentation
├── examples/                      # Example scripts
├── requirements.txt               # Production dependencies
├── requirements-dev.txt           # Development dependencies
├── README.md                      # English documentation
├── README-TR.md                   # Turkish documentation
└── CONTRIBUTING.md               # This file
```

## 🧪 Testing Guidelines

### Unit Tests
```python
import pytest
from android_volume_controller import AndroidVolumeController

def test_volume_mapping():
    """Test volume range mapping functionality."""
    controller = AndroidVolumeController()
    # Test implementation
```

### Integration Tests
```python
def test_android_connection():
    """Test actual Android device connection."""
    # Requires connected device
    # Test implementation
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_volume_controller.py

# Run with coverage
pytest --cov=android_volume_controller

# Run with verbose output
pytest -v
```

## 📊 Code Coverage

We aim for **80%+ code coverage**. You can check coverage with:

```bash
# Generate coverage report
pytest --cov=android_volume_controller --cov-report=html

# View report
open htmlcov/index.html
```

## 🚀 Release Process

For maintainers only:

1. **Update Version**: Bump version in `__init__.py`
2. **Update Changelog**: Document all changes
3. **Create Tag**: `git tag v1.2.0`
4. **Push Tag**: `git push origin v1.2.0`
5. **Create Release**: Use GitHub releases

## 🤔 Questions and Support

- 💬 **General Questions**: Start a [GitHub Discussion](https://github.com/y4kupkaya/android-volume-controller/discussions)
- 🐛 **Bug Reports**: Create an [Issue](https://github.com/y4kupkaya/android-volume-controller/issues)
- 💡 **Feature Ideas**: Create an [Issue](https://github.com/y4kupkaya/android-volume-controller/issues) with feature request label

## 📜 Code of Conduct

We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Please read it before contributing.

### Our Standards

- ✅ **Be respectful** and inclusive
- ✅ **Welcome newcomers** and help them learn
- ✅ **Focus on what's best** for the community
- ✅ **Show empathy** towards other members

## 🙏 Recognition

All contributors will be:
- 🌟 **Listed** in the README acknowledgments
- 🏆 **Credited** in release notes
- 💫 **Appreciated** by the community

## 📬 Contact

**Yakup Kaya**
- 🌐 Website: [yakupkaya.me](https://yakupkaya.me)
- 📧 GitHub: [@y4kupkaya](https://github.com/y4kupkaya)
- 💼 LinkedIn: [Connect with me](https://linkedin.com/in/y4kupkaya)

---

<div align="center">

**Thank you for contributing to Android Volume Controller! 🎉**

*Every contribution, no matter how small, makes a difference!* ✨

</div>