# AGENTS.md

## Project Working Preferences

1. Use built-in VS Code command flow first
- Prefer built-in VS Code command-based editing so file changes are clearly visible in the editor.
- Make incremental edits in small, reviewable steps.

2. Keep code clean and structured
- Write simple, well-organized code with clear function boundaries.
- Favor readability over cleverness.
- Use descriptive names and consistent formatting.

3. Target readability for a 2nd-year student
- Keep logic easy to follow.
- Avoid unnecessary abstractions and advanced patterns unless truly needed.
- Add short comments only when they clarify non-obvious logic.

4. Handle edge cases carefully (but not fancy)
- Validate inputs and parsed data.
- Handle missing fields, empty datasets, and unexpected formats gracefully.
- Provide clear error messages for failure paths.

5. Prefer pragmatic implementation
- Solve the task requirements directly before optional improvements.
- Avoid over-engineering, extra layers, or speculative features.

6. Maintain basic engineering hygiene
- Use explicit type hints in Python.
- Keep functions small and testable.
- Ensure the script runs end-to-end without manual fixes.

7. Suggest commit name after code changes
- After every code change, end the response with one clean, descriptive commit name suggestion.

8. Log every user prompt
- After any user prompt, update prompts.md to log the prompt using the project template.
