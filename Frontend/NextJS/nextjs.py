import streamlit as st

def nextjs():
    st.header('Next JS')
    st.write("")
    st.write('''
            Next.js is a popular React framework for building web applications that offers the 
            following key features:
            * Server-Side Rendering (SSR): Next.js allows you to render React components on the server, delivering faster initial page loads and improved SEO.
            * Client-Side Routing: It provides a built-in routing system for creating single-page applications with dynamic client-side routing, allowing seamless navigation between pages.
            * Static Site Generation (SSG): Next.js supports generating static HTML files for improved performance and easier deployment, while still allowing dynamic data updates.
            * Automatic Code Splitting: It automatically optimizes your application by splitting code into smaller chunks, ensuring that only the necessary JavaScript is loaded for each page.
            * API Routes: You can create API endpoints within your Next.js application, making it easy to handle server-side logic and data retrieval.
            * File-Based Routing: Pages in Next.js are created by simply adding files to a pages directory, following a convention that maps filenames to routes.
            * Dynamic Routing: Next.js supports dynamic routing by using brackets in filenames, allowing for flexible and parameterized routes.
            * A Rich Ecosystem: It has a vibrant ecosystem with support for various plugins, tools, and extensions, making it easy to extend and customize your application.

            ''')

    st.write(''' ''')
    st.write(''' ''')
    
    with st.expander("Create app"):
        st.write(
            '''
              We can create next app with the prefered package manager, for exampke pnpm

              ```
                pnpmx create-next-app@latest
              ```  

              This gives us dialoge screen with several options we can chose from.

            '''
            )
        
   
    

   

        
        
