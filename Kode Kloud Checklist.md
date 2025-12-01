# 🚀 FINAL COMPREHENSIVE CHECKLIST - KODEKLOUD DEVOPS ENGINEER PATH
## Your Complete Action Plan to Land a DevOps Job in 3-4 Months

**Created for:** Ajit Patel (Age 37, 10+ yrs infra/cloud, Caltech Cloud PG, New to DevOps)  
**Start Date:** Monday, December 2, 2025  
**Target Job Date:** End of February / Mid-March 2026  
**Goal:** DevOps Engineer role, ₹18-24L+, CKAD certified

---

## ✅ SECTION 1: PRE-LAUNCH (THIS WEEK - DEC 1-6, 2025)

### Step 1: Create Accounts & Set Up Environment
- [ ] **Create KodeKloud Account**
  - Go to: https://kodekloud.com
  - Sign up with email
  - Enroll in: "DevOps Engineer Learning Path"
  - Bookmark: https://notes.kodekloud.com (cheat sheets)

- [ ] **Create/Verify GitHub Account**
  - Go to: https://github.com
  - Create account (or use existing)
  - Set up SSH key for secure commits
    - Guide: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
  - Bookmark profile for later portfolio work

- [ ] **Create Docker Hub Account**
  - Go to: https://hub.docker.com
  - Free account (for pushing Docker images)
  - Write down username & password

- [ ] **Set Up Local Development Environment**
  - [ ] **Install Git** → https://git-scm.com/download
    - Verify: Run `git --version` in terminal
  
  - [ ] **Install Docker Desktop** → https://www.docker.com/products/docker-desktop
    - Verify: Run `docker --version`
    - Start Docker service
  
  - [ ] **Install kubectl** → https://kubernetes.io/docs/tasks/tools/
    - Verify: Run `kubectl version --client`
  
  - [ ] **Install minikube OR kind** (for local Kubernetes)
    - minikube: https://minikube.sigs.k8s.io/docs/start/
    - OR kind: https://kind.sigs.k8s.io/docs/user/quick-start/
    - Verify: Run `minikube version` or `kind version`
  
  - [ ] **Install Terraform** → https://www.terraform.io/downloads
    - Verify: Run `terraform version`
  
  - [ ] **Install VS Code** (recommended editor) → https://code.visualstudio.com/
    - Extensions: Docker, Kubernetes, Terraform, Git Graph
  
  - [ ] **Verify All Tools**
    - Open terminal and run:
      ```bash
      git --version
      docker --version
      kubectl version --client
      minikube version  # or kind version
      terraform version
      python3 --version
      ```
    - All should return version numbers without errors

### Step 2: Create GitHub Repositories
Create **7 empty repositories** on GitHub (all public):

- [ ] **devops-learning**
  - Purpose: Initial notes, Linux cheatsheet, learning resources
  - Template: Just README.md for now

- [ ] **devops-scripts**
  - Purpose: Bash automation scripts
  - Add: README.md

- [ ] **devops-python**
  - Purpose: Python DevOps utilities
  - Add: README.md, requirements.txt template

- [ ] **devops-docker**
  - Purpose: Dockerfile, docker-compose files
  - Add: README.md

- [ ] **devops-kubernetes**
  - Purpose: K8s manifests, Helm charts, CKAD notes
  - Add: README.md, folder structure

- [ ] **devops-cicd**
  - Purpose: Jenkins Groovy, GitHub Actions workflows
  - Add: README.md

- [ ] **devops-terraform**
  - Purpose: Infrastructure-as-code
  - Add: README.md

- [ ] **devops-observability** (optional for later)
  - Purpose: Prometheus, Grafana, monitoring configs
  - Add: README.md (can skip for now)

**Verification:**
```bash
# Clone all repos locally
git clone git@github.com:YOUR_USERNAME/devops-learning.git
git clone git@github.com:YOUR_USERNAME/devops-scripts.git
# ... (repeat for all 7)
```

### Step 3: Join Communities & Follow Experts
- [ ] **Join Reddit Communities**
  - Subscribe: /r/devops
  - Subscribe: /r/kubernetes
  - Subscribe: /r/Terraform
  - Set notification for posts you're interested in

- [ ] **Follow on LinkedIn**
  - Search for: "#DevOps" thought leaders
  - Follow: "KodeKloud" official account
  - Follow: Kubernetes community leaders
  - Comment on 2-3 posts (build visibility)

- [ ] **Bookmark Important Resources**
  - Kubernetes Docs: https://kubernetes.io/docs/
  - Terraform Registry: https://registry.terraform.io/
  - Docker Docs: https://docs.docker.com/
  - GitHub Actions: https://docs.github.com/en/actions
  - Stack Overflow DevOps Tag: https://stackoverflow.com/questions/tagged/devops
  - KodeKloud Notes: https://notes.kodekloud.com/

- [ ] **Set Calendar Reminders**
  - [ ] Dec 2 (Mon) 8 AM: Start Week 1 - Linux Fundamentals
  - [ ] Every Sunday 6 PM: Weekly review + next week prep
  - [ ] Every Friday: GitHub portfolio check-in
  - [ ] Feb 15: CKAD exam prep intensifies
  - [ ] Feb 28: Start job applications

