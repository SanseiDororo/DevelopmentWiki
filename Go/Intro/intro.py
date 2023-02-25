import streamlit as st


def intro():
    st.header("GO Encyclopedia")
    st.write("")
    st.write(
        """
            Go is a statically typed, compiled programming language designed for efficiency, 
            simplicity, and concurrency. It was created by Google and features a clean syntax, 
            garbage collection, and strong support for concurrency through goroutines and channels. 
            Go is commonly used for building scalable network and web applications, system tools, 
            and cloud infrastructure. 

            The following encyclopedia contains basic information about the data types, syntax,
            routines and small challenges coverd under the topic based subsections.  
    
        """
    )
    st.write("")

    st.write("")
    st.write("")

   
    with st.expander("Philosophical Aspects"):
        st.write(
            f"""
            Some aspects of Python are deeply meaningful from the philosophical perspective.
            This is a side effect of it's integrated polymorphism. One can always benefit from
            the meditating on this subjects repeatedly.

            * True > False => True

            The truth values in epistemology are mostly observed on the level of their intrinsic
            values rather than quantitative attributes. Logically true and false are the same
            vector with the opposite direction, as for example 1 and -1. But if we translate the
            meaning of the truth value in the social context, quantitative aspect becomes extreamly
            important as the measurement or direction of the preferred collective appreciacion.

            * bool(int(0)) => False  

            The boolean or truthful status of integer class state 0 (=>False) is deeply ontologically 
            meaningful. 0 as a confirmation of a non-existant or it's truth value can never be true. 0 as an existential predicate
            always presupposes some kind of existence. This could be observed from the additional perspective
            of probably one of the most beautiful philosophical questions ever raised:

            "Why is there something rather than nothing" (G.W. Leibniz)

            Because there is something rather than nothing even nothing is always something. 
            With other words there is no no-thing.

            * False * (100 * True) == False

            Ex falso sequitur quodlibet. Any kind of argument derived from the false assertion is false
            regardless of the logical consistency of it's logical derivation. Modern people love to consider
            their opinions as truth but the fact is that their truth regardless of complexity is just an opinion,
            since it is logically derived from an opinion or bias. 

            Science doesn't care what you believe.
        
        """
        )

    st.write("")
