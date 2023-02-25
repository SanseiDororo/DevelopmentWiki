import streamlit as st

def commiting():
    st.header('Commiting')
    st.write("")
    st.write('''
            Commiting is probably one of the most importand operations in the git flow.
            It moves files from working folder to staging. 

            ''')
            
    st.write('''''')
    st.write('''''')

    with st.expander('Operations'):
        st.write('''

            

            | Command                               | Description                                  |
            |---------------------------------------|----------------------------------------------|
            | git commit -m                         | Making commit and add message                |
            | git show <sha_of_the_commit>          | Inspect specific commit                      |
            | git commit --amend -m                 | Adjusting last commit and adding message     |
            | git cherry-pick <sha_of_the_commit>   | Pick specific commit and set it as last of the branch |
            | git cherry-pick <sha_of_the_repository> --no-commit | Not commiting cherry picked commit |
            | git stash                             | Saving uncommited work without committing |
             
                                 
           
            
            

            ''')

    


   


    

   

        
        
