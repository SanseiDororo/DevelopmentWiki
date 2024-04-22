import streamlit as st

def administration():
    st.header('Linux Administration')
    st.write("")
    st.write('''
            
        This section covers most importan aspects of Linux Administration. The content is divided into
        topics such as properties, steps, examples. Detailed explanation of each topic is 
        provided in the extensions below. 


            ''')
    
    st.write(''' ''')
    st.write(''' ''')

    with st.expander('Create & Manage Users'):
        st.write(
            '''
               Linux is the most comprehensive os. There is almost infinte list of operations for
               performing basic and advanced operations. The following section lists most common
               operation we need to know in order to be able to start using linux. Linux is multiuser 
               system. Administrator is super user. If we want to perform the operations as administrators,
               we need to use keyword SUDO

               * ADDING USERS
                
                ```
                    sudo adduser username
                ```
                -------------------------
               * SWITCHING USERS

                ```
                    #Switching user
                    su username

                    #Executing command as a different user
                    sudo -u username command
                ```
                -------------------------
               * CHANGING PASSWORDS

                ```
                    #Change password
                    passwd

                    #Change password for a different user
                    sudo passwd username
                ```
                -------------------------

                * CREATING GROUPS

                ```
                    sudo groupadd groupname
                ```
                -------------------------
                PUTTING USERS IN A GROUP

                ```
                    sudo usermod -a -G groupname username
                ```
            '''
            )

    with st.expander('Folders & Files'):
        st.write(
            '''
                * CREATE FILE
                
                ```
                    touch filename
                ```
                -------------------------
                * CREATE FOLDER
                
                ```
                    mkdir folder name
                ```
                -------------------------
                * LIST FILES & FOLDERS

                ```
                    ls -al (alias can be ll)
                ```
                -------------------------
                * CHANGE FOLDERS

                ```
                    cd foldername
                ```
                -------------------------
                * PRINT WORKING DIRECTORY

                ```
                    pwd
                ```
                -------------------------
                * VIEW CONTENT OF A FILE

                ```
                    less filename
                ```
                * COPY FILES AND FOLDERS

                ```
                    cp item... folder
                ```
                -------------------------
                * MOVE AND RENAME FILES

                ```
                    mv item_name1 item_name2
                    
                    mv file... folder
                ```
                -------------------------
                * REMOVING FILES AND FOLDERS

                ```
                    rm item

                    Available flegs:
                    * -i interactive
                    * -r --recursive
                    * -f --force
                    * -v --verbose
                ```
                -------------------------
                
            '''
            )
    with st.expander('System Folders'):
        st.write(
            '''
               Below is the lis of linux system folder and their main purpose:

               * **/root** directory which is the starting point
               * **/bin** contains binaries that must be present for the system to but and run
               * **/boot** contains the kernel, boot image, initial RAM disk image. To confugure
                 the boot loader grub/grub.conf or menu.lst are used.
               * **/dev** this folder contains device nodes. "Everything in linux is a file"
                 This is true for the devices as well.
               * **/etc** contains all the system wide configuration. It contains collection of
                shell scripts as well that start each of the services at boot time. Some examples
                /etc/crontab file defines all automated jobs, etc/fstab is a table of storage devices
                and their associated mount points.
               * **/home** each user has his own home folder
               * **/lib** this containes shared libraries used by the core system programs
               * **/media** stores removable disks and usb drives
               * **/mnt** mount points for removable devises
               * **/opt** is used to install "optional" software 
               * **/root** home directory of the root user
               * **/sbin** contains system binaries
               * **/tmp** is used to store temporary transitient files
               * **/usr** it contains all the programms and support files used by regular users
               * **/var** stores the data that is likely to be change   

               
            '''
            )    
    with st.expander('Commands'):
        st.write(
            '''
                Short list of useful commands

                
                * TYPE

                ```
                    Displays the kinf of command the shell will execute
                    
                    type command
                ```
                -------------------------
               
               * WHICH

                ```
                    Displays executable's location
                    
                    which python
                ```
                -------------------------
                
                * HELP

                ```
                    Shows the docstring of the command
                    
                    help cd
                    mkdir --help
                ```
                -------------------------
                * MAN

                ```
                    Displays program manual page
                    
                    man ls

                    Single line program manual
                    whatis ls
                ```
                -------------------------
                * ALIASES

                ```
                    Aliases are great way to create own commands vocabulary

                    alias command_name='command_to_exexute'
                ```
                -------------------------
            '''
            ) 
    
    with st.expander('Redirecting & Storing Output'):
        st.write(
            '''
                Redirecting and storing the standard output is very common and useful operation.

                
                * Store content in a file

                ```
                    command > file.txt

                    #command can be piped and stored

                    command | grep keyword > command.txt
                    history | grep git > git_commands.txt

                ```
                -------------------------
               
               
            '''
            ) 
    with st.expander('Keybord & Terminal'):
        st.write(
            '''
                In order to be able to efficiently use keyboard and terminal, the following
                shortcuts and commands can be handy.

                
                * Clear The Screen

                ```
                    clear
                    ctrl + L

                ```
                -------------------------

                * Clear The Screen

                ```
                    clear
                    ctrl + L

                ```
                -------------------------

               * Cursor Movement

                ```
                    CTRL + A = beginning of the line
                    CTRL + E = end of the line
                    CTRL + F = move 1 character
                    CTRL + B = move 1 character back
                    ALT + F  = move 1 word forward
                    ALT + B move 1 word backward
                    
                ```
                -------------------------

                * Editing commads

                ```
                    CTRL + D = delete character at the cursor location
                ```
                -------------------------

                * Cutting & Parting

                ```
                    CTRL + K = kill text from the cursor location to the end of the line
                    CTRL + U = kill the text frum the cursor location to the beginning of the line
                    CTRL + Y = Yank the text from the kill-ring and insert it at the cursor location
                    
                ```
                -------------------------
               
            '''
            ) 
    with st.expander('Permissions'):
        st.write(
            '''
                Linux is multiuser operation system, which is why permissions play cruical role
                in defining scope of the user's space

                
                * Basic commands

                ```
                id = Display user identity

                whoami = Which user is active

                chmod = Change file's mode

                umask = Set the default file permissions
                    
                su = Run a shell as another set

                sudo = Execute a command as another user.
                    
                chown = Change a file's owner
                    
                chgrp = Change a file's group ownership
                    
                passwd = Change user's password

                ```
                -------------------------

                * Permissions

                ```
                   There are three basic permissions:

                   r = read
                   w = write 
                   x = execut

                   Permisions can be defined on the level of:

                   |Owner |Group | World|

                   To change a user permission chmod command is used 

                ```
                -------------------------

                
    
            '''
            ) 