pipeline {
    agent any

    environment {
        ANSIBLE_PLAYBOOK = "ansible/playbook.yml"  // Путь до playbook
        INVENTORY_FILE = "ansible/inventory/hosts"      // Путь до inventory-файла
        ANSIBLE_BECOME_PASS =  "001999"
    }

    stages {
        stage('Environment setup') {
            steps {
                script {
                    echo "step1: Environment setup (docker installation, repositories cloning)"
                }
                sshagent(['devopslab']) { // Use the ID you set for your SSH credentials 
                sh """
                    ansible-playbook ${ANSIBLE_PLAYBOOK} -i ${INVENTORY_FILE} --tags docker_setup,clone_repository
                """
            }
        }

        stage('Launching applications') {
            steps {
                script {
                    echo "Этап 2: Launching applications (Docker Compose)"
                }
                sshagent(['devopslab']) { // Use the ID you set for your SSH credentials
                sh """
                    ansible-playbook ${ANSIBLE_PLAYBOOK} -i ${INVENTORY_FILE} --tags start_services
                """
            }
        }
    }
}
