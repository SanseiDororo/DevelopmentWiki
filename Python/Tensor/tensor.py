import streamlit as st


def tensor():
    st.header("Machine Learning With TensorFlow")
    st.write("")
    st.write(
        """
            This section covers TensorFlow framework. It presupposes basic knowledge
            of Machine Learning and Statistics. There are several amazing resources to start with.

            * [Rules of Machine Learning by Google](https://developers.google.com/machine-learning/guides/rules-of-ml)  
    
        """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Basics"):
        st.write(
            """
                Machine Learning is useful approach in case of:

                * Challenges whith extensive list of rules
                * Constantly changing environments
                * Gathering insights from extensive collections of data
            """)
        st.write("***")

        st.write("""
                Machine learning can be used on anything as long as you can convert it
                into numbers and program it to find patterns.

                Some of the most common Deep Learning use cases:

                * Recommendation
                * Translation
                * Speech Recognition
                * Computer vision
                * Natural Language Processing

            """
        )

    with st.expander("Neural Networks"):
        st.write(
            """
                At a high level, a neural network is a type of machine learning algorithm 
                modeled after the structure and function of the human brain. It's called 
                a "neural network" because it is made up of many small processing nodes 
                that are connected together, just like neurons in the brain.
                At a more detailed level, a neural network typically consists of multiple 
                layers of interconnected nodes. Each node in a layer receives input from 
                some number of nodes in the previous layer, performs a computation on that 
                input, and passes the result on to one or more nodes in the next layer. 
                The inputs and computations performed at each node are determined by the 
                network's configuration, which is often learned from data through a process 
                called training.
                
                During training, the network is presented with many examples of the type of 
                input data it will encounter at runtime, along with the corresponding correct
                output. The network uses this training data to adjust its configuration so that 
                it can produce the correct output for a given input. This process of adjusting 
                the network's configuration is called optimization, and it typically involves 
                adjusting the network's weights and biases, which are numeric parameters that 
                control the computation performed at each node.

                Once the network has been trained, it can be used to make predictions on new, 
                unseen data. To do this, the new input data is passed through the network, 
                layer by layer, and the final output is produced by the last layer of the network.
                Because the network has been trained to produce correct outputs for a given type 
                of input, it can often make accurate predictions on new data of the same type.

                Overall, neural networks are a powerful tool for performing complex computations 
                and can be used for a wide range of applications, such as image and speech 
                recognition, natural language processing, and many others.

                Neural Network Data Flow:

                Information Input => Translation Into Numbers => Learn Representation patterns =>
                Representational Output => Output

            """
        )
    with st.expander("Tensor Creation"):
        st.write(
            '''
                Tensors are multidimensional arrays with a uniform type. There are several
                functions which allows us to create tensors. As integers in python tensors
                are immutable.

                BASIC TENSOR OBJECT:

                We can initialise tensor object with constant() or Variable().

                ```
                scalar = tf.constant(6)
                vector = tf.constant([2.0,3.0,4.5])
                ```

                tf.Variable is class that represents mutable tensor. In opposition to a
                constant tensors, we can change values in mutable tensors with the assign method.

                ```
                example = tf.Variable(1.) => example.assign(2.)
                ```

                GENERATING RANDOM TENSOR

                ```
                random_tensor = tf.random.Generator.from_seed(37)
                ```

                SHUFFLE TENSOR

                ```
                tf.random.shuffle()
                ```

                GENERATING TENSOR FROM NUMPAY ARRAY

                ```
                ones = tf.ones([3,2])
                ```
        
            '''
        )   
    with st.expander("Inspection"):
        st.write(
            '''
                Most important attributes of tensors are:

                SHAPE:

                Number of elements of each dimension of a tensor.
                ```
                tensor.shape
                ```

                RANK:

                Number of tensor dimensions
                ```
                tensor.ndim
                ```

                AXIS

                A particular dimension
                ```
                tensor[0], tensor[:,1]    
                ```            

                SIZE

                ```
                A total number of items in tensor.
                tf.size(tensor)
                ```
           
            '''
        )

    with st.expander("Indexing"):
        st.write(
            '''
                We can slice tensors in the same manner as python lists.

                ```
                list = [1,2,3,4,5]

                all_ elements = list[:]
                first_element = list[0]
                last_element = list[-1]
                first_three = list[:2]

                tensor[:dimension,:element]

                ```
                Adding new dimension to existing tensor

                ```
                3dim_tensor = 2dim_tensor[...,tf.newaxis]
                tf.expand_dims(2dim_tensor, axis=-1) 
                ```
            '''
        )

    with st.expander("Arithmetic operations"):
        st.write(
            '''
                As with n-dimensional numpy arrays we can perform vectorised arithmetic
                operations on matrices or matrices.

                We can easily add, subtract, multiply divide elements by certain number.
                We can as well multiply tensor with other tensors as long as they have 
                compatible shapes and size.

                DOT PRODUCT:

                ```
                tf.matmul
                tf.tensordot
                ```

                If we need to adjust shape of different tensors, we can use the following methods:

                ```
                tf.transpose => this method flipps tensor's axis
                tf.reshape => this method reshuffles elements in the tensor
                ```


                [Beautiful Visual Guide](http://matrixmultiplication.xyz/)

            '''
        )

    with st.expander("Changing Data Type"):
        st.write(
            '''
               In order to make execution of the operations faster, we can
               change datatype of the tesnors. For example reduce the float
               size from 32bit to 16 bit

               ```
               #Change from float_32 to flaot_16: reduced precision
               tensor_float_16 = tf.cast(tensor_float_32, dtype=tf.float16)

               ```

            '''
        )

    with st.expander("Aggregation"):
        st.write(
            '''
               Common aggregations operations

               ```
               #Finding minimum
               tf.reduce_min
               ```

               ```
               #Finding maximum
               tf.reduce_max
               ```

               ```
               #Finding positional maximum
               tf.argmax(tensor)
               tesnor[tf.argmax(tensor)]
               ```          

               ```
               #Finding mean
               tf.reduce_mean
               ```      

               ```
               #Finding sum
               tf.reduce_sum
               ```
               ```
               #Finding standard deviation
               tf.math.reduce_std(tensor)
               ```
               
               ```
               #Finding variance of a tensor
               tf.math.reduce_variance(tensor)
               ```

               ```
               #Squeezeing: i.d. removind dimensions with size one from the shape of the tensor
               tf.squeeze(tensor)

               ```

            '''
        )