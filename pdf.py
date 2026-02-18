# ==============================
# A) Setup & Configuration
# ==============================

# Check installed Git version
# git --version

# Set username globally (one-time setup)
# git config --global user.name "Your Name"

# Set email globally (one-time setup)
# git config --global user.email you@example.com


# ==============================
# B) Create or Clone Repositories
# ==============================

# Initialize a new Git repository in current folder
# git init

# Clone a remote repository
# git clone <repository-url>


# ==============================
# C) Check Status
# ==============================

# Show current status (modified, staged, untracked files)
# git status


# ==============================
# D) Add Files (Staging Area)
# ==============================

# Stage a specific file
# git add file.txt

# Stage all changed files
# git add .


# ==============================
# E) Commit Changes
# ==============================

# Create a new commit with a message
# git commit -m "Message"

# Amend (edit) the most recent commit (message or content)
# git commit --amend


# ==============================
# F) View History
# ==============================

# Show full commit history
# git log

# Show compact commit history
# git log --oneline

# Show visual branch history
# git log --oneline --graph --all


# ==============================
# G) Branching
# ==============================

# List all branches
# git branch

# Create a new branch
# git branch <name>

# Switch to an existing branch
# git checkout <name>

# Create and switch to a new branch
# git checkout -b <name>


# ==============================
# H) Merging
# ==============================

# Merge a branch into the current branch
# git merge <branch-name>


# ==============================
# I) Remote Repository (GitHub)
# ==============================

# Add a remote repository named origin
# git remote add origin <url>

# View configured remotes
# git remote -v

# Push changes to main branch on GitHub
# git push origin main

# First push: set upstream and push
# git push -u origin main

# Pull latest changes (fetch + merge)
# git pull origin main

# Fetch latest changes (no merge)
# git fetch


# ==============================
# J) Undo / Reset / Restore
# ==============================

# Restore a file to last committed state
# git restore file.txt

# Unstage a staged file
# git restore --staged file.txt

# Undo last commit but keep changes staged
# git reset --soft HEAD~1

# Undo last commit, keep changes in working directory
# git reset --mixed HEAD~1

# Undo last commit and delete changes (dangerous)
# git reset --hard HEAD~1

# Safely undo a commit by creating a new reverse commit
# git revert <commit-id>


# ==============================
# K) Stash (Temporary Save)
# ==============================

# Save uncommitted work temporarily
# git stash

# List all stashes
# git stash list

# Apply the latest stash (keep it in stash list)
# git stash apply

# Apply and remove the latest stash
# git stash pop


# ==============================
# L) Tagging (Release Versions)
# ==============================

# Create a tag (release version)
# git tag v1.0

# Push a specific tag to GitHub
# git push origin v1.0

# Push all tags to GitHub
# git push --tags
