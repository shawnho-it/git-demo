# 🚀 Flask App CI/CD Deployment with GitHub Actions + EC2

This project demonstrates a complete CI/CD pipeline for deploying a Python Flask application to an AWS EC2 instance using GitHub Actions. It includes secure handling of SSH credentials via GitHub secrets, automation of code transfer, and remote app restart through systemd. The app is hosted on EC2 and accessible via HTTP.

---

## 🔧 Project Overview

This repository contains:

- A simple Flask app (`app.py`)
- A `requirements.txt` for dependency management
- A `.github/workflows/deploy.yml` GitHub Actions workflow to automate deployment to an EC2 instance
- A systemd service configuration (set up manually on EC2) for process management

---

## 📁 Tech Stack

| Component       | Purpose                                    |
|----------------|---------------------------------------------|
| Flask (Python) | Web app framework                           |
| EC2 (AWS)      | Linux server hosting the application        |
| GitHub Actions | CI/CD orchestration                         |
| SCP / SSH      | Secure file transfer and remote commands    |
| systemd        | Process management for the Flask service    |

---

## ⚙️ Deployment Process

1. Code is pushed to the `master` branch.
2. GitHub Actions workflow triggers on push.
3. Actions workflow:
   - Checks out the code
   - Uses `scp` to copy project files to EC2 (`~/flaskapp`)
   - SSHs into EC2 to:
     - Kill any running Flask process
     - Install Python dependencies
     - Restart the systemd service (`flaskapp.service`)
4. Flask app is served on port `8080` and accessible publicly via EC2 public IP.

---

## 🔐 GitHub Secrets

| Secret Name     | Description                                |
|----------------|---------------------------------------------|
| `EC2_HOST`      | Public IP of the EC2 instance               |
| `EC2_USER`      | SSH username (e.g., `ec2-user`)             |
| `EC2_KEY`       | Contents of PEM private key for SSH access  |

These secrets are used by the GitHub Actions `scp` and `ssh` steps for secure access.

---

## 🧾 Systemd Service Example (on EC2)

Path: `/etc/systemd/system/flaskapp.service`

```ini
[Unit]
Description=Flask App
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/flaskapp
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 📡 Access the App

Once deployed and running, the app can be accessed via:
```
http://<EC2_PUBLIC_IP>:8080
```

Make sure your EC2 Security Group allows inbound traffic on port 8080.

---

## 📦 Project Structure

```
.
├── app.py
├── requirements.txt
├── .gitignore
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## 📚 Related Projects and Roadmap

This project is part of a larger DevOps roadmap that includes:

| Step | Project                                           | Skills Covered                                 |
|------|---------------------------------------------------|-----------------------------------------------|
| 1️⃣   | Host static site on S3                           | AWS, S3 configuration, IAM                     |
| 2️⃣   | Automate S3 deployment with GitHub Actions       | CI/CD, AWS CLI, secrets                        |
| 3️⃣   | Launch EC2 + setup Python Flask app              | Linux, EC2, SSH                                |
| 4️⃣   | Deploy Flask to EC2 via GitHub Actions           | CI/CD pipelines, automation, remote exec       |
| 5️⃣   | Dockerize the EC2 app                            | Docker, containerization                       |
| 6️⃣   | Push Docker image to DockerHub via GitHub Actions| Docker registries, CI integration              |
| 7️⃣   | Run Docker container on EC2                      | Cloud deployment, container runtime            |
| 8️⃣   | Add basic Bash or CloudWatch monitoring          | Scripting, system metrics                      |
| 9️⃣   | Simulate SHIP-HATS style gated pipeline          | GovTech pipelines, security policies           |

---

## 📄 License
MIT


