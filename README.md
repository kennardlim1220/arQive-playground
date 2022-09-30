Commit whatever you feel like.
Note: I recommend you watch https://www.youtube.com/watch?v=tRZGeaHPoaw for the visual. You don't have to though. This is just a stupidly simplified version of that tutorial.

## Instructions
0. Set up git
   `git config --global user.name "<your name>"`  
   `git config --global user.email <your email>`  
1. Create a folder to put this project in. For simplicity, we will use ~  
   - `cd ~`  
2. Clone the repository  
   - `git clone https://github.com/kennardlim1220/arQive-playground.git`  
3. Enter the directory  
   - `cd ./arQive-playground`  
4. Create a new branch for whatever you are going to do.  
   1. Create a branch called update-names.txt (not a txt file)  
      `git branch update-names.txt`
      Don't forget to change <your name> to your name
   2. Switch into that branch that you just created
      `git switch update-names.txt`
      alternatively: `git checkout update-names.txt`
      use `git branch` to ensure that you are using the correct branch (update names)
5. Edit the file. You can do this however you like (nano, vim, notepad)
   - nano
     1. `nano names.txt`
     2.  Add your name
     3.  press ctrl + x, y, and finally enter to save and leave
   - vim
     1. `vim names.txt`
     2. press i to enter insertion mode (to edit the file)
     3. enter your name into the file
     4. press esc to exit insertion mode
     5. type `:wq` and press enter to save and exit vim
   - echo (Not recommended, just happens to be the easiest)
     Don't forget to replace "your name" with your name. Don't remove the quote.
     `echo "<your name>" >> names.txt`
7. Tell git you are finished editing the files.
   1. Add the files
      `git add names.txt`
   2. Commit the file
      `git commit -m "added <your name>"`
   Alternatively: `git commit -a -m "added <your name>"`
8. Go back to the main branch
   `git switch main`
Optional:
use `cat README.md` to see that the change is not longer there. This is because you made the changes in the update-names.txt branch instead of the main branch. You need to merge them to keep the change.
9. Merge the changes to the main branch
   `git merge -m "merge message" update-names.txt`
   `git merge update-names.txt` if you don't care about the merge message
10. Delete the now useless branch
    `git branch -d update-names.txt
11. More than likely, you will have a merge conflict. We are now going to simulate it. edit merge-conflict.txt 
    1. Create a new branch and use it `git branch merge-conflict` then `git switch merge-conflict`  
       Alternatively: `git switch -c merge-conflict` -c is used to create a new branch to switch into
    2. Edit the file however you like. I am going to use `echo "This is the merge-conflict branch text" >> merge-conflict.txt`. 
    3. Go back to your original branch
       `git switch main`
    4. Edit merge-conflict.txt
       `echo "This is the main branch text"`
    5. Attempt to merge them together
       `git merge merge-conflict`
    6. Edit the files to solve the merge conflict however you want. You should see 