### Step 4: Create Study Space
- [ ] **Physical Setup**
  - Clear desk space with dual monitor (if possible)
  - Good internet connection (test speed: speedtest.net)
  - Quiet room for 4 hours daily study
  - Comfortable chair (your back will thank you!)

- [ ] **Digital Setup**
  - Create folder: `~/DevOps-Learning/` for all projects
  - Create: `study-notes.md` file (local or Notion/Google Docs)
  - Set up: IDE shortcuts, terminal profile
  - Bookmark 5 key resources in browser

- [ ] **Accountability Setup**
  - Tell family/friends about your 16-week goal
  - Join DevOps Slack/Discord (search: "DevOps community")
  - Find 1 study buddy (even virtual, via Reddit or LinkedIn)
  - Share your GitHub link with accountability partner

**Pre-Launch Checkpoint:**
- [ ] All tools installed and verified
- [ ] 7 GitHub repos created and cloned locally
- [ ] Communities joined, bookmarks set
- [ ] Study space ready, calendar reminders set
- [ ] Accountability partner identified

---

## ✅ SECTION 2: WEEKLY CHECKLISTS (Weeks 1-16)

### **WEEK 1: Foundations - Linux & DevOps Intro** (Dec 2-6, 2025)

**Courses to Complete:**
- [ ] **DevOps Pre-Requisite Course** (KodeKloud)
  - Estimated time: 2-3 hours (you can speed through)
  - [ ] Watch all modules
  - [ ] Take notes on DevOps philosophy

- [ ] **Linux for Beginners** (KodeKloud)
  - Estimated time: 6-8 hours
  - [ ] Watch all modules
  - [ ] Complete ALL labs
  - [ ] Take screenshots of lab completions

**Practical Exercises:**
- [ ] Create `linux-cheatsheet.md` with:
  - File system navigation commands
  - User & permission management
  - Process management
  - Package management (apt/yum)
  - Service management

- [ ] GitHub Commit:
  - [ ] Push to `devops-learning/` repo
  - [ ] File: `linux-cheatsheet.md`
  - [ ] Write README explaining the cheatsheet

**Daily Checklist (Mon-Sat):**
- [ ] Morning (1-1.5 hrs): Watch course videos
- [ ] Afternoon (1.5 hrs): Complete labs on KodeKloud
- [ ] Evening (30 min): Document + push to GitHub
- [ ] Total: ~4 hours/day

**Week 1 Checkpoint (Friday Dec 6):**
- [ ] DevOps Pre-Req course: ✅ Complete
- [ ] Linux for Beginners: ✅ 80%+ complete
- [ ] Linux cheatsheet: ✅ On GitHub
- [ ] Labs: ✅ All attempted + screenshots saved
- [ ] GitHub commits: ✅ At least 2 commits this week

---

### **WEEK 2: Git & Bash Scripting Basics** (Dec 9-13, 2025)

**Courses to Complete:**
- [ ] **Git for Beginners** (KodeKloud)
  - Estimated time: 4-5 hours
  - [ ] Watch modules
  - [ ] Complete labs (clone, branch, merge, PR)
  - [ ] Set up SSH keys

- [ ] **Linux Shell Scripting** (KodeKloud)
  - Estimated time: 12-15 hours
  - [ ] Watch modules (loops, conditionals, functions)
  - [ ] Complete ALL labs
  - [ ] Write your own scripts

**Practical Exercises - Write 3 Bash Scripts:**
- [ ] **Script 1: `backup.sh`**
  - Purpose: Backup a directory with timestamp
  - Features: Loop through files, create dated backup folder
  - Test locally before committing
  - Push to `devops-scripts/` repo

- [ ] **Script 2: `log_analyzer.sh`**
  - Purpose: Parse log files, extract error lines
  - Features: grep, awk, conditional output
  - Test with sample log file
  - Push to `devops-scripts/` repo

- [ ] **Script 3: `health_check.sh`**
  - Purpose: Monitor CPU, memory, disk usage
  - Features: Get system metrics, alert if threshold exceeded
  - Test on local machine
  - Push to `devops-scripts/` repo

**GitHub Commits:**
- [ ] Push all 3 scripts to `devops-scripts/`
- [ ] Each script: .sh file + comments explaining logic
- [ ] README.md: Explain each script, how to run
- [ ] Minimum 3 commits

**Week 2 Checkpoint (Friday Dec 13):**
- [ ] Git course: ✅ Complete
- [ ] Shell Scripting course: ✅ 80%+ complete
- [ ] 3 bash scripts: ✅ Written, tested, on GitHub
- [ ] Git configured with SSH: ✅ Verified
- [ ] GitHub commits: ✅ At least 3 commits this week

---

### **WEEK 3: Python Basics for DevOps** (Dec 16-20, 2025)

**Courses to Complete:**
- [ ] **Python for DevOps** (KodeKloud or alternative)
  - Estimated time: 10-12 hours
  - [ ] Watch modules (data types, functions, file I/O)
  - [ ] Focus on: JSON, YAML, HTTP requests
  - [ ] Complete ALL labs

**Practical Exercises - Write 2 Python Scripts:**
- [ ] **Script 1: `api_health_checker.py`**
  - Purpose: Call a public API, check if it's healthy
  - Libraries: requests, json
  - Features: Make HTTP request, parse JSON response, print status
  - Test: Use a free public API (e.g., jsonplaceholder)
  - Push to `devops-python/` repo

