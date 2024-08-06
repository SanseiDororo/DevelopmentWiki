import streamlit as st

def zod():
    st.header('Validation with Zod')
    st.write("")
    st.write('''
            Zod is a TypeScript-first schema declaration and validation library. "Schema" broadly refers to any data type, from a simple string to a complex nested object.
            Zod is designed to be as developer-friendly as possible. The goal is to eliminate duplicative type declarations. With Zod, you declare a validator once and Zod will 
            automatically infer the static TypeScript type. It's easy to compose simpler types into complex data structures.
            ''')
    st.write(''' ''')
    st.write(''' ''')
    
    with st.expander("Usage"):
        st.write(
            '''
                In order to be able to use Zod, we need to create the appropriate schemas.

                1. On the root level of the project, we create schema folder. In the schema
                we create appropriate schema.ts file in which we create data validation schema.

                ```
                    // creating a schema for strings
                    const mySchema = z.string();
                    
                    // parsing
                    mySchema.parse("tuna"); // => "tuna"
                    mySchema.parse(12); // => throws ZodError
                ```
                ----------------------
                
                2. The basic form with zod schema validation has the following structure:

                Most common hook to work with forms is React Hook Form.

                The component which serves as form must be declared 'use client'

                * Create zod schema:

                import * as z from zod

                ```
                const loginSchema = z.object({
                    email: z.string().email(),
                    password: z.string()
                })
                ```

                * Create form

                ```
                cons form = useForm<z.infer<typeof loginSchema>>({
                    resolver = zodResolver(formSchema)
                })
                ```
            '''
            )
   

          
          
