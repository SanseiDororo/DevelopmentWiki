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
                pnpx create-next-app@latest
              ```  
              This gives us dialoge screen with several options we can chose from.
            '''
            )
    with st.expander("Authentification with Clerk"):
        st.write(
            '''
              Clerk is service which provides simple authentification integration.
              [More about Clerk]('https://clerk.com/docs')
              1. In order to be able to use Clerk, you need to sign in and create app
              ```
                * Create App
                * Define sign in methods (google, apple etx.)
                * Copy environment keys in .env file of the project
              ```  
              2. Install Clerk inside the project
              ```
                pnpm install @clerk/nextjs
              ```
              3. Wrap html object inside the app/layout.tsx with Clerk Provider

              ```
                import { ClerkProvider } from '@clerk/nextjs'

                return (
                    <ClerkProvider>
                      <html lang="en">
                        <body>{children}</body>
                      </html>
                    </ClerkProvider>
                    )
              ```
              4. Create route protection policy by makin middleware.ts file inside you project folder
              ```
                import { authMiddleware } from "@clerk/nextjs";

                // This example protects all routes including api/trpc routes
                // Please edit this to allow other routes to be public as needed.
                // See https://clerk.com/docs/references/nextjs/auth-middleware for more information about configuring your Middleware
                export default authMiddleware({});
                export const config = {
                  matcher: ['/((?!.+\\.[\\w]+$|_next).*)', '/', '/(api|trpc)(.*)'],
                };

              ```
              5. Build sign-in and sign-up pages
              Inside app folder create (auth) folder and put sign-in and sign-up folder insied. It the 
              sign-in folder create [[...sign-in]] folder and do the same in sign-up folder [[...sign-up]].
              Put page.tsx in both folders. 
              SignUp page
              ```
                import { SignUp } from "@clerk/nextjs";

                export default function Page() {
                  return <SignUp />;
                }
              ```
              SignIn page
              ```
                import { SignIn } from "@clerk/nextjs";
                export default function Page() {
                  return <SignIn />;
                }
              ```
            6. Create User Button in app page.tsx
            ```
                import { UserButton } from "@clerk/nextjs";

                export default function Home() {
                  return (
                    <div>
                      <UserButton afterSignOutUrl="/"/>
                    </div>
                  )
                }
            ```
            '''
            )
    with st.expander("Shadcn Components"):
      st.write(
        '''
          ShadCN is a component library providing most of the required components to build
          your app.

          1. Installation

          ```
            pnpx shadcn-ui@latest init
          ```

          2. Customize according to the needs of you project.

          Most common setup:
          
          * Typescript
          * New York
          * Neutral
          * Default for globals.css
          * No for variables
          * tailwind default
          * default

          3. Add components for the projects.

          ```
            pnpx shadcn-ui@latest add
          ```
          You can add all by pressing a and enter.

        '''
        )    
  
    with st.expander('Switching Themes'):
      st.write(
        '''
          In order to create Theme Switcher we first need to install next-themes

          ```
            pnpm install next-themes
          ```
        '''
      )
  

          
          
