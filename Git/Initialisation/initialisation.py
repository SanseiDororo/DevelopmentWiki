import streamlit as st

def initialisation():
    st.header('Initialisation')
    st.write("")
    st.write('''
            In order to change a local folder into a git repository, we need a working version
            of git installed on the host machine. Most of the operation systems support git. 
            There are several graphical environments enabling execution of git commands but CLI 
            is still most commonly used.
            

            Every git project has 3 main stages:

            * Working Directory
            * Staging Area or Index (git add)
            * Git repository (git commit)

            ''')
            
    st.write('''''')
    st.write('''''')

    with st.expander('Configuration'):
        st.write('''

            

            | Command                               | Description                                  |
            |---------------------------------------|----------------------------------------------|
            | git config --global user.name ['']    | set username to credit version reviews            |
            | git config --global user.email ['']   | set email to which will be associated with history maker|
            | git config --global color.ui auto     | set automatic command line coloring|

            ''')


    with st.expander('Initialising Projects'):
        st.write('''

            

            | Command                               | Description                                  |
            |---------------------------------------|----------------------------------------------|
            | git init                              | Initialize a local Git repository            |
            | git clone ssh://git@github.com/[username]/[repository-name].git  | Create a local copy of the repository|
            
                                                         
        
        ''')

    with st.expander('Basic Snapshoting'):
        st.write('''

            

            | Command                               | Description                                  |
            |---------------------------------------|----------------------------------------------|
            | git status                            | Check status of the reposito       |
            | git add [file-name.txt]               | Add file to the staging area       |
            | git add -A                            | Add all tracked and changed files to staging      |
            | git reset file                        | Unstage file. Changes in the working directory retain.      |
            | git diff                              | Review unstaged changes|
            | git diff --staged                     | Review staged but not yet commited changes      |
            | git commit -m "[commit message]"      | Commit staged files with commit message       |
            | git rm -r [file-name.txt]             | Remove files from staging      |
                                                         
        
        ''')


    

   

        
        