- [ ] **Script 2: `config_parser.py`**
  - Purpose: Read YAML/JSON config file, extract values
  - Libraries: yaml (or json), os
  - Features: Parse config, print specific values
  - Test: Create sample config file, parse it
  - Push to `devops-python/` repo

**GitHub Commits:**
- [ ] Push 2 Python scripts to `devops-python/`
- [ ] Add `requirements.txt` with dependencies
- [ ] README.md: How to install requirements, run scripts
- [ ] Minimum 2 commits

**Phase 1 Recap - Foundations Complete:**
- [ ] Linux fundamentals: ✅
- [ ] Git workflow: ✅
- [ ] Bash scripting: ✅
- [ ] Python scripting: ✅
- [ ] GitHub portfolio started: ✅ 3+ repos

**Week 3 Checkpoint (Friday Dec 20):**
- [ ] Python course: ✅ 80%+ complete
- [ ] 2 Python scripts: ✅ Written, tested, on GitHub
- [ ] `requirements.txt`: ✅ Created
- [ ] GitHub commits: ✅ At least 2 commits this week
- [ ] **Total Phase 1 commits: ✅ 7+ commits across all repos**

---

### **WEEK 4: Docker Fundamentals** (Dec 23-27, 2025)

**Courses to Complete:**
- [ ] **Docker for Absolute Beginners** (KodeKloud)
  - Estimated time: 12-15 hours
  - [ ] Watch all modules
  - [ ] Complete ALL labs
  - [ ] Focus on: Dockerfile, volumes, networks

**Practical Exercises:**
- [ ] **Build a Simple App Dockerfile**
  - Option A: Python Flask app (easy)
  - Option B: Node.js app (also fine)
  - Create: `Dockerfile` with best practices
  - Build: `docker build -t myapp:1.0 .`
  - Test: `docker run -p 8080:5000 myapp:1.0`
  - Verify: App runs without errors

- [ ] **Create Docker Compose Setup**
  - Create: `docker-compose.yml`
  - Services: App + PostgreSQL database
  - Features: Volumes, networks, environment variables
  - Test: `docker-compose up`, verify both services running
  - Cleanup: `docker-compose down`

- [ ] **Push to Docker Hub (Public)**
  - Build image: `docker build -t YOUR_USERNAME/myapp:1.0 .`
  - Push: `docker push YOUR_USERNAME/myapp:1.0`
  - Verify: Image visible on Docker Hub profile

**GitHub Commits:**
- [ ] Push to `devops-docker/`:
  - [ ] Dockerfile
  - [ ] docker-compose.yml
  - [ ] README.md (with build & run instructions)
  - [ ] .dockerignore file
- [ ] Minimum 2 commits

**Week 4 Checkpoint (Friday Dec 27):**
- [ ] Docker course: ✅ 80%+ complete
- [ ] Dockerfile created & tested: ✅
- [ ] Docker Compose setup: ✅
- [ ] Image pushed to Docker Hub: ✅
- [ ] GitHub commits: ✅ At least 2 commits

---

### **WEEK 5-6: Kubernetes - The Heavy Lifting** (Dec 30 - Jan 10, 2026)

**Courses to Complete:**
- [ ] **Kubernetes for Absolute Beginners** (KodeKloud)
  - Estimated time: 15-18 hours
  - [ ] Watch all modules
  - [ ] Complete ALL labs (multiple times)
  - [ ] Focus: Pods → Deployments → Services → Ingress

- [ ] **Kubernetes Networking Deep Dive** (KodeKloud - optional but recommended for YOU)
  - Estimated time: 8-10 hours
  - [ ] Watch modules (your networking background helps!)
  - [ ] Complete labs

**Practical Exercises:**
- [ ] **Deploy Your Docker App to Local Kubernetes**
  - Start minikube/kind: `minikube start` or `kind create cluster`
  - Create Deployment YAML: `deployment.yaml`
  - Create Service YAML: `service.yaml`
  - Apply: `kubectl apply -f deployment.yaml -f service.yaml`
  - Verify: `kubectl get pods`, `kubectl get svc`
  - Access app: Forward port or use ingress

- [ ] **Create Kubernetes Manifests Set**
  - `deployment.yaml`: 3 replicas of your app
  - `service.yaml`: ClusterIP service
  - `configmap.yaml`: App configuration
  - `secret.yaml`: Sensitive data (encrypted)
  - `ingress.yaml`: Traffic routing (if needed)
  - All files: Properly commented

**GitHub Commits:**
- [ ] Push to `devops-kubernetes/`:
  - [ ] `/manifests` folder with all YAML files
  - [ ] README.md (architecture diagram, deployment steps)
  - [ ] Folder: `/notes` with your Kubernetes learning notes
- [ ] Minimum 3 commits

**Week 5-6 Checkpoint (Friday Jan 10):**
- [ ] K8s for Beginners course: ✅ 100% complete
- [ ] K8s Networking course: ✅ 80%+ complete (or started)
- [ ] Local Kubernetes cluster running: ✅
- [ ] App deployed to K8s: ✅
- [ ] Manifests on GitHub: ✅
- [ ] Can describe K8s architecture: ✅

---

### **WEEK 7: CKAD Certification Prep - 40% Complete** (Jan 13-17, 2026)

