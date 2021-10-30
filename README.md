# Linux Setup Environment:....

1. Download VSCode - https://code.visualstudio.com/download
2. Download python - https://www.python.org/downloads/
3. Download python extension in VScode - https://code.visualstudio.com/download
4. sudo apt install git-all ### Download git
5. git config --global user.name "username" ### Add a username to the git config file
5. git config --global user.email email ### add an email to the git config file
6. git config --global core.editor "code --wait" ### add VScode as the default editior and have it wait until it is manually closed
7. git config --global core.autocrlf input ### tell git how to handle end of lines for linux and MAC only. If on windows set input to true instead
8. git init ### cd into the folder and then use this command to initialize the repository
9. git config --global init.defaultBranch branch_name ### Set the defaultBranch name
10. Create a file and make your first commit using git add --all and git commit -m "message"
11. Go to git hub and create a new repository - https://github.com/
12. git remote add origin https://github.com/git_hub_username/name_of_repository.git ### Since We already created a repository we are going to add it to github. Git hub will show you the commands once you make the repository
13. git push origin master ### push your work to the new repository that was just created. You will need your username and a token for the password. The token can be set up here - https://github.com/settings/tokens
14. git config --global diff.tool vscode ### set VScode as the default diff tool
15. git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE" ### tell git how to open VScode for the diff tool 
16. git config --global -e ### open the config file and make sure $LOCAL and $REMOTE are added
17. 

# Git Token:....

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 ### Token for pushing

# Git Kraken:....

1. download Git Kraken - https://www.gitkraken.com/download 
2. Open the REPO that was initlized

gitkraken ### Used to open Git Kraken from the terminal

# Master Branch:....

master/core ### Default master branch name ?? Still figuring this one out
master ### Main Branch that holds all features


