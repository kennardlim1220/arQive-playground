To complete your exercise, you must first revert this file. 
First type in `git log`. You should see something that says:
commit 76ab22c0eec096f4a274c5e483f15aa8e8c44385 (HEAD -> debug)
Author: Kennard Lim <kennardlim1220@gmail.com>
Date:   Thu Oct 27 17:52:05 2022 -0700

    Initialized debug.py
    
Copy the commit hashcode.
Then type `git restore <hashcode>`
Example: `git restore 76ab22c0eec096f4a274c5e483f15aa8e8c44385`
Note: You will only need enough character for the hash to be uniquely identified. The first 6 should work, so:
`git restore 76ab22c` will also usually work.

It will not change the files. You will need to type `git restore .` to restore all the files to how they were right after this commit.