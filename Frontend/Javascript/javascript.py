import streamlit as st

def javascript():
    st.header('Javascript')
    st.write("")
    st.write('''
            This section covers most basic aspects of the Javascript languge. It serves as a quick refresher and 
            focuses primarily on the most important topics puting deep diving aside.   

            ''')

    st.write(''' ''')
    st.write(''' ''')

    with st.expander("Destructuring"):
        st.write(
            '''
                Javascript offers several approaches to destruct arrays and objects. 

                For example we can store items from the array into new
                constant or variable.
                
                ```
                    friends = ['John', 'Mart', 'Sibile', 'Slash', 'Steven'];

                    /Full Array

                    const [John, Mart, Sibile, Slash, Steven] = friends;

                    /Specific items from the array
                    const [John, Mart, ,Steven,] = friends;    
                ```

                Destructuring objects is very similar:

                Example:
                ```
                const alien = {
                    'name':'XR11', 'age':1909, 'lenght':220, 'origin':'AlfaCentaury', 'plane':{'number':1}
                };

                const {name, age, lenght, plane:{number:'planenumber'}} = alien;
                ```


            '''
        )
    
    with st.expander("Map"):
        st.write(
            '''
              Map is the most popular and widely used Javascript array method. Map method returns a new array. It doesn't change the size
              of the original array. It uses the values from the original array.

              The basic structure of the map method is:

              cost ValueName = array.map((item) => {
                return item.value;
              })

              Example

              ```
                const people = [
            
                  { 'name' : 'Steven', 'age' : 28, 'job' : 'scientist',},
                  { 'name' : 'Ana', 'age' : 35, 'job' : 'doctor',},
                  { 'name' : 'Lola', 'age' : 48, 'job' : 'singer',},
                  { 'name' : 'Chris', 'age' : 28, 'job' : 'dancer',},
                ];
        

              const ages = people.map((person)=>{
                  return person.age;
              });
              
            ```
            ---

            If we want to return only unique values, we can achive that with the Set datatype which was introduced with ES6.
            To turn set into an aray we use [...] spread operator.

            Example:

            ```
              const uniqueAges = [...new Set(people.map((person)=>{
              return person.age;
              }))];
            ```


            '''
            )
    with st.expander("Filter & Find"):
      st.write(
        '''
          Filter method returns new array based on the provided condition but it can, in difference to the map array method,
          change the size of the array.

          Example:
          
          ```
          const people = [
            
              { 'name' : 'Steven', 'age' : 28, 'job' : 'scientist',},
              { 'name' : 'Ana', 'age' : 35, 'job' : 'doctor',},
              { 'name' : 'Lola', 'age' : 48, 'job' : 'singer',},
              { 'name' : 'Chris', 'age' : 28, 'job' : 'dancer',},
            ];
        

           const young = people.filter((person) => {
               if (person.age < 48){
                  return person;
              }
           })
   
           //Shorter version
           const young = people.filter((person) => {
               return person.age < 48;
           })


        ```
        ---

        Find method returns single instance from the array if mathing criteria is true, otherwise it returns undefined

        Example:

        ```
        const dancer = people.filter((person)=>
        person.job === 'dancer'
        );
        ```

        '''
        )

    
    with st.expander("Set"):
      st.write(
        '''
          Set is built-in Javascript object which stores a collection of unique values. Sets are
          similar to array but can only store unique values.

          We can perform various methods on a provided set.

          Creating a set:
          ```
            // Creating an empty set
            const mySet = new Set();

            // Creating a set with initial values
            const mySetWithValues = new Set([1, 2, 3]);

          ``` 
          ---
          Adding or Removing elements:
          ```
            mySet.add(2);

            mySet.delete(1); // Removes the value 1 from the set

          ```
          ---

          Checking existence:
          ```
          const mySet = new Set([1, 2, 3]);
          console.log(mySet.has(2)); // true
          ```
          ---

          Getting size:
          ```
          console.log(mySet.size);

          ```
        '''
        )    
    