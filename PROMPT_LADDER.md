# 🪜 Prompt Ladder

### FlyRank Internship – Week 2 | General AI Fluency

---

## 🎯 Objective

This exercise demonstrates how a simple prompt can be systematically improved by adding **one prompt engineering layer at a time**. Each version introduces exactly one change, compares the resulting output, and reflects on its impact.

---

# 🟢 Baseline (Weak Prompt)

### Prompt

```text
Write a CRUD API.
```

### Representative Output

> Here is a simple CRUD API with Create, Read, Update, and Delete operations.

The response provided generic CRUD code without asking about the programming language, framework, project requirements, or intended audience.

### Reflection

| Question                   | Answer                                           |
| -------------------------- | ------------------------------------------------ |
| **What changed?**          | Baseline prompt with no improvements.            |
| **What improved?**         | N/A                                              |
| **What still failed?**     | The response was too generic and lacked context. |
| **What would I try next?** | Specify the goal more clearly.                   |

---

# 🔹 Version 1 — Layer: Clearer Goal

### Prompt

```text
Write a CRUD API using FastAPI.
```

### Representative Output

> The response generated a FastAPI application with CRUD endpoints and basic routing.

### Reflection

| Question                   | Answer                                                                                                                |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **What changed?**          | Added a clearer goal by specifying FastAPI.                                                                           |
| **What improved?**         | The output immediately became relevant to the technology I intended to use instead of suggesting multiple frameworks. |
| **What still failed?**     | The AI still didn't understand why I was building the project.                                                        |
| **What would I try next?** | Add real project context.                                                                                             |

---

# 🔹 Version 2 — Layer: Real Context

### Prompt

```text
Write a CRUD API using FastAPI for my FlyRank Backend Internship assignment.
```

### Representative Output

> The generated project looked more like an educational assignment and included cleaner project organization.

### Reflection

| Question                   | Answer                                                                                       |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| **What changed?**          | Added the project context.                                                                   |
| **What improved?**         | The output focused on learning and good project organization instead of only producing code. |
| **What still failed?**     | The response was difficult to follow because it wasn't organized into clear steps.           |
| **What would I try next?** | Request a structured output format.                                                          |

---

# 🔹 Version 3 — Layer: Output Format

### Prompt

```text
Write a CRUD API using FastAPI for my FlyRank Backend Internship assignment.

Explain everything step by step and include the project folder structure.
```

### Representative Output

> Step 1: Create the project directory.

> Step 2: Install FastAPI.

> Step 3: Build the models.

> Step 4: Create CRUD endpoints.

> Step 5: Run the application.

### Reflection

| Question                   | Answer                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------- |
| **What changed?**          | Specified the desired output format.                                               |
| **What improved?**         | The explanation became much easier to understand and follow during implementation. |
| **What still failed?**     | Some sections contained more detail than I needed for a beginner project.          |
| **What would I try next?** | Add constraints to make the answer more concise.                                   |

---

# 🔹 Version 4 — Layer: Constraints

### Prompt

```text
Write a CRUD API using FastAPI for my FlyRank Backend Internship assignment.

Explain everything step by step.

Include the project structure.

Keep the explanation beginner-friendly and under 500 words.
```

### Representative Output

> The response became shorter, easier to read, and focused only on the essential implementation steps.

### Reflection

| Question                   | Answer                                                                     |
| -------------------------- | -------------------------------------------------------------------------- |
| **What changed?**          | Added length and readability constraints.                                  |
| **What improved?**         | The explanation became more concise and easier to consume.                 |
| **What still failed?**     | Some useful implementation details were removed to satisfy the word limit. |
| **What would I try next?** | Define quality expectations instead of making the response shorter.        |

---

# 🔹 Version 5 — Layer: Quality Criteria

### Prompt

```text
Write a CRUD API using FastAPI for my FlyRank Backend Internship assignment.

Explain everything step by step.

Include the project structure.

Keep the explanation beginner-friendly.

Follow REST API best practices.

Comment important sections of the code.
```

### Representative Output

> The generated solution included organized project folders, RESTful endpoints, clear comments, and implementation guidance that closely matched a real backend project.

### Reflection

| Question                   | Answer                                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **What changed?**          | Added quality criteria.                                                                                             |
| **What improved?**         | The code became cleaner, more maintainable, and followed REST API conventions.                                      |
| **What still failed?**     | Adding too many quality requirements made the response longer. For a quick learning task, this reduced readability. |
| **What would I try next?** | Ask the AI to review its own solution and suggest improvements.                                                     |

> **Honest Observation:** Although the quality improved, the response became noticeably longer. This made it harder to quickly identify the implementation steps. More detail is not always better.

---

# 🏆 Final Reusable Prompt

```text
You are an experienced Backend Software Engineer.

Build a RESTful CRUD API using Python and FastAPI for a backend internship project.

Requirements:

- Follow REST API best practices.
- Organize the project using a clean folder structure.
- Implement Create, Read, Update, and Delete endpoints.
- Explain the implementation step by step.
- Include the complete project structure.
- Add comments to important sections of the code.
- Keep explanations beginner-friendly.
- After generating the solution, review it and suggest improvements for production readiness.
```

---

# 📚 What I Learned

This exercise showed me that improving prompts is most effective when changing **one variable at a time**. Small, intentional changes made it easy to see how each prompt engineering technique affected the quality of the output.

Instead of relying on trial and error, I now understand how to systematically improve prompts by refining the goal, adding context, defining output formats, applying constraints, and specifying quality expectations.

This approach will help me write more effective prompts for future software engineering and AI-assisted development tasks.
