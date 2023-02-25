import streamlit as st

def branching():
    st.header('Branching')
    st.write("")
    st.write('''
            Branches are isolated development lines which can be merged into the main development tree 
            at any time. Branches allow developers to code features saparetely in regards to the code base.
            Isolating work in branches makes reviewing, commenting, testing and approving changes much easier.
            Besides, development history is transparent and more easily managable. Technically branches are 
            pointers to a snapshots of produced changes.  

            Branches are stored in .git/refs/heads folder

            ''')
            
    st.write('''''')
    st.write('''''')

    with st.expander('Branching'):
        st.write('''

            

            | Command                               | Description                                  |
            |---------------------------------------|----------------------------------------------|
            | git branch                            | List branches (the asterisk denotes the current branch)          |
            | git branch -a                         | List all branches, local and remote          |
            | git branch [branch name]              | Create new branch                            |
            | git branch -d [branch name]           | Delete branch                                |
            | git push origin --delete [branch name]| Delete a remote branch                       |
            | git checkout -b [branch name]         | Create new branch and switch to it           |
            | git checkout -b [branch name] origin/[branch name] | Clone a remote branch and switch to it                               |
            | git branch -m [old branch name] [new branch name]           | Rename local branch    |
            | git checkout [branch name]            | Switch to a branch    |
            | git checkout -                        | Switch to a last checkout branch    |
            | git checkout -- [file-name.txt]       | Discard changes to a file    |
            | git checkout -- [file-name.txt]       | Discard changes to a file    |
            | git merge                             | Merge a branch into the active branch    |
            | git merge [source branch] [target branch]  | Merge a branch into the target branch    |
            | git stash                             | Stash changes in a dirty directory    |
            | git stash clear                       | Remove all stashed entries    |
           
            
            

            ''')


   


    

   

        
        
