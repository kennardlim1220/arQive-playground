Commit whatever you feel like.
Note: I recommend you watch https://www.youtube.com/watch?v=tRZGeaHPoaw for the visual. You don't have to though. This is just a extremely simplified version of that tutorial.

## Instructions
#Getting started
1. Download git here: https://git-scm.com/downloads. Just use all of the default settings.
2. Use Git by either using the built your computer built in terminal (command prompt, terminal, etc) or use git bash from your git installation. Most of the intstruction assumes you are using linux.
3. Set up git
   `git config --global user.name "<your name>"`  
   `git config --global user.email <your email>` 
4. Go to where you want the project be.
   `cd ~`
5. Clone the repository  
   - `git clone https://github.com/kennardlim1220/arQive-playground.git`
6. Enter the directory
   - `cd ./arQive-playground` 
7. Whenever you begin, make sure your local repository is updated
   -`git pull origin main`

#Adding a file.
1. Create a new branch for whatever you are going to do.  
   1. Create a branch called newFile 
      `git branch newFile`
   2. Switch into that branch that you just created
      `git switch newFile`
   -  use `git checkout -b newFile` to create and switch into a new branch in 1 line.
   -  use `git branch` to ensure that you are using the correct branch (newFile)
2. Edit the file. Replace <your name> with your name.
     1. `nano <your name>.txt`
     2.  Add whatever you want into the file.
     3.  press ctrl + x, y, and finally enter to save and leave
3. Tell git you are finished editing the files.
   1. Add the files
      `git add <your name>.txt`
   2. Commit the file
      `git commit -m "added <your name>.txt"` 
4. Push it to the repository
   `git push -u origin newFile`
#Editting a file
1. Make a branch called update-names.txt
   `git switch -c update-names.txt`
2. Edit the file names.txt and add your name.
   `nano names.txt`, add your name to the file, then save.
3. 
