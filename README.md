# Github Automation Workflows
This repository make for practice before do the test. Github automation script ".yml" and also include Python script for operation checking.

---

## Tech Stack
* **Language:** Python 3.11
* **Containerization:** Docker & Docker Compose
* **CI/CD:** GitHub Actions

---

## Project Structure
```
├── .github/workflows/          # GitHub Actions pipeline definitions
│   ├── 1_exercise.yml          # Basic CI test
│   ├── 1_template_workflow.yml # Hello world workflow template
│   ├── 2_exercise.yml          # Triggering on specific branches
│   ├── 3_pull_request.yml      # Pull request event handling
│   ├── 4_exercise.yml          # Python environment setup
│   ├── 5_exercise.yml          # Script validation workflow
│   ├── 6_exercise.yml          # Deployment check with environment variables
│   └── 7_exercise.yml          # Conditional execution and failure handling
├── iam_policies/               # IAM policy files (JSON/TXT) for validation
├── src/day1/                   # Python basics and exercises
│   ├── exercise1/              # Version validation exercise
│   ├── exercise2/              # Log file validation exercise
│   ├── exercise3/              # Environment and path exercise
│   ├── exercise4/              # Critical error/Exit code exercise
│   ├── exercise5/              # JSON configuration validation exercise
│   ├── 1_read_file.py          # File reading examples
│   ├── 3_os_module.py          # OS and Environment variable examples
│   ├── 5_parse_json.py         # JSON parsing logic
│   └── 6_loop_in_folder.py     # Directory scanning logic
├── app.py                      # Main application entry point
├── check_deploy.py             # Deployment target validation script
├── validate_all.py             # Automated policy validation script
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Multi-container orchestration
├── requirements.txt            # Python dependencies
├── .dockerignore               # Files excluded from Docker builds
└── .gitignore                  # Files excluded from Git tracking
```











---

## Installation

#### Setup project
   ```
      git clone https://github.com/your-username/project-name.git
      cd project-name
   ```

#### Run in locally

   1. Create Virtual Environment for Python 3.11 version
      - Linux / macOS
          ```
          python3.11 -m venv .venv
          ```
      - Windows
           ```
           py -3.11 -m venv .venv
           ```
   
   2. Activate Virtual Environment
      - Linux / macOS
          ```
          source .venv/bin/activate
          ```
      - Windows
           ```
           .\.venv\Scripts\Activate.ps1
           ```
   
   3. Install Dependencies
       ```
       pip install -r requirements.txt
       ```
   
   4. Run to test
       ```
       python main.py
       ```

#### Run in container Docker
   ```
      docker-compose up -d --build
   ```