**Courses to Complete:**
- [ ] **CKAD (Certified Kubernetes Application Developer)** (KodeKloud)
  - Estimated time: 15-20 hours (for weeks 7-8 combined)
  - [ ] Watch modules (Pod design, Deployments, Jobs, Secrets, PVs)
  - [ ] Complete labs
  - [ ] Start taking notes for exam

**Practical Exercises:**
- [ ] **CKAD Practice Scenarios**
  - Complete 5-10 CKAD challenges on KodeKloud
  - Document your approach for each
  - Time yourself (exam is 2 hours)

- [ ] **Create CKAD Study Guide**
  - File: `CKAD_Study_Guide.md` in `devops-kubernetes/`
  - Include: Key concepts, commands, best practices
  - Add: Mock exam practice questions (5-10)

**GitHub Commits:**
- [ ] Push to `devops-kubernetes/`:
  - [ ] CKAD study guide
  - [ ] Sample challenge solutions
  - [ ] CKAD notes from course
- [ ] Minimum 2 commits

**Week 7 Checkpoint (Friday Jan 17):**
- [ ] CKAD course: ✅ 40-50% complete
- [ ] CKAD challenges attempted: ✅ 5+
- [ ] Study guide created: ✅
- [ ] Mock exam score: ✅ Target ≥60%
- [ ] GitHub commits: ✅ At least 2 commits

---

### **WEEK 8: Helm & CKAD - 60% Complete** (Jan 20-24, 2026)

**Courses to Complete:**
- [ ] **Helm for Beginners** (KodeKloud)
  - Estimated time: 6-8 hours
  - [ ] Watch all modules
  - [ ] Complete labs

- [ ] **CKAD Certification** (continued)
  - [ ] Complete 50-60% of course
  - [ ] Take 2nd mock exam
  - [ ] Target score: ≥70%

**Practical Exercises:**
- [ ] **Create Reusable Helm Chart**
  - Create chart: `helm create myapp`
  - Customize templates: deployment, service, configmap, ingress
  - Test: `helm install myapp ./myapp`
  - Verify: All resources created correctly
  - Cleanup: `helm uninstall myapp`

- [ ] **Helm Chart Best Practices**
  - Values file with sensible defaults
  - Helper templates for DRY code
  - Chart.yaml with metadata
  - values-dev.yaml, values-prod.yaml for environments

**GitHub Commits:**
- [ ] Push to `devops-kubernetes/`:
  - [ ] `/helm-chart` folder with complete chart
  - [ ] Chart.yaml, values.yaml, templates/
  - [ ] README.md (how to install, customize, deploy)
- [ ] Minimum 2 commits

**Phase 2 Complete - Containerization & Orchestration:**
- [ ] Docker: ✅ Proficient
- [ ] Kubernetes: ✅ Deployments running locally
- [ ] Helm: ✅ Charts created
- [ ] CKAD: ✅ 50-60% complete, ≥70% mock exam score

**Week 8 Checkpoint (Friday Jan 24):**
- [ ] Helm course: ✅ 100% complete
- [ ] Helm chart created & tested: ✅
- [ ] CKAD course: ✅ 50-60% complete
- [ ] Mock exam score: ✅ ≥70%
- [ ] GitHub commits: ✅ At least 3 commits this week

---

### **WEEK 9: CI/CD Pipelines - Jenkins** (Jan 27-31, 2026)

**Courses to Complete:**
- [ ] **Jenkins for Beginners** (KodeKloud)
  - Estimated time: 10-12 hours
  - [ ] Watch all modules
  - [ ] Focus on: Declarative Pipelines, Git integration, Docker integration
  - [ ] Complete labs

**Practical Exercises:**
- [ ] **Set Up Jenkins Locally (Docker)**
  - Run Jenkins in container: `docker run -d -p 8080:8080 jenkins/jenkins:lts`
  - Access: localhost:8080
  - Install plugins: Pipeline, Git, Docker

- [ ] **Create Sample Jenkins Pipeline**
  - Create: `Jenkinsfile` (Declarative syntax)
  - Stages:
    1. Checkout (git clone your repo)
    2. Build (build Docker image)
    3. Test (run tests if applicable)
    4. Push (push to Docker Hub)
    5. Deploy (deploy to Kubernetes - mock/sandbox)
  - Store in GitHub repo (`devops-cicd/`)

- [ ] **Pipeline Integration**
  - Create Jenkins job pointing to GitHub repo
  - Set up webhook (GitHub → Jenkins)
  - Test: Push code to GitHub, watch pipeline trigger
  - Verify: All stages pass

**GitHub Commits:**
- [ ] Push to `devops-cicd/`:
  - [ ] Jenkinsfile
  - [ ] README.md (pipeline explanation, stages, screenshots)
  - [ ] Screenshots of Jenkins UI running pipeline
- [ ] Minimum 2 commits

**Week 9 Checkpoint (Friday Jan 31):**
- [ ] Jenkins course: ✅ 100% complete
- [ ] Jenkins running locally: ✅
- [ ] Jenkinsfile created: ✅
- [ ] Pipeline tested & working: ✅
- [ ] GitHub integration: ✅
- [ ] GitHub commits: ✅ At least 2 commits

---

### **WEEK 10: GitHub Actions & Terraform Intro** (Feb 3-7, 2026)

