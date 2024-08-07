import streamlit as st

def react():
    st.header('React')
    st.write("")
    st.write('''
            React is contemporary open-source Javascript library for building UI.
            It is component based and uses virtual DOM to effectively update and
            render the components. It is based **unidirectional** data flow from parent
            to child component via props, ensuring a predictable and easy-to-understand 
            flow of data and reducing the chances of data inconsistencies.

            ''')

    st.write(''' ''')
    st.write(''' ''')
    
    with st.expander("Basics"):
        st.write(
            '''
            Basic building block of the react app is a component, reusable, self-contained 
            piece of code that encapsulates a specific part of a user interface (UI) and 
            its related functionality. Components allow you to break down your UI into smaller, 
            modular pieces.

            A React component can be thought of as a JavaScript function or a class that returns 
            a piece of JSX (JavaScript XML) code representing the UI. There are two main types of 
            components in React:

            * Functional Components: 
            
            Functional components are JavaScript functions that accept properties, known as props, 
            as input and return JSX to describe the UI. They are simpler and easier to understand 
            compared to class components. Functional components are typically used for presentational 
            or stateless UI elements.

            ```
                function Greeting(props) {
                     return <h1>Hello, {props.name}!</h1>;
                    };
            ```

            Props are used to pass data from a parent component to a child component.
                Props are immutable and are passed down the component tree. 

            ** Class Components: Class components are ES6 classes that extend the React.Component base class. 
            They have a more feature-rich API, including state management, lifecycle methods, and event 
            handling. Class components are suitable for more complex UI elements that require internal 
            state or lifecycle management.

            Example:

            ```
            class Counter extends React.Component {
              constructor(props) {
                super(props);
                this.state = { count: 0 };
              }

              increment() {
                this.setState({ count: this.state.count + 1 });
              }

              render() {
                return (
                  <div>
                    <p>Count: {this.state.count}</p>
                    <button onClick={() => this.increment()}>Increment</button>
                  </div>
                );
              }
            }

            ```

            Components must return one parent element otherwise interpreter will return an error.

            '''
            )
        
    with st.expander('JSX rules'):
        st.write(
            '''
                JavaScript XML is an extension to JavaScript syntax that allows you to write HTML-like 
                code within your JavaScript code in React applications.

                Basic Rules:

                * Use capitalized component names and self-closing tags.
                  ```<ExampleComponent />```
                * Wrap Multiple Elements
                  Multiple elements should be wrapped in a single parent element, would it be div, section or
                  simply 
                  ```React.Fragment aka <>```

                * Use Curly Braces for Expressions
                  ```<div>{variable}</div>```
                * Html classes should be classNames
                  ```<div className="simple-example"```
                * CSS inline styles
                  ```style = {paddingTop: 35px}```
                * Comments 
                  ```{/* This is a comment */}```         
            '''
            )
        
    with st.expander('Context API'):
        st.write(
            ''' 
            React's global context, also known as the Context API, allows you to share data across multiple 
            components in a React application without passing props manually through each intermediate component. 
            It provides a way to manage global state and make it accessible to any component that needs it.
            
            
            
            
            '''
            )
        
    with st.expander('React Hooks'):
        st.write(
            '''
                React hooks are functions that allow functional components to have state 
                and access other React features previously available only in class components. 
                Hooks provide a simpler and more concise way to write reusable and stateful logic 
                in functional components.

                * useState

                The useState hook allows you to add state to a functional component. 
                It returns a state value and a function to update that value.

                Example:

                ```
                    import React, { useState } from 'react';

                    function Counter() {
                      const [count, setCount] = useState(0);

                      const increment = () => {
                        setCount(count + 1);
                      };

                      return (
                        <div>
                          <p>Count: {count}</p>
                          <button onClick={increment}>Increment</button>
                        </div>
                      );
                    }

                ```
                useState hook is used to initialize state of the component, which is, in this case,
                count value of 0. When button is clicked, state gets updated and count increments for 1.
                The component rerenders and shows new value.
                
                ----
                
                * useEffect

                The useEffect hook is a built-in hook in React that allows you to perform side effects 
                in functional components. Side effects can include fetching data, subscribing to 
                events, manipulating the DOM, and more.

                The useEffect hook takes two arguments: a callback function and an optional dependencies 
                array. The callback function is executed after the component renders and re-renders. The 
                dependencies array allows you to specify values that the effect depends on, and the effect 
                will only re-run if any of the dependencies change.

                Example:

                ```
                import React, { useEffect } from 'react';

                function MyComponent() {
                  useEffect(() => {
                    // Code to be executed after the component renders or re-renders

                    // Example: Fetch data from an API
                    fetch('https://api.example.com/data')
                      .then(response => response.json())
                      .then(data => {
                        // Do something with the data
                        console.log(data);
                      });

                    // Example: Add event listener
                    const handleClick = () => {
                      console.log('Button clicked');
                    };
                    document.addEventListener('click', handleClick);

                    // Clean-up function
                    return () => {
                      // Code to be executed when the component unmounts or before the effect runs again

                      // Example: Remove event listener
                      document.removeEventListener('click', handleClick);
                    };
                  }, []); // Empty dependencies array to run the effect only once

                  return <div>My Component</div>;
                }

                ```
                ----
                * useRef

                The useRef hook is a built-in hook in React that allows you to create a mutable reference that
                persists across re-renders of a component. It provides a way to access and manipulate 
                DOM elements or store mutable values within a functional component.

                Example of accessing specific DOM element and attaching specific function with useRef:

                ```
                    import React, { useRef } from 'react';

                    function MyComponent() {
                      const inputRef = useRef();

                      const handleButtonClick = () => {
                        inputRef.current.focus(); // Accessing the input element and setting focus
                      };

                      return (
                        <div>
                          <input ref={inputRef} type="text" />
                          <button onClick={handleButtonClick}>Focus Input</button>
                        </div>
                      );
                    }


                ```
                ---
        
            '''

        )

    with st.expander('Conditional Rendering'):
        st.write(
            '''
                * Ternary Operator

                Ternary Operator is extremely useful part of React since it allows conditional rendering.
                The basic syntax is condition? expression_1:expression_2. Based on the condition react App
                renders certain part. This is extremely useful in combination with useState hook. 

                Example:
                ```
                    import React from 'react';

                    function MyComponent({ isLoggedIn }) {
                      return (
                        <div>
                          {isLoggedIn ? (
                            <p>Welcome, user!</p>
                          ) : (
                            <button>Login</button>
                          )}
                        </div>
                      );
                    }

                ``` 

                && Operator

                Example:

                ```
                import React from 'react';

                function MyComponent({ items }) {
                  return (
                    <div>
                      {items.length > 0 && (
                        <ul>
                          {items.map((item, index) => (
                            <li key={index}>{item}</li>
                          ))}
                        </ul>
                      )}
                      {items.length === 0 && <p>No items available.</p>}
                    </div>
                  );
                }

                ```

            '''
            
        )
      
    with st.expander('React Query / Tanstack Query'):
      st.write(
          '''
              React Query is a library to manage server states. It handles:
              * Loading/Error states
              * Prefething
              * Pagination
              * Mutations (Updates of data on the server)
              * De-duplication of the requests
              * Retry on error
              * Callbacks
              React Query maintains cache of the server data on the client. There are several ways
              and procedures how to update and fetch this data, which can be defined according to the
              user needs.

              In order to be able to use ReactQuery, we need to:

              * Install the library
              * Create query client which manages our queries and caches the data
              * Apply QuerContainerizationyProvider 
              * Define useQuery hook which fetches data from the server
              -------------------------------------

              BASIC SETUP

              In order to be able to use react query, we need to:

              ```
              // create a queryClient
              const queryClient = new QuertClient()

              // wrap the app with the QueryClient Provider and pass client as prop
              <QueryClientProvider client={queryClient}>
                <div className="App">
                  <Component />
                </div>
                </QueryClientProvider>
              ```


              ------

              On the level of the component in which we would like to render the received data,
              we need to initialize the useQuery hook, which returns a data and accepts an object
              of options as for example:

              * queryKey - what defines the received data in the query cache
              * queryFn - this is the function which runs to fetch the data
              * isLoading - checks if the data is loading
              * isError - checks if there was an error with loading the data

              -----
              DEVTOOLS

              ReactQuery devtools offer various aspects of inspection in regards to the used
              reactQueries. We can Refetch, Invalidate, Reset, Trigger Error and Loading etc. 
              Besides, we can inspect the data corresponding to a specific queryKey. In order
              to be able to use the devtools we need to import it and place it into the app:
              ```
                import { Posts } from './Posts'
                import './App.css'
                import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
                import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
                
                const queryClient = new QueryClient()
                
                function App() {
                  return (
                    // provide React Query client to App
                    <QueryClientProvider client={queryClient}>
                      <div className="App">
                        <h1>Blog &apos;em Ipsum</h1>
                        <Posts />
                      </div>
                      <ReactQueryDevtools />
                    </QueryClientProvider>
                  )
                }
                
                export default App

              ```
              --------
              INFINITE QUERY

              Infinite query hook is used to implement the infinite scroll.

              useInfiniteQuery has the following structure:
              
              ```
                useInfiniteQuery({
                  queryKey: ["key"],
                  queryFn: ({pageParam = initialUrl} => {fetchUrl(pageParam)})
                  getNextPageParam:(lastPage) => {return lastPage.next || undefined}
                })
                return (<InfiniteScroll loadMore={()=> if(!isFetching){fetchNextPage()}}hasMore={hasNextPage})>
                  {data.map(...)}
                  </InfiniteScroll>
              ```

              useInfitieQuery returns :

              * data: 
              * fetchNextPage: function which returns more available data
              * hasNextPage: boolean which determines if there is more data

              --------
              MUTATIONS

              Mutation hooks are used to perform CRUD operations on the server. 

              The basic structure is like this:

              * Define an api call
              * Create a useMutation hook which takes an api call as a mutateFn
              * Pass the mutation hook as a prop to the target component
              * Call it, as for example with onClick event

              ```
                // Example of the useMutationHook
                const updateMutation = useMutation({
                  mutationFn: (postId) => updatePost(postId),
                })

                //Example of the call
                <button onClick={() => updateMutation.mutate(post.id)}>
              ```

          '''
          
      )
    with st.expander("React Hook Form & ShadCN Form"):
      st.write(
        '''
          Forms are the most common way to collect the user inputs. Some of the most common 
          form fields are:

            * Input (text, password, email)
            * Date (for passing the dates)
            * Checkboxes (for boolean decisions)
            * Textarea (for comments or feedbacks)
            * Buttons

            React Hook Form is a library for managing form state and validation in React applications.
            It leverages React hooks to provide a simple and performant way to handle form inputs, validation, 
            and submission. Unlike traditional form libraries, React Hook Form focuses on minimizing re-renders and 
            optimizing performance by utilizing uncontrolled components and native HTML inputs

            React hook provides several built-in methods which can be used to perform all the neccessary 
            form operations:

          * **register Method** : Registers an input or select element and its validation rules.
          * **handleSubmit Method** : Handles form submission and validation.
          * **watch Method** : Watches specified inputs and returns their values.
          * **reset Method** : Resets the form state and input values.
          * **setValue Method** : Sets the value of an input programmatically.
          * **getValues Method** : Returns all form values.
          * **trigger Method** : Triggers validation for specified inputs
          
          (React Hook Tutorial)['https://www.youtube.com/watch?v=KejZXxFCe2k&list=PLC3y8-rFHvwjmgBr1327BA5bVXoQH-w5s']


          ---------------------------------
          Shadcn is a react component library which helps to build application faster by providing most common 
          elements, methods and others.

          ShadCN form is build on top of React Hook Form. It is easy to implement, especially in combination
          with the zod data validation library. Below is a simple example of the login form implementation. Form
          component has 3 main parts:

          * form schema provided by zod
          * useForm hook which binds schema and form together
          * handleSubmit function which gets called, when submit button is triggerd

          -----------------------------------------

          ```
          //We must define the component as a client component, since user is passing the data
          'use client'

          //Zod and useForm are crucial, other imports are associated with ShadCN
          import { useForm } from 'react-hook-form'
          import { zodResolver } from '@hookform/resolvers/zod'
          import { Button } from '@/components/ui/button'
          import {
            Card,
            CardContent,
            CardDescription,
            CardFooter,
            CardHeader,
            CardTitle,
          } from '@/components/ui/card'
          import { Input } from '@/components/ui/input'
          import { Label } from '@/components/ui/label'
          import { PersonStandingIcon } from 'lucide-react'
          import Link from 'next/link'
          import * as z from 'zod'
          import {
            Form,
            FormControl,
            FormDescription,
            FormField,
            FormItem,
            FormLabel,
            FormMessage,
          } from '@/components/ui/form'
          import { useToast } from '@/components/ui/use-toast'

          //In order to perform client side data validation, we have to create schema, which is
          // zod object

          const formSchema = z.object({
            email: z.string().email(),
            password: z.string(),
          })

          const LoginPage = () => {
            //Toaster Code
            const { toast } = useToast()

            /*Connect Zod Resolver With React
              We pass the <z.infer<typeof formSchema>> data type to form and define zod
              As as resolver. Besided we pass the default values*/


            const form = useForm<z.infer<typeof formSchema>>({
              resolver: zodResolver(formSchema),
              defaultValues: {
                email: '',
                password: '',
              },
            })

            /*
              This is handle submit function which takes data as a parameter and
              validates it agains the provided formSchema. This is just an example
              which is why submitted data are shown via toas
            */

            const handleSubmit = (data: z.infer<typeof formSchema>) => {
              console.log(data)
              toast({
                title: 'Form data pano toast',
                description: (
                  <code className="text-white">{JSON.stringify(data, null, 2)}</code>
                ),
              })
            }

            return (
              <>
                <PersonStandingIcon size={50} />
                <Card className="w-full max-w-sm">
                  <CardHeader>
                    <CardTitle>Login</CardTitle>
                    <CardDescription>Login to your supported account.</CardDescription>
                  </CardHeader>
                  <CardContent>
                    /*
                    This part is very important since form is unpacked as a property
                    of a Shadcn Form Component
                    */
                    <Form {...form}>
                      <form
                        className="flex flex-col gap-4"
                        onSubmit={form.handleSubmit(handleSubmit)}
                      >
                        <FormField
                          control={form.control}
                          name="email"
                          render={({ field }) => (
                            <FormItem>
                              <FormLabel>Email</FormLabel>
                              <FormControl>
                                <Input placeholder="john.doe@gmail.com" {...field} />
                              </FormControl>
                              <FormDescription>
                                Please enter your sign up mail.
                              </FormDescription>
                              <FormMessage />
                            </FormItem>
                          )}
                        />
                        <FormField
                          control={form.control}
                          name="password"
                          render={({ field }) => (
                            <FormItem>
                              <FormLabel>Password</FormLabel>
                              <FormControl>
                                <Input placeholder="password" {...field} />
                              </FormControl>
                              <FormMessage />
                            </FormItem>
                          )}
                        />
                        <Button type="submit">Login</Button>
                      </form>
                    </Form>
                  </CardContent>
                  <CardFooter className="justify-between">
                    <small>Dont have account</small>
                    <Button asChild variant={'outline'} size="sm">
                      <Link href="sign-up">Sign Up</Link>
                    </Button>
                  </CardFooter>
                </Card>
              </>
            )
          }
          export default LoginPage


          ```

        '''
      )

   

        
        
