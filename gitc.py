# git inits
# git add .
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/chandni-melwani/gitc.git
# git push -u origin main

# git commit --amend  || git commit --amend -m "Initial commit"
# git branch || show all b
# git branch feature1 || make a new
# git checkout main || switch to main b
# git checkout -b feature1 || make a new an dswitch to it
# git remote -v


# Pipeline Task 1:
# pipeline {
#  agent any
#  stages {
#  stage('Checkout Code') {
#  steps {
#  git 'https://github.com/your-username/your-repo.git'
#  }
#  }
#  stage('Show Files') {
#  steps {
#  bat 'dir'
#  }
#  }
#  }
# }

# pipeline {
#   agent any
#   stages {
#     stage('Checkout Code') {
#       steps {
#         git 'https://github.com/your-username/your-repo.git'
#       }
#     }
#     stage('Print Directory') {
#       steps {
#         bat 'cd'
#       }
#     }
#   }
# }

# pipeline tast3

# pipeline {
#   agent any
#   stages {
#     stage('Checkout Code') {
#       steps {
#         git 'https://github.com/your-username/your-repo.git'
#       }
#     }
#     stage('Print Message') {
#       steps {
#         echo 'Hello! Jenkins Pipeline executed successfully'
#       }
#     }
#   }
# }


#Pipeline task 4:
# pipeline {
#   agent any
#   stages {
#     stage('Checkout Code') {
#       steps {
#         git 'https://github.com/your-username/your-repo.git'
#       }
#     }
#     stage('Create File') {
#       steps {
#         bat 'echo This file is created by Jenkins > demo.txt'
#       }
#     }
#   }
# }
#
# Pipeline task 5:
# pipeline {
#   agent any
#   stages {
#     stage('Checkout Code') {
#       steps {
#         git 'https://github.com/your-username/your-repo.git'
#       }
#     }
#     stage('Read File') {
#       steps {
#         bat 'type README.md'
#       }
#     }
#   }
# }