**Courses to Complete:**
- [ ] **GitHub Actions** (KodeKloud or self-taught)
  - Estimated time: 6-8 hours
  - [ ] Watch modules
  - [ ] Complete labs

- [ ] **Terraform for Beginners** (KodeKloud)
  - Estimated time: 10-12 hours (start course)
  - [ ] Watch modules (HCL syntax, providers, resources)
  - [ ] Start labs

**Practical Exercises:**
- [ ] **Create GitHub Actions Workflow**
  - File: `.github/workflows/ci-cd.yaml`
  - Workflow steps:
    1. Trigger on push to main
    2. Lint code
    3. Build Docker image
    4. Push to Docker Hub
    5. (Optional) Deploy to staging
  - Test: Push code to GitHub, verify workflow runs

- [ ] **Start Terraform Project - Simple VPC**
  - Create folder: `devops-terraform/simple-vpc/`
  - Files:
    - `main.tf` (VPC definition)
    - `variables.tf` (input variables)
    - `outputs.tf` (output values like VPC ID)
    - `terraform.tfvars.example` (example values, no secrets!)
  - Test: `terraform init`, `terraform plan`, `terraform apply`
  - Destroy: `terraform destroy` (to save cloud costs)

**GitHub Commits:**
- [ ] Push to `devops-cicd/`:
  - [ ] `.github/workflows/ci-cd.yaml`
  - [ ] README.md (workflow explanation)

- [ ] Push to `devops-terraform/`:
  - [ ] `simple-vpc/` folder with TF files
  - [ ] README.md (architecture, how to deploy)
  - [ ] `terraform.tfvars.example`
- [ ] Minimum 3 commits total

**Week 10 Checkpoint (Friday Feb 7):**
- [ ] GitHub Actions course: ✅ 100% complete
- [ ] GitHub Actions workflow: ✅ Created & tested
- [ ] Terraform course: ✅ 50-60% complete
- [ ] Terraform VPC project: ✅ Created & tested
- [ ] GitHub commits: ✅ At least 3 commits

---

### **WEEK 11: Infrastructure as Code - Terraform Production** (Feb 10-14, 2026)

**Courses to Complete:**
- [ ] **Terraform for Beginners** (continued & completed)
  - Estimated time: 5-8 hours
  - [ ] Watch remaining modules
  - [ ] Complete all labs
  - [ ] Focus on: Modules, state management, best practices

**Practical Exercises:**
- [ ] **Create Production Terraform Project - 3-Tier App Infrastructure**
  - Create folder: `devops-terraform/app-infrastructure/`
  - Components:
    - VPC with public/private subnets
    - EC2 instance (in public subnet) OR GCP instance
    - Security groups (firewall rules)
    - RDS database OR managed database service
    - Outputs: IP addresses, DNS names, DB endpoint
  - Files: `main.tf`, `variables.tf`, `outputs.tf`, `terraform.tfvars.example`
  - Test: `terraform plan`, `terraform apply`, verify resources in cloud console
  - Destroy: `terraform destroy` after verification

- [ ] **Create Terraform Modules (Reusable Code)**
  - Create: `modules/vpc/` (VPC creation logic)
  - Create: `modules/compute/` (EC2/GCP instance creation)
  - Use modules in main project
  - Benefits: DRY code, reusability

**GitHub Commits:**
- [ ] Push to `devops-terraform/`:
  - [ ] `app-infrastructure/` folder (complete project)
  - [ ] `modules/` folder (vpc, compute modules)
  - [ ] README.md (architecture diagram, step-by-step deployment)
  - [ ] Screenshots of deployed infrastructure
- [ ] Minimum 3 commits

**Week 11 Checkpoint (Friday Feb 14):**
- [ ] Terraform course: ✅ 100% complete
- [ ] Production IaC project: ✅ Created, deployed, tested
- [ ] Terraform modules: ✅ Created and working
- [ ] Architecture diagrams: ✅ On GitHub
- [ ] GitHub commits: ✅ At least 3 commits

---

### **WEEK 12: Observability - Prometheus, Grafana & CKAD Finishing** (Feb 17-21, 2026)

**Courses to Complete:**
- [ ] **Prometheus & Grafana** (KodeKloud)
  - Estimated time: 10-12 hours
  - [ ] Watch all modules
  - [ ] Complete labs

- [ ] **CKAD Certification** (final push to 85%+)
  - Estimated time: 8-10 hours
  - [ ] Complete remaining modules
  - [ ] Take 2-3 mock exams
  - [ ] Target score: ≥85%

**Practical Exercises:**
- [ ] **Deploy Prometheus + Grafana to Kubernetes**
  - Use Helm chart or manifests
  - Configure Prometheus to scrape metrics
  - Create Grafana dashboards:
    - Pod count by namespace
    - CPU usage (nodes & pods)
    - Memory usage
    - Request latency
    - Custom app metrics
  - Set up alert rules: Pod down, high CPU, etc.

- [ ] **Create Monitoring Configuration**
  - File: `prometheus-config.yaml`
  - File: `alert-rules.yaml`
  - File: Grafana dashboard JSON exports
  - Document: How to deploy, what each dashboard shows

- [ ] **CKAD Mock Exams**
  - Take 3 full mock exams (2 hours each)
  - Target score: ≥85%
  - Review weak areas
  - Take notes on commonly missed questions

