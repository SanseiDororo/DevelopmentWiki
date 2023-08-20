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

    with st.expander("Reduce"):
      st.write(
        '''
          Reduce is very powerful Javascript array method. It can replace both, filter and find respectively.
          Reduce iterates over a given array and executes provided callback function. Reduce returns single
          value which can be number, array or object.

          The structure of the reduce method is:

          array.reduce((acc)=>{},initial value)

          In our case accumulator parameter is called total, and initial value is set to a 0.

          Example:
          
          ```
          //Get total salaries

          const people = [
              { 'name' : 'Steven', 'age' : 28, 'job' : 'scientist', 'salary': 1200},
              { 'name' : 'Ana', 'age' : 35, 'job' : 'doctor', 'salary': 800},
              { 'name' : 'Lola', 'age' : 48, 'job' : 'singer', 'salary': 1400},
              { 'name' : 'Chris', 'age' : 28, 'job' : 'dancer', 'salary': 2200},
            ];

           const dailyTotal = people.reduce((total,person)=>{
                total += person.salary;
                return total;
            },0)

          ``` 
        '''
        )    
    