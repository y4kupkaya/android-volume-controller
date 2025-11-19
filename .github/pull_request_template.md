name: Pull Request
description: Submit a pull request to improve Android Volume Controller
title: ""
body:
  - type: markdown
    attributes:
      value: |
        Thanks for contributing to Android Volume Controller! 🎉
        
        Please make sure you have read our [Contributing Guide](https://github.com/y4kupkaya/android-volume-controller/blob/main/CONTRIBUTING.md) before submitting.

  - type: dropdown
    id: type
    attributes:
      label: Type of Change
      description: What type of change does this PR introduce?
      multiple: true
      options:
        - 🐛 Bug fix (non-breaking change which fixes an issue)
        - ✨ New feature (non-breaking change which adds functionality)
        - 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
        - 📚 Documentation update
        - 🧪 Test improvements
        - 🔧 Code refactoring
        - ⚡ Performance improvement
        - 🎨 Style/formatting changes
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: Description
      description: Please provide a clear and concise description of your changes.
      placeholder: Describe what this PR does...
    validations:
      required: true

  - type: textarea
    id: motivation
    attributes:
      label: Motivation and Context
      description: Why is this change required? What problem does it solve?
      placeholder: This change is needed because...

  - type: input
    id: issue
    attributes:
      label: Related Issue
      description: Does this PR close any existing issues?
      placeholder: "Closes #123, Fixes #456"

  - type: textarea
    id: testing
    attributes:
      label: Testing
      description: How have you tested your changes?
      placeholder: |
        - [ ] Unit tests pass
        - [ ] Integration tests pass  
        - [ ] Manual testing completed
        - [ ] Tested on multiple devices
        - [ ] Tested on different Windows versions
    validations:
      required: true

  - type: textarea
    id: screenshots
    attributes:
      label: Screenshots (if applicable)
      description: Add screenshots to help explain your changes

  - type: dropdown
    id: breaking
    attributes:
      label: Breaking Changes
      description: Does this PR introduce any breaking changes?
      options:
        - "No breaking changes"
        - "Yes, breaking changes (documented below)"
    validations:
      required: true

  - type: textarea
    id: breaking-details
    attributes:
      label: Breaking Changes Details
      description: If you selected "Yes" above, please describe the breaking changes and migration path.

  - type: checkboxes
    id: checklist
    attributes:
      label: Pre-submission Checklist
      description: Please confirm the following
      options:
        - label: My code follows the project's style guidelines
          required: true
        - label: I have performed a self-review of my code
          required: true
        - label: I have commented my code, particularly in hard-to-understand areas
          required: true
        - label: I have made corresponding changes to the documentation
          required: true
        - label: My changes generate no new warnings
          required: true
        - label: I have added tests that prove my fix is effective or that my feature works
          required: true
        - label: New and existing unit tests pass locally with my changes
          required: true
        - label: Any dependent changes have been merged and published