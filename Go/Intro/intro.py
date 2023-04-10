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
    with st.expander("Installation"):
        st.write(
            '''
                To install go, we need to download binary for the corresponding OS.

                [Source]('https://go.dev/dl/')

                Once the download is complete, open the downloaded file and follow the instructions 
                for installation. On Linux and macOS, you can typically install Go by extracting 
                the downloaded archive to a directory in your home directory, such as $HOME/go. 
                
                On Windows, you can use the MSI installer to install Go.
        

                After installation, add the Go binary directory to your system's 
                PATH environment variable. On Linux and macOS, you can do this by 
                adding the following line to your .bashrc or .bash_profile file:

            '''
            )

    
    with st.expander('Basic Commands'):
        st.write(
            '''
                * go help: check available commands
                * go version: check go version
                * go fmt: format go code
                * go run: run go file
                * go build: builds file, reports errors, puts executable in the folder
                * go install: compiles the program, names the exe and puts it in folder's bin 
                * go test: it looks for a test file in the package folder and executes it's functions    
            
            '''
            
        )
    
    with st.expander("Worskpace"):
        st.write(
            '''
                Go is opiniated about the way how developers should structure their code.
                The workspace is set of rules which defines how the code should be structured
                in order to be concise throughout the development comunity. 

                More about the fundations of this rules can be found [here](https://rework.withgoogle.com/print/guides/5721312655835136/).

                In Go, a workspace is a directory hierarchy that contains Go source code 
                and associated files. The workspace is the location on your file system 
                where you keep all of your Go code and where you build, install, and manage Go packages.

                A typical Go workspace contains three subdirectories:

                * **BIN**: This directory contains executable programs that you build from 
                your Go source code. When you run the go install command, Go compiles your 
                code and generates binary executable files that are stored in this directory.

                * **PKG**: This directory contains compiled Go package files (.a files) 
                that are generated when you build your Go code. These files are architecture-specific 
                and are stored in subdirectories named after the target architecture.

                * **SRC**: This directory contains your Go source code files organized in packages. 
                Each package is a directory containing one or more Go source files and a go.mod 
                file that specifies the package's dependencies.


                By convention, you should organize your workspace such that each project is 
                contained in a separate directory under the src directory. For example, if you 
                are working on a project called myproject, you would create a directory 
                src/myproject that contains your Go source code files.

                To use a Go workspace, you must set the GOPATH environment variable to 
                the path of the workspace directory. For example, if your workspace is 
                located at /home/user/go, you would set GOPATH=/home/user/go. 
                This tells the Go tools where to find your source code, compiled packages, 
                and executable files. 

                **After GO 1.13 GO modules replaced Wordkspaces**

            
            '''
            )
    with st.expander("Go Modules"):
        st.write(
            '''
                Go modules is official go's dependecies package management. It is
                It is required since go version 1.13

                * To use Go Modules in a Go project, follow these steps:

                If you're starting a new project, create a new directory outside of your GOPATH 
                and initialize a new module with the command: 
                
                ```go mod init <module-name>``` 
                
                This will create a new go.mod file in your project directory.
                
                If you're working with an existing project that's using an older version of Go, 
                update to Go 1.11 or later, and then enable Go Modules by setting the environment 
                variable GO111MODULE=on in your terminal or command prompt.
                
                * Add dependencies to your project:

                To add a new dependency, use the 
                
                ```go get command``` 
                
                followed by the name of the package you want to add. 
                
                Example:
                 
                ``` go get github.com/gin-gonic/gin. ```
                
                Once a package is added, the module will update the **go.mod** file to include 
                the new package and its version, as well as any dependencies that package may have.
                If you want to specify a specific version of a package, you can do so with the 
                @version suffix. 
                
                Example: 
                
                ```go get github.com/gin-gonic/gin@v1.6.3.```

                Use the dependencies in your code:

                After you've added the necessary dependencies to your project, 
                you can import them in your code using the normal Go import statements.
                When you build or run your project, the Go Modules system will 
                automatically download any missing dependencies and ensure that the 
                correct versions are used.
                
                * Manage your dependencies:

                To manage your dependencies, you can use the go mod command to 
                list, add, remove, and update packages and versions.
                
                Example: 
                
                * go mod list: will list all the dependencies of your project
                * go mod tidy: will remove any unused dependencies and ensure that the go.mod and 
                  go.sum files are up to date.
                
                  
                By following these steps, you can properly use Go Modules to manage 
                dependencies in your Go project.



            '''
            )
   
   