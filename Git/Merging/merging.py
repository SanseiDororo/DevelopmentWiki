import streamlit as st

def merging():
    st.header('Merging')
    st.write("")
    st.write('''
            Merging of branches is one of the most important operations in the git flow. After
            developing a specific feature under the context of isolated branch, we need to
            merge it with the main branch at some point. There are several approaches with
            specific benefits and caveats. 

            ''')
            
    st.write('''''')
    st.write('''''')

    with st.expander('Fast Forward'):
        st.write('''

            If the main branch remains intact after we create an isolated branch out of it,
            git performs fast-forward merge procedure. This means that moves pointer of the main branch
            at the end of the feature branch.

            Fast forward merge produces consistent progress line but can cause inadequate commit history.
            It is not the most suitable merge strategy for the large projects.

            Precedure:
            * Checkout feature branch
            * Make new commits
            * Checkout target branch
            * Merge Feature branch
            

            ''')

    with st.expander('Rebasing'):
        st.write('''

            Git allows tracking changes on the main and feature branch simultaneously.
            This means that it is possible to update changes on the main branch in order
            to perform fast forward merge. This establish linear history instead of 3-way
            merge. Technically rebasing moves the pointer to the last made commit. Tradeoff of 
            making linear history is incomplete history of all commits.

            Procedure:

            * git checkout branch_name
            * git rebase main
            * git checkout main
            * git merge branch_name 
            

            ''')

    with st.expander('3 - way merge'):
        st.write('''

            3 - way merge allows rejoing different branches even if they were changed.
            Git compares main branch and the feature branch and defines the common ancestor 
            of the both. If there aren't any conflicts new merge commit is created. 

            3 - way merge preserves adequate commit history but produces complex progress
            line.

            ''')

    


   


    

   

        
        