**GitHub Commits:**
- [ ] Push to `devops-observability/`:
  - [ ] `prometheus-config.yaml`
  - [ ] `alert-rules.yaml`
  - [ ] Grafana dashboard JSONs (in `/dashboards` folder)
  - [ ] Screenshots of dashboards
  - [ ] README.md (deployment steps, dashboard explanations)

- [ ] Push to `devops-kubernetes/`:
  - [ ] CKAD final notes & practice answers
  - [ ] CKAD mock exam scores/notes

- [ ] Minimum 4 commits total

**Phase 3 Complete - Automation & Observability:**
- [ ] CI/CD pipelines: ✅ Working (Jenkins & GitHub Actions)
- [ ] IaC: ✅ Terraform projects deployed
- [ ] Observability: ✅ Prometheus/Grafana running
- [ ] CKAD progress: ✅ 85%+ ready for exam

**Week 12 Checkpoint (Friday Feb 21):**
- [ ] Prometheus/Grafana course: ✅ 100% complete
- [ ] Monitoring setup: ✅ Running in K8s, dashboards live
- [ ] CKAD course: ✅ 100% complete
- [ ] Mock exam scores: ✅ ≥85% on latest
- [ ] GitHub commits: ✅ At least 4 commits

---

### **WEEK 13-14: KKE Challenges, Portfolio Polish, Interview Prep** (Feb 24 - Mar 7, 2026)

**Activities to Complete:**
- [ ] **KodeKloud Engineer (KKE) Challenges**
  - [ ] Complete 5-10 KKE challenges
  - [ ] Document your approach for each
  - [ ] Create: `devops-kke-solutions/` repo with solutions
  - [ ] For each challenge: Problem statement, solution, lessons learned

- [ ] **CKAD Exam Booking & Prep**
  - [ ] Schedule CKAD exam (Feb 24 - Mar 7 timeframe)
  - [ ] Take final mock exams daily
  - [ ] Review weak areas
  - [ ] Create quick reference sheet for exam day

- [ ] **GitHub Portfolio Finalization**
  - [ ] Create root README: `README.md` in main profile repo
  - [ ] List all 7 projects with 1-2 sentence description each
  - [ ] Add architecture diagrams (use draw.io, Lucidchart, or ASCII art)
  - [ ] Screenshot examples from each project
  - [ ] Links to live demos (if deployed to cloud)

- [ ] **Create Professional Portfolio Document**
  - File: `PORTFOLIO.md` in one of your repos
  - Include:
    - 2-3 paragraph summary of your journey
    - What you learned in each phase
    - Key technologies mastered
    - Links to all projects
    - CKAD certification status

- [ ] **Interview Preparation**
  - [ ] Study common DevOps questions:
    - "Explain your CI/CD pipeline"
    - "How would you troubleshoot a pod crash?"
    - "What are the benefits of IaC?"
    - "Describe your Kubernetes architecture"
  - [ ] Record yourself answering 5-10 questions
  - [ ] Mock interview with friend or online platform (Pramp, Interviewing.io)
  - [ ] Research 5 target companies, understand their tech stack

- [ ] **Blog Posts (Optional but Helpful)**
  - [ ] Write 2-3 blog posts on Medium or Dev.to:
    - "How I set up CI/CD for Kubernetes deployments"
    - "Infrastructure as Code with Terraform: lessons learned"
    - "Monitoring and alerting with Prometheus & Grafana"
  - [ ] Share on LinkedIn + GitHub

**GitHub Commits:**
- [ ] Push to all relevant repos:
  - [ ] Portfolio updates
  - [ ] KKE solutions
  - [ ] CKAD study materials
  - [ ] Architecture diagrams
- [ ] Minimum 5-10 commits across all repos

**Weeks 13-14 Checkpoint (Friday Mar 7):**
- [ ] KKE challenges: ✅ 5-10 completed & documented
- [ ] CKAD exam: ✅ Scheduled, practicing intensively
- [ ] Portfolio: ✅ Professional, complete, on GitHub
- [ ] Interview prep: ✅ Mock interviews done, Q&A ready
- [ ] Blog posts: ✅ Published (optional, but +1 if done)
- [ ] GitHub portfolio: ✅ Polished, all projects visible

---

### **WEEK 15-16: Job Hunt & Final Adjustments** (Mar 10-21, 2026)

**Activities to Complete:**
- [ ] **Take CKAD Exam (if scheduled)**
  - [ ] Exam date: Late Feb or early Mar (already scheduled in week 13)
  - [ ] Target score: ≥70% (passing)
  - [ ] If passed: Add to resume & LinkedIn immediately
  - [ ] If failed: Retake within 30 days; most people pass on 2nd attempt

- [ ] **Update Resume & LinkedIn Profile**
  - [ ] Rewrite resume header:
    ```
    Ajit Patel – Senior DevOps Engineer | Kubernetes & CI/CD Specialist
    10+ years infrastructure & cloud | AWS, Terraform, Jenkins, Prometheus
    CKAD Certified | Caltech Cloud PG
    ```
  - [ ] Update LinkedIn headline & summary
  - [ ] Add all projects to portfolio section
  - [ ] Include GitHub link, blog posts
  - [ ] Add CKAD badge (if earned)

