import os

# Root folder
root = "KnowledgeVault"

structure = {
    "00-Foundations": {
        "Linux": [
            "File-System.md",
            "Permissions.md",
            "Processes.md",
            "Systemd.md",
            "Networking-Commands.md",
            "Package-Management.md",
            "Performance-Monitoring.md",
            "Troubleshooting.md",
        ],
        "Networking": [
            "OSI-Model.md",
            "TCP-vs-UDP.md",
            "DNS.md",
            "HTTP-HTTPS.md",
            "Load-Balancing.md",
            "Reverse-Proxy.md",
            "Subnetting.md",
            "Common-Network-Issues.md",
        ],
        "Git-GitHub": [
            "Git-Basics.md",
            "Branching-Strategy.md",
            "Merge-vs-Rebase.md",
            "Git-Internals.md",
            "GitHub-Actions.md",
            "SSH-Setup.md",
            "Troubleshooting.md",
        ],
    },
    "01-Scripting": {
        "Shell-Scripting": [
            "Variables.md",
            "Loops-Conditions.md",
            "Cron-Jobs.md",
            "Log-Parsing.md",
            "Automation-Examples.md",
        ],
        "Python-Automation": [
            "Virtualenv.md",
            "File-Handling.md",
            "API-Requests.md",
            "Automation-Scripts.md",
            "CLI-Tools.md",
        ],
    },
    "02-Containers": {
        "Docker": [
            "Docker-Basics.md",
            "Dockerfile-Best-Practices.md",
            "Volumes.md",
            "Networking.md",
            "Debugging.md",
        ],
        "Kubernetes": [
            "K8s-Architecture.md",
            "Pods.md",
            "Deployments.md",
            "Services.md",
            "Ingress.md",
            "ConfigMaps-Secrets.md",
            "RBAC.md",
            "Helm.md",
            "kind-Setup.md",
            "Troubleshooting.md",
        ],
    },
    "03-IaC": {
        "Terraform": [
            "Basics.md",
            "Providers.md",
            "Modules.md",
            "State-Management.md",
            "Remote-Backend.md",
            "Best-Practices.md",
        ],
        "Ansible": [
            "Inventory.md",
            "Playbooks.md",
            "Roles.md",
            "Variables.md",
            "Vault.md",
            "Debugging.md",
        ],
    },
    "04-CI-CD": [
        "CI-CD-Concepts.md",
        "GitHub-Actions-Pipelines.md",
        "Jenkins.md",
        "Artifact-Management.md",
        "Deployment-Strategies.md",
    ],
    "05-Cloud": {
        "AWS": [
            "EC2.md",
            "IAM.md",
            "VPC.md",
            "S3.md",
            "RDS.md",
            "Monitoring.md",
        ],
        "Cloud-Concepts.md": None,
    },
    "06-Observability": [
        "Logging.md",
        "Monitoring.md",
        "Prometheus.md",
        "Grafana.md",
        "Alerting.md",
    ],
    "07-Security": [
        "Linux-Security.md",
        "Network-Security.md",
        "IAM-Policies.md",
        "Secrets-Management.md",
        "DevSecOps.md",
    ],
    "08-Projects": [
        "Mini-Projects.md",
        "Production-Deployment.md",
        "Mistakes-I-Faced.md",
        "Architecture-Diagrams.md",
    ],
    "09-Interview-Prep": [
        "Linux-QA.md",
        "Networking-QA.md",
        "Kubernetes-QA.md",
        "Terraform-QA.md",
        "Scenario-Based.md",
        "HR-Round.md",
    ],
}


def create_structure(base_path, tree):
    for name, content in tree.items():
        current_path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(current_path, exist_ok=True)
            create_structure(current_path, content)

        elif isinstance(content, list):
            os.makedirs(current_path, exist_ok=True)
            for file in content:
                file_path = os.path.join(current_path, file)
                open(file_path, "a").close()

        elif content is None:
            # Single markdown file inside folder
            file_path = os.path.join(base_path, name)
            open(file_path, "a").close()


# Create root
os.makedirs(root, exist_ok=True)

# Build everything
create_structure(root, structure)

print("KnowledgeVault structure created successfully!")