# Note: For your next activity, use git pull to get the rest of the branches. Then switch to the debug branch with `git switch debug`. Read the file debug.py for your task.
# DO NOT PUSH IT TO ORIGIN UNTIL EVERYONE IS FINISHED. If someone did, then go `git switch debug` -> `git merge debug_archive` -> `git restore .` 

Commit whatever you feel like.
Note: I recommend you watch https://www.youtube.com/watch?v=tRZGeaHPoaw for the visual of what every git commands looks like.
Also, check out https://git-scm.com/docs/gittutorial, which is the official git tutorial.

## Instructions
Note: Most of these command assumes you are using a linux server except when visiting a url
#

# Getting started
1. Set up git  
   `git config --global user.name "<your name>"`  
   `git config --global user.email <your email>`  
2. Go to where you want the project be.  
   `cd ~`  
3. Clone the repository  
   - `git clone https://github.com/kennardlim1220/arQive-playground.git`  
4. Enter the directory
   - `cd ./arQive-playground` 
5. 
   -`git config pull.ff true` You only need this once  
   -`git pull`
# Adding a file.
1. Create a new branch for whatever you are going to do.  
   1. Create a branch called with the same name as your name.  
      `git branch <your name>`
   2. Switch into that branch that you just created  
      `git switch <your name>`
   -  use `git switch -c <your name>` to create and switch into a new branch in 1 line.  
   -  use `git branch` to ensure that you are using the correct branch (*<your name>)  
2. Edit the file. Replace <your name> with your name.  
     1. `nano <your name>.txt`
     2.  Add whatever you want into the file.  
     3.  press ctrl + x, y, and finally enter to save and leave  
3. Tell git you are finished editing the files.  
   1. Add the files  
      `git add <your name>.txt` <br />
      Note: repeat `git add <your file>` for each file you want to commit.
   2. Commit the file
      `git commit -m "added <your name>.txt"` 
4. Push it to the repository
   `git push -u origin <your name>`
5. Go to the repository on your host machine: https://github.com/kennardlim1220/arQive-playground.git  
6. Click branches -> New pull request -> Create pull request  
NOTE: DO NOT MERGE YOUR OWN PULL REQUEST. Honestly, it doesn't matter in the arQive-playground, but don't do it in the actual production.  

# Dealing with merge conflict  
1. Get a merge conflict
   ##Making a merge conflict
   1. Make a branch to have a merge conflict
      `git switch -c merge_conflict`
   2. Make any change to merge-conflict.txt and commit it.
      ```
      echo "I'm from the merge_conflict branch" > merge-conflict.txt
      git commit -m "merge-conflict branch merge conflict" merge-conflict.txt
      ```
   3. Go back to main.
      `git switch main`
   4. Edit merge-conflict in main and commit it.
      ```
      echo "I'm from the main branch" > merge-conflict.txt
      git commit -m "main branch merge conflict" merge-conflict.txt
      ```
   5. Try to merge
      1. `git switch main`
      2. `git merge merge_conflict`
         You should see something like: 
         >Auto-merging merge-conflict.txt  
         CONFLICT (content): Merge conflict in merge-conflict.txt  
         Automatic merge failed; fix conflicts and then commit the result.  
      
         If you read the file, it should have something like this:
         ```
         <<<<<<< HEAD
         I'm from the main branch
         =======
         I'm from the merge_conflict branch
         >>>>>>> merge_conflict
         ```
      3. Use `git status` to see the current staus. Unmerged path should show merge-conflict.txt
      4. Communicate with whoever committed those changes, edit the file as needed, then commit the changes.  
         -`nano merge-conflict.txt` and edit the file as needed
         -`git add merge-conflict.txt
         -`git commit -m "merge conflict resolved"`

# Editting an existing file
1. Make a branch called update-names.txt
   `git switch -c update_names.txt`
2. Edit the file names.txt and add your name.
   `nano names.txt`, add your name to the file, then save.
3. Commit the file.
   1. `git add names.txt`
      -use `git add <fileName>` as needed for each file.
      -use `git add .` to add everything. Not recommended in case you added a file you were not supposed to.
   2. `git commit -m "added my name to the names file"
4. `git push -u origin update_names.txt`
5. Go to the repository on your host machine.
6. Click branches -> New Pull Request -> Create pull request
7. During production, it is possible that someone edited the file and had it merged with the main branch in the mean time.

# Notes:
Pre-existing rules from previous years:
Contribution Rules

✔️ Never work on master or production branch!

⚠️ Be sure to branch off the development branch for features WIP

⚠️ Branch off of the production branch for hot fixes


✔️ Create a new branch for each set of related bugs or set of related tasks, naming by:


type_PascalCase, example: feat_CareerPage, bug_CareerEmail.


Common short type tokens: wip (work in progress), feat (feature or design), bug (bug fixes)


💻 command to create new branch locally: git checkout -b bug_CareerEmail


⚠️ Important: Before creating a branch, check if someone already started to work on this task and if there's already a branch created for this task, and if there is, please checkout and track the branch with the 💻 command: git checkout --track origin/bug_CareerEmail


--track shorthand for git checkout -b [branch] [remotename]/[branch] where remote name is origin and branch is the specific branch you're pulling from the origin remote


Right after creating a new branch, push it to remote to make it available for everyone, defining the upstream


💻 command: git push -u origin bug_CareerEmail


✔️ Everyday after working, push your local branch updates to remote branch.


⚠️ Important: make sure you're on the correct branch... and push


With 💻 command: git push


✔️ Finished with the task and want to merge?


Fix conflicts if needed, usually happens when more than 1 developer is working on the same file on different branches - communicate with the other developer to make sure their work was not removed


Please make the merge/pull request with as much detail about what you've done/added.


Or lead will merge your branch to master for you. Just ask!


