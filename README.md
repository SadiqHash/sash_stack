sash_stack

Secure backend architecture template powered by sash_trust

---

What is sash_stack?

sash_stack is a secure backend foundation designed to be built and validated under sash_trust principles.

→ sash_trust (Security Rules Engine)
→ sash_stack (System built under those rules)

sash_trust defines what secure means,
sash_stack implements a real system that follows it.

---

Why sash_stack Exists?

Modern backend projects often fail because:

* Security is added later
* Secrets leak into code
* Config is inconsistent
* Encryption is misused
* Auth is loosely implemented
* CI does not enforce security

sash_stack exists to solve that.

It provides:

* Clean layered architecture
* Centralized security abstractions
* Database best practices
* Dockerized environment
* CI enforcement
* Security policy validation

---

What Problem Does sash_stack Solve?

sash_stack solves:

* Insecure backend scaffolding
* Weak authentication implementation
* Secret mismanagement
* Config sprawl
* Lack of CI security enforcement
* Inconsistent development environments

It gives developers a secure backend foundation from day one.

---

How sash_stack Uses sash_trust

sash_trust is a static security policy engine.

It scans code using:

* AST validation
* Security policy rules
* Structural enforcement

sash_stack integrates sash_trust in two ways:


1. Local CLI Enforcement

Developers run:

```bash
sash-trust run ./app policies/strict.yaml
```

This ensures:

* No insecure auth patterns
* No secret leaks
* No weak encryption
* No unsafe config usage
* No raw password handling


2. CI Enforcement (GitHub Actions)

Inside:

.github/workflows/ci.yml

We enforce:

```yaml
- name: Run Trust Scan
  run: poetry run sash-trust run ./app policies/strict.yaml
```

If security fails → CI fails.
Security becomes non-optional.

---

How Developers Use sash_stack

sash_stack is designed to be:

* Clone → Configure → Run → Secure → Extend

Everything is structured, predictable, and security-enforced.


1. Clone the Repository

```bash
git clone https://github.com/SadiqHash/sash_stack.git
```

* Routes do not touch the database directly
* Services contain business logic
* Repositories handle data access
* Security is centralized in core/


2. Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Open .env and adjust values:

```env
APP_NAME=sash_stack
APP_ENV=development

DATABASE_URL=postgresql+psycopg://sash:sash_password@db:5432/sash_stack

SECRET_KEY=replace_this_with_secure_random_string
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
Why this matters

* No secrets inside source code
* No hardcoded credentials
* Configuration is centralized
* Follows security policy enforced by sash_trust


3. Run with Docker

```
docker-compose -f docker/docker-compose.yml up --build
```

This starts:

* FastAPI backend
* PostgreSQL database
* Isolated Docker network
* Persistent database volume

After startup:

```
http://localhost:8000/docs
```
You’ll see the automatic Swagger UI provided by FastAPI.

Why Docker?

Docker ensures:

* Same Python version for everyone
* Same PostgreSQL version
* No environment conflicts
* Production parity
* Deterministic builds

No “works on my machine” problems.


4. Database Migrations (Alembic)

```bash
docker exec -it sash_stack_api alembic revision --autogenerate -m "update"
docker exec -it sash_stack_api alembic upgrade head
```

This keeps schema versioned and consistent.


5. Running Tests

```bash
poetry install --all-extras
poetry run pytest
```

Tests ensure:

* Business logic correctness
* API stability
* Security assumptions remain valid


6. Run Security Scan (Critical Step)

sash_stack is designed to work with:

sash_trust

Run:

```bash
sash-trust run ./app policies/strict.yaml
```

What this does:

* Scans project using AST validation
* Detects insecure patterns
* Enforces encryption rules
* Prevents secret leakage
* Validates secure config usage
* Ensures authentication implementation standards

If violations are found:

Scan fails
CI fails
Pull request blocked

Security is not optional.

---

Typical Development Flow


1. Clone project
2. Create feature branch
3. Write code inside proper layer
4. Run tests
5. Run sash_trust scan
6. Commit & push
7. CI validates automatically

---

Example: Adding a New Feature

Suppose you want to add a new entity called Project.

You would:


1. Create model:

app/models/project.py

2. Create schema:

app/schemas/project.py

3. Create repository:

app/repositories/project_repository.py

4. Create service:

app/services/project_service.py

5. Add route:

app/api/routes/project.py

6. Register route in main.py

7. Generate migration

8. Run sash_trust scan

This keeps:

* Clear separation of concerns
* No business logic inside routes
* No database access inside API layer
* Security enforcement intact

---

How sash_stack + sash_trust Protect Developers

Most developers accidentally introduce:

* Hardcoded secrets
* Weak hashing
* Insecure JWT usage
* Direct SQL queries
* Plaintext password storage

sash_stack structure prevents this.

sash_trust enforces it.

Together they provide:

Security by design
Security by enforcement
Security by automation

---

Using Without Docker (Optional)

If you prefer local development without Docker:

```bash
poetry install --all-extras
poetry run uvicorn app.main:app --reload
```

But Docker is recommended for consistency.

---

CI Enforcement

On every push:

* Dependencies install
* Lint runs
* Type checking runs
* Tests run
* sash_trust scan runs
* Docker image builds

Security violations block merging.

---

What You Get as a Developer

With sash_stack you get:

* Clean backend architecture
* Secure authentication foundation
* Centralized configuration
* Proper secret management
* Enforced security standards
* Dockerized deployment-ready system
* CI-validated security pipeline

It is a secure backend foundation.

---

Contributing to sash_stack

First, thank you for considering contributing.

sash_stack is a security-first backend architecture template.
Every contribution must preserve:

* Clean architecture
* Layered design
* Security enforcement
* Deterministic builds
* CI integrity


Contribution Philosophy

Before contributing, understand:

* Business logic belongs in services/
* Database access belongs in repositories/
* API routes must stay thin
* Security must remain centralized in core/
* No hardcoded secrets
* No bypassing security abstractions

This project prioritizes long-term architectural integrity over quick patches.


Local Development Setup

1. Fork & Clone

```
git clone https://github.com/your_username/sash_stack.git
```

2. Install Poetry (if not installed)

```bash
pip install poetry
```

Verify:

```bash
poetry --version
```

3. Install All Dependencies (Including Dev Tools)

```
poetry install --all-extras
```

This installs:

* Runtime dependencies
* Testing tools (pytest)
* Linters (ruff)
* Formatter (black)
* Type checker (mypy)
* Security tools (bandit)

Now activate virtual environment:

```bash
poetry shell
```

Or run commands using:

```bash
poetry run <command>
```

4. Setup Environment File

```bash
cp .env.example .env
```

Adjust values if needed.

5. Run Application Locally (Without Docker)

```bash
poetry run uvicorn app.main:app --reload
```

Or use Docker:

```bash
docker-compose -f docker/docker-compose.yml up --build
```


Before Submitting a Pull Request

You must run all validation steps locally.

1. Run Tests

```bash
poetry run pytest
```

All tests must pass.

2. Run Linting

```bash
poetry run ruff check .
```

Fix issues before committing.

3. Run Type Checking

```bash
poetry run mypy app
```

Type errors must be resolved.

4. Run Security Scan

This is mandatory.

```bash
poetry run sash-trust run ./app policies/strict.yaml
```

This ensures:

* No insecure patterns introduced
* No secret leakage
* Proper encryption usage
* Secure configuration practices
* No unsafe authentication logic

If this fails, your PR will fail in CI.


Architecture Rules for Contributors

When adding features:

Do:

* Create models in models/
* Create schemas in schemas/
* Add repository layer
* Add service layer
* Keep routes minimal
* Use dependency injection via api/deps.py
* Use centralized security utilities

Do NOT:

* Access database directly inside routes
* Hash passwords inline in routes
* Use os.getenv() randomly across files
* Log sensitive information
* Hardcode secrets
* Bypass validation


Contribution Workflow

1. Fork repository
2. Create feature branch

```bash
git checkout -b feature/your-feature-name
```

3. Implement changes
4. Run all checks locally
5. Commit with meaningful message

```bash
git commit -m "feat: add meaningful message"
```

6. Push branch
7. Open Pull Request


CI Enforcement

Every PR triggers GitHub Actions:

* Dependencies install
* Linting runs
* Type checking runs
* Tests run
* sash_trust security scan runs
* Docker image builds

If any step fails:

PR cannot be merged.

Security and architecture standards are automatically enforced.


Security Responsibility

This project integrates with:

sash_trust

All contributions must comply with enforced security policies.

Security violations are treated as breaking changes.


Code Quality Standards

* Python 3.12+
* Type hints required
* Clean commit messages
* No dead code
* No commented-out legacy code
* Maintain separation of concerns


Open for Contributors

We welcome:

* Backend engineers
* Security researchers
* DevOps contributors
* Architecture reviewers
* Documentation writers

This project aims to become a secure backend blueprint for modern Python systems.

---

License

MIT License

Open for:

* Contributors
* Security researchers
* Backend engineers
* Architecture contributors
