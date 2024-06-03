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
          '''
          
      )
    

   

        
        
