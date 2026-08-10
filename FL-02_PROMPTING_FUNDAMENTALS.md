# 🚀 FL-02: Prompting Fundamentals on Real Tasks v2

**Track:** General AI Fluency
**Phase:** Foundations
**Week:** 2
**Estimated Workload:** 6 Hours

---

# 📌 Objective

This assignment demonstrates how prompt engineering techniques improve AI-generated responses when applied to a real software engineering task. Rather than changing many things at once, each iteration introduces one specific prompting technique and evaluates its effect on the generated output.

---

# 🛠️ Real Task (From FL-01)

**Task:** Build a RESTful CRUD API using Python and FastAPI.

This task was originally completed as part of the FlyRank Backend Engineering internship and serves as the real-world example for this exercise.

---

# 🔹 Baseline Prompt (Naive)

### Prompt

```text
Write a CRUD API.
```

### Representative Output

* Generic CRUD example.
* No programming language specified.
* No framework specified.
* No explanation.
* No project structure.

### Reflection

**Technique:** None (Baseline)

**What changed?**

This is the original one-line prompt I would have written before learning prompt engineering.

**Observed output difference**

The AI produced a generic answer that could apply to almost any technology stack. It required significant follow-up questions before it became useful.

**What I learned**

Vague prompts produce vague responses.

---

# 🔹 Version 1 — Role Assignment

### Prompt

```text
You are a Senior Backend Software Engineer.

Build a CRUD API.
```

### Representative Output

* Better engineering terminology.
* Cleaner implementation.
* More professional explanations.

### Reflection

**Technique:** Role Assignment

**What changed?**

Assigned the AI the role of an experienced Backend Software Engineer.

**Observed output difference**

The response became more technical and better organized. It focused on engineering practices rather than simply generating code.

**What I learned**

Giving the AI a role significantly changes its perspective and writing style.

---

# 🔹 Version 2 — Context & Motivation

### Prompt

```text
You are a Senior Backend Software Engineer.

I'm building my first CRUD API as part of a backend engineering internship.

Help me create a clean and beginner-friendly implementation.
```

### Representative Output

* Simpler explanations.
* Better learning focus.
* More educational guidance.

### Reflection

**Technique:** Context & Motivation

**What changed?**

Added information about the project's purpose and my experience level.

**Observed output difference**

Instead of assuming expert knowledge, the AI explained decisions and emphasized concepts that helped me understand the implementation.

**What I learned**

Context helps the AI tailor its explanations to the user's needs.

---

# 🔹 Version 3 — Few-Shot Examples

### Prompt

```text
You are a Senior Backend Software Engineer.

I'm building my first CRUD API.

Good example:

GET /tasks
Returns every task.

Follow this style for every endpoint.
```

### Representative Output

* Consistent endpoint descriptions.
* Better formatting.
* More predictable responses.

### Reflection

**Technique:** Few-Shot Examples

**What changed?**

Provided a small example of the expected style.

**Observed output difference**

The AI copied the demonstrated format throughout the response, making the documentation more consistent.

**What I learned**

Even one example strongly influences the structure and style of the output.

---

# 🔹 Version 4 — Output Structure

### Prompt

```text
You are a Senior Backend Software Engineer.

Build a CRUD API.

Return the answer using this structure:

1. Overview
2. Folder Structure
3. Dependencies
4. API Endpoints
5. Source Code
6. Testing
```

### Representative Output

* Clearly organized sections.
* Easier navigation.
* Improved readability.

### Reflection

**Technique:** Output Structure

**What changed?**

Specified the desired organization of the response.

**Observed output difference**

The response became significantly easier to follow because every topic appeared in a predictable location.

**What I learned**

Explicit structure makes long technical responses much more usable.

---

# 🔹 Version 5 — Step Decomposition

### Prompt

```text
You are a Senior Backend Software Engineer.

Build a CRUD API.

Complete one step before moving to the next.

Step 1: Explain the project.

Step 2: Create the folder structure.

Step 3: Install dependencies.

Step 4: Build the endpoints.

Step 5: Explain testing.

Step 6: Review the solution and suggest improvements.
```

### Representative Output

* Logical workflow.
* Better explanations.
* Easier implementation.

### Reflection

**Technique:** Step Decomposition

**What changed?**

Split the task into sequential steps.

**Observed output difference**

The AI produced a more methodical response that mirrored how I would actually implement the project, reducing confusion and making it easier to follow.

**What I learned**

Breaking complex tasks into smaller steps improves clarity and helps prevent skipped details.

---

# 🤖 Cross-Model Comparison

The final prompt was tested with both **Claude** and **ChatGPT**.

| Category      | Claude                                | ChatGPT                                             |
| ------------- | ------------------------------------- | --------------------------------------------------- |
| Tone          | Methodical and instructional          | Conversational and practical                        |
| Structure     | Very consistent section organization  | Flexible and easy to customize                      |
| Accuracy      | Strong conceptual explanations        | Strong implementation guidance                      |
| Best Strength | Teaching concepts clearly             | Producing practical solutions quickly               |
| Limitation    | Sometimes more verbose than necessary | Occasionally needs explicit formatting instructions |

## Overall Reflection

Both models produced useful responses, but their strengths differed.

Claude excelled at explaining concepts and maintaining a consistent structure, making it valuable for learning and documentation.

ChatGPT produced responses that were easier to adapt directly into code and practical implementation. It responded well to explicit instructions and generated concise, actionable guidance.

Choosing between them depends on whether the goal is learning a concept or accelerating implementation.

---

# 🧩 Final Reusable Prompt Template

```text
You are an experienced Backend Software Engineer.

Task:
Build a RESTful CRUD API using <Programming Language> and <Framework>.

Requirements:

- Follow REST API best practices.
- Explain the implementation step by step.
- Include a clean project structure.
- Add comments where appropriate.
- Keep explanations suitable for the target audience.
- Review the completed solution and suggest improvements.

Output Format:

1. Project Overview
2. Folder Structure
3. Dependencies
4. Source Code
5. API Endpoints
6. Testing Instructions
7. Best Practices
8. Possible Improvements
```

This template is reusable because only the programming language, framework, and project details need to be replaced.

---

# 📚 Key Takeaways

Through this exercise, I learned that effective prompt engineering is an iterative process. Small, deliberate improvements produced measurable changes in the quality of AI-generated responses.

The most valuable techniques for my software engineering workflow were:

* Role Assignment
* Context & Motivation
* Output Structure
* Step Decomposition

Together, these techniques transformed a vague request into a clear, reusable prompt capable of producing structured, high-quality technical guidance for real backend development tasks.
