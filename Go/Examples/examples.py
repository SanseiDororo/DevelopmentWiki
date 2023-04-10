import streamlit as st


def examples():
    st.header("Coding Examples")
    st.write(
        """
    
        This section offers slow introduction into the GO language by offering simple code challenges.
        The challenges are solved in GO and Python, to expose the difference between the two languages.
    
        """
    )
    st.write("")
    st.write("")
    with st.expander("Banger"):
        st.write(

            """
                In this challenge you have to take a user input from the command line and return it in
                capitals. After the word you have to put as many exclamation marks as there is characters
                in the the word.

                GO Solution

                ```
                package main

                import (
                	"fmt"
                	"strings"
                	"unicode/utf8"
                )

                func main() {
                	fmt.Println("Please enter a word")

                	var word string
                	fmt.Scanln(&word)

                	fmt.Println(strings.ToUpper(word) + strings.Repeat("!", utf8.RuneCountInString(word)))

                }           

                ```

                * Python

                ```
                insert = input("Please insert a word: ")

                print(insert.upper()+("!" * len(insert)))y
                ```

            """
        )
    
    with st.expander("Path Separator"):
        st.write(
            """
                This challenge requires you to separate different levels of a file path. For example,
                you have a folder/andfile. You will learn how to use Path package from the standard
                library and how to use multiple assignement expressions.

                GO Solution

                ```
                package main

                import (
                	"fmt"
                	"path"
                )

                func main() {
                	// Store the path to split in a variable
                	myPath := "folder/file.pdf"

                	// Call path.Split on the variable
                	var dir, file = path.Split(myPath)

                	fmt.Println("dir: ", dir)
                	fmt.Println("file: ", file)
                }

                This returns dir: folder, file: file.pdf 

                If you want to discard some values, you can use _ character like:
                _, file = path.Split ....               

                ```

                * Python

                ```
                import os

                #path
                path = 'main/page1.py'

                #os.path.split returns a list
                path_components = os.path.split(path)

                print("dir: ", path_components[0])
                print("file: ", path_components[1])

                This returns: dir: main, file: page1.py
                ```

            """
        )
    with st.expander("Greeter"):
        st.write(
            """
                Get input from the command line an printout the arguments.

                GO Solution

                ```
                package main

                import (
                	"fmt"
                	"os"
                )

                func main() {
                	fmt.Printf("%#v\n", os.Args)

                	fmt.Println("Path:", os.Args[0])
                	fmt.Println("1 arg:", os.Args[1])
                	fmt.Println("2 arg:", os.Args[2])

                	fmt.Println("Print the number of cmd arguments", len(os.Args))
                }         

                ```

                * Python

                ```
                import sys

                print(f"Name of the script      : {sys.argv[0]=}")
                print(f"Arguments of the script : {sys.argv[1:]=}")
                ```

            """
        )
    with st.expander("Read File"):
        st.write(
            r"""
                Read the content of the file and print the output in terminal

                GO Solution

                ```
                package main

                import (
                	"fmt"
                	"io/ioutil"
                	"log"
                	"os"
                )

                func main() {
                	data, err := readFile("example.txt")
                	if err != nil {
                		log.Fatal(err)
                	}
                    // defer start file closing operation in case of error
                	defer fmt.Println("Closing file...")
                	defer data.Close()

                	content, err := ioutil.ReadAll(data)
                	if err != nil {
                		log.Fatal(err)
                	}

                	fmt.Printf("Content of file:\n%s", content)
                }

                func readFile(filename string) (*os.File, error) {
                	fmt.Printf("Opening file %s...\n", filename)
                	file, err := os.Open(filename)
                	if err != nil {
                		return nil, err
                	}
                	return file, nil
                }        

                ```

                * Python

                ```
                #With is context manager in python which takes care
                #for resource handling after execution
                
                
                with open ("example.txt", r) as file:
                    content = file.read()
                    print(content)
                ```

            """
        )
    
    

   
    

     

   
