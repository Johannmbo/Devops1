pipeline {
    agent any

    environment {
        ANSIBLE_PLAYBOOK = "ansible/playbook.yml"  // Path to the playbook  
        INVENTORY_FILE = "ansible/inventory/hosts"  // Path to the inventory file  
        ANSIBLE_BECOME_PASS = "001999"
    }

    stages {
        stage('Environment setup') {
            steps {
                script {
                    echo "step1: Environment setup (docker installation, repositories cloning)"
                }
                sshagent(['johann']) { // Use the ID you set for your SSH credentials  
                    sh """
                        ansible-playbook ${ANSIBLE_PLAYBOOK} -i ${INVENTORY_FILE} --tags docker_setup,clone_repository  
                    """
                }
            }
        }

        stage('Launching applications') {
            steps {
                script {
                    echo "Step 2: Launching applications (Docker Compose)"
                }
                sshagent(['johann']) { // Use the ID you set for your SSH credentials  
                    sh """
                        ansible-playbook ${ANSIBLE_PLAYBOOK} -i ${INVENTORY_FILE} --tags start_services  
                    """
                }
            }
        }
    }
}