- [ ] **Create Job Search Materials**
  - [ ] Polish cover letter template (customize per company)
  - [ ] Prepare "Tell me about yourself" pitch (2-3 minutes)
  - [ ] Practice salary negotiation talking points
  - [ ] List 10-15 target companies

- [ ] **Job Applications** (Target: 10-15 applications)
  - [ ] Company 1: [Company name, position, date applied]
  - [ ] Company 2: [...]
  - [ ] ... (continue for 10-15 companies)
  - [ ] Track: Company, position, date, status
  - [ ] Follow up: After 5-7 days if no response

- [ ] **Interview Preparation (Ongoing)**
  - [ ] Practice daily: 30 min technical questions, 30 min behavioral
  - [ ] Mock interviews: 2-3 full mock interviews
  - [ ] System design: Be ready to discuss architecture design
  - [ ] Troubleshooting scenarios: Practice K8s debugging

- [ ] **Continuous Learning (If Time Allows)**
  - [ ] Start exploring CKA (next certification)
  - [ ] Explore SRE or Platform Engineer concepts
  - [ ] Contribute to open-source DevOps projects
  - [ ] Read DevOps engineering books (e.g., The Phoenix Project)

**Job Search Tracking:**
- [ ] Create spreadsheet:
  | Company | Position | Date Applied | Status | Interview Date | Outcome |
  |---------|----------|--------------|--------|----------------|---------|
  | Company A | DevOps Eng | Mar 10 | Applied | - | - |
  | ... | ... | ... | ... | ... | ... |

**Week 15-16 Checkpoint (Friday Mar 21):**
- [ ] CKAD exam: ✅ Passed (target ≥70%)
- [ ] Resume: ✅ Updated with all skills + projects
- [ ] LinkedIn: ✅ Polished, visible to recruiters
- [ ] Job applications: ✅ 10-15 submitted
- [ ] Phone interviews: ✅ 2-3 completed
- [ ] Mock interviews: ✅ 3+ done
- [ ] **Expected: 1-2 real interviews scheduled**

---

## ✅ SECTION 3: SUCCESS METRICS - FINAL CHECKPOINTS

### By End of Week 8 (Jan 24)
- [ ] **Linux & Git:** Fluent in commands and workflows
- [ ] **Docker:** Images built, pushed to Docker Hub
- [ ] **Kubernetes:** App running locally, manifests created
- [ ] **Helm:** Reusable charts created
- [ ] **GitHub:** 4 professional repos with README + code
- [ ] **CKAD Prep:** 50-60% of course complete, ≥70% on mock

### By End of Week 12 (Feb 21)
- [ ] **CI/CD:** Jenkins pipeline working + GitHub Actions workflow
- [ ] **IaC:** Terraform projects deployed to cloud (VPC + app infra)
- [ ] **Observability:** Prometheus + Grafana running, dashboards live
- [ ] **CKAD:** 100% of course, ≥85% on mock exams
- [ ] **GitHub:** 7 professional repos, all with documentation + diagrams
- [ ] **KKE:** 5+ challenges completed & documented

### By End of Week 16 (Mar 21)
- [ ] **CKAD Exam:** ✅ Passed (target ≥70%)
- [ ] **Resume:** ✅ Professional, skills-focused
- [ ] **Portfolio:** ✅ 7 GitHub repos, all polished
- [ ] **Job Applications:** ✅ 10-15 submitted
- [ ] **Interviews:** ✅ 2-3 phone screens, 1-2 technical rounds
- [ ] **Expected Outcome:** ✅ 1-2 job offers (₹18-24L+ salary)

---

## ✅ SECTION 4: DAILY HABITS CHECKLIST

### Every Single Day (Mon-Sat)
- [ ] **Morning (8-9:30 AM):** Watch 1-2 course modules
- [ ] **Late Morning (9:30-11:30 AM):** Complete lab on KodeKloud
- [ ] **Afternoon (1:30-3:30 PM):** Code locally (build, script, configure)
- [ ] **Late Afternoon (4:30-5:15 PM):** Document & push to GitHub
- [ ] **Evening (optional):** Read documentation or study notes

### Every Week (Sunday Evening)
- [ ] Review week's progress
- [ ] Update study notes
- [ ] Check GitHub commit count (target: 3-5 per week)
- [ ] Plan next week's focus
- [ ] Update calendar reminders

### Every 2 Weeks
- [ ] Review GitHub portfolio
- [ ] Update README files
- [ ] Check architecture diagrams
- [ ] Add new screenshots from latest work

### Every Month
- [ ] Reflect on learning
- [ ] Identify gaps
- [ ] Adjust study plan if needed
- [ ] Update LinkedIn with progress
- [ ] Share wins with accountability partner

---

## ✅ SECTION 5: TROUBLESHOOTING & HELP

### If You Get Stuck
1. **Check KodeKloud Forums** – Most answers there
2. **Search Stack Overflow** – Add tags: devops, kubernetes, docker, terraform
3. **Ask Reddit /r/devops** – Search first, then ask with details
4. **Google the error message** – Exact error + technology
5. **Read official documentation** – Kubernetes.io, Docker docs, Terraform docs

### Common Issues & Solutions

**"My Docker build fails"**
- [ ] Check Dockerfile syntax
- [ ] Ensure all dependencies listed
- [ ] Check Docker Hub credentials
- [ ] Try building from fresh directory

