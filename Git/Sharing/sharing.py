import streamlit as st

def sharing():
    st.header('Sharing & Updating')
    st.write("")
    st.write('''
            Local repository can be extended to remote repository which enables
            colaboration between various contributors working on or from the same code base.

            ''')
            
    st.write('''''')
    st.write('''''')

    with st.expander('Share & Update'):
        st.write('''

            

            | Command                               | Description                                  |
            |---------------------------------------|----------------------------------------------|
            | git push origin [branch name]         | Push a branch to your remote repository      |
            | git push -u origin [branch name]      | Push changes to remote repository (and remember the branch)|
            | git push                              | Push changes to remote repository (remembered branch)|
            | git push origin --delete [branch name]| Delete a remote branch|
            | git pull                              | Update local repository to the newest commit|
            | git pull origin [branch name]         | Pull changes from remote repository|
            | git fetch                             | Fetch all branches from the remote|
            | git add remote origin url             | Adding remote git repository|
            | git remote set-url origin ssh://git@github.com/[username]/[repository-name].git| Set a repository's origin branch to SSH|

            ''')


    
        
