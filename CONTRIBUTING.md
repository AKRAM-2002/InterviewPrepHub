# Contributing to InterviewPrepHub

We're thrilled you're interested in contributing to InterviewPrepHub! Whether you're submitting new interview questions, adding solutions, or improving existing code, your contributions are welcome.

## Table of Contents
1. [How to Contribute](#how-to-contribute)
   - [Adding New Mock Interview Problems](#adding-new-mock-interview-problems)
   - [Contributing to Existing Mock Interviews](#contributing-to-existing-mock-interviews)
   - [Contributing to Documentation](#contributing-to-documentation)
2. [Contribution Guidelines](#contribution-guidelines)
3. [Getting Started](#getting-started)
4. [License](#license)

## How to Contribute

### Adding New Mock Interview Problems

1. **Create a New Folder:**
   - In the `mock-interviews/` directory, create a new folder named after your interview problem (use hyphens to separate words, e.g., `online-cloud-reading-app`).

2. **Write the Problem Description:**
   - In the new folder, create a `README.md` file.
   - Include a detailed description of the problem, system design requirements, coding challenges, and hints if applicable.
   - Feel free to add example code or images if needed.

3. **Provide Multiple Challenges (Optional):**
   - If your mock interview problem has multiple coding challenges, break them down into separate sections within the `README.md`.

4. **Submit Solutions:**
   - In the `solutions/` folder of your mock interview problem, provide solutions to each coding challenge.
   - If possible, submit solutions in multiple programming languages (e.g., Python, Java, JavaScript, etc.).
   - Make sure your code is well-structured and easy to understand.

5. **Add Test Cases:**
   - Create a `test-cases/` folder in your interview problem's directory.
   - Include sample input/output for each coding challenge in separate text files (e.g., `pagination/input.txt`, `pagination/output.txt`).
   - Make sure the test cases can verify the correctness of the solutions.

6. **Submit a Pull Request (PR):**
   - Once you've added all relevant files, create a PR with a clear title and description summarizing the changes.
   - Mention any relevant information in the PR description.

### Contributing to Existing Mock Interviews

1. **Find the Existing Problem:**
   - Navigate to the `mock-interviews/` folder and locate the folder for the relevant interview problem.

2. **Add or Improve Solutions:**
   - If adding a new solution, place it in the `solutions/` folder of the relevant interview.
   - Ensure that your code is clean, efficient, and well-commented.
   - If modifying an existing solution, explain the improvements clearly in your pull request.

3. **Update or Add Test Cases:**
   - If needed, update the test cases in the `test-cases/` folder or add new ones.
   - Ensure the test cases cover edge cases and are well-documented.

4. **Submit a PR:**
   - Describe what you've done in the PR description.

### Contributing to Documentation

- **Fix Typos or Improve Clarity:**
  - If you find any mistakes or unclear descriptions, feel free to correct them.
  - This includes `README.md` files in mock interview problems and the main documentation.

- **Expand Hints or Explanations:**
  - If you feel an explanation or hint could be made clearer, you're welcome to add additional context.

## Contribution Guidelines

### Code Style
- Follow consistent naming conventions (use `snake_case` for Python and `camelCase` for JavaScript).
- Write readable and efficient code.
- Include comments to explain non-obvious logic.

### Testing
- Ensure that your solutions pass the provided test cases.
- If you add new solutions, provide corresponding test cases to verify correctness.

### Submitting a Pull Request
- Make sure your PR title is descriptive.
- Include a summary of your changes in the PR description.
- Ensure your branch is up-to-date with the latest version of the main branch before submitting the PR.

## Getting Started

### Fork the Repository
1. Navigate to the main page of the repository.
2. Click the "Fork" button in the upper-right corner of the page to create a copy of the repository under your GitHub account.

### Clone the Fork
```bash
git clone https://github.com/your-username/interview-prep-hub.git
```

### Create a New Branch
```bash
git checkout -b feature/your-feature-name
```

### Push Your Changes
Once you've made your changes and committed them, push the branch to your fork:
```bash
git push origin feature/your-feature-name
```

### Open a Pull Request
1. Navigate to your fork on GitHub.
2. Click on the "Pull Request" button and submit your PR.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing and helping others prepare for their interviews! Happy coding!