**"kubectl command not found"**
- [ ] Verify kubectl installed: `kubectl version --client`
- [ ] Add to PATH if needed
- [ ] Reinstall if necessary

**"Terraform apply errors"**
- [ ] Run `terraform validate` first
- [ ] Check variable values in `terraform.tfvars`
- [ ] Verify AWS/GCP credentials
- [ ] Check provider version compatibility

**"Stuck on a concept"**
- [ ] Rewatch the KodeKloud course module (2-3 times)
- [ ] Read the official documentation
- [ ] Watch YouTube explainer videos
- [ ] Practice the lab 2-3 times
- [ ] Teach it to someone else (solidifies understanding)

---

## ✅ SECTION 6: MENTAL CHECKLIST & MINDSET

### Mindset Reminders
- [ ] **Progress over perfection:** Your first script won't be perfect. That's okay.
- [ ] **Consistency beats intensity:** 4 hours daily > 16 hours once a week
- [ ] **Labs are 70% of learning:** Watch videos fast, spend time on labs
- [ ] **Failures are learning:** If something breaks, debug it (great learning!)
- [ ] **Your experience matters:** 10+ years infra is a HUGE advantage
- [ ] **Coding is learnable:** Bash + Python are not rocket science
- [ ] **GitHub is your resume:** Every commit matters

### Motivation Checkpoints
- [ ] Week 3: "I wrote Bash scripts that actually work!"
- [ ] Week 8: "My app is running on Kubernetes locally!"
- [ ] Week 12: "I set up a real CI/CD pipeline!"
- [ ] Week 14: "I passed CKAD certification!"
- [ ] Week 16: "I got a DevOps Engineer job offer!"

### Accountability
- [ ] Find 1 study buddy (online or local)
- [ ] Join DevOps Slack/Discord communities
- [ ] Post weekly progress on LinkedIn
- [ ] Share GitHub repos with friends
- [ ] Tell family your goal → they'll remind you when you skip days

---

## ✅ FINAL PRE-LAUNCH ACTIONS (Before Dec 2, 2025)

**Do These Today (Dec 1):**
- [ ] Print this checklist (or bookmark it)
- [ ] Create all GitHub repos (don't add content yet)
- [ ] Install all local tools (Docker, kubectl, Terraform)
- [ ] Test all installations
- [ ] Join Reddit /r/devops
- [ ] Set phone reminder for Monday Dec 2, 8 AM
- [ ] Tell someone about your goal (accountability!)

**Monday Dec 2, 2025 - LAUNCH DAY:**
- [ ] Open KodeKloud, find DevOps Engineer path
- [ ] Enroll in first course: "DevOps Pre-Requisite Course"
- [ ] Start watching videos
- [ ] First GitHub commit: devops-learning/README.md
- [ ] Celebrate! You've started! 🎉

---

## 🎯 FINAL GOAL REMINDER

| Metric | Target | Current | Date Achieved |
|--------|--------|---------|----------------|
| Linux fundamentals | ✅ | ❌ | Week 3 |
| Docker proficiency | ✅ | ❌ | Week 4 |
| Kubernetes deployment | ✅ | ❌ | Week 8 |
| CI/CD pipeline | ✅ | ❌ | Week 9 |
| Infrastructure as Code | ✅ | ❌ | Week 11 |
| Prometheus/Grafana | ✅ | ❌ | Week 12 |
| CKAD certification | ✅ | ❌ | Week 14 |
| GitHub portfolio (7 repos) | ✅ | ❌ | Week 14 |
| Job applications (10+) | ✅ | ❌ | Week 15 |
| **JOB OFFER** | **✅** | **❌** | **Week 16** |

---

## 🚀 YOU'VE GOT THIS!

**Your Timeline:**
- 🟢 **Dec 2, 2025:** Start learning
- 🟡 **Jan 15, 2026:** Halfway through (feeling confident!)
- 🟠 **Feb 21, 2026:** Exam prep + job applications begin
- 🔴 **Mar 21, 2026:** Job offers should be coming in

**Expected Outcome:**
- DevOps Engineer role
- ₹18-24L+ salary
- CKAD certification
- 10+ years experience + 16 weeks modern skills = **COMPETITIVE**

**Remember:** Your network + cloud + infrastructure background is your **superpower**. You just need to wrap it in modern DevOps tools. 

**Let's go! 💪🚀**

---

## 📞 QUICK REFERENCE LINKS

- **KodeKloud:** https://kodekloud.com
- **KodeKloud Notes:** https://notes.kodekloud.com/
- **GitHub:** https://github.com
- **Docker Hub:** https://hub.docker.com
- **Kubernetes Docs:** https://kubernetes.io/docs/
- **Terraform Registry:** https://registry.terraform.io/
- **Reddit DevOps:** https://www.reddit.com/r/devops/
- **Stack Overflow DevOps:** https://stackoverflow.com/questions/tagged/devops

---

**Document Created:** December 1, 2025  
**For:** Ajit Patel  
**Goal:** DevOps Engineer job in 16 weeks  
**Status:** 🟢 **READY TO LAUNCH**

---

**PRINT THIS. PIN IT. FOLLOW IT. WIN IT!**

🚀 **Let's get you that DevOps job offer! 🎉**
