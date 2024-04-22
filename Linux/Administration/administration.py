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
                
            '''
            )
    with st.expander('System Folders'):
        st.write(
            '''
               Below is the lis of linux system folder and their main purpose:

               * / root directory which is the starting point
               * /bin contains binaries that must be present for the system to but and run
               * /boot contains the kernel, boot image, initial RAM disk image. To confugure
                 the boot loader grub/grub.conf or menu.lst are used.
               * /dev this folder contains device nodes. "Everything in linux is a file"
                 This is true for the devices as well.
               * /etc contains all the system wide configuration. It contains collection of
                shell scripts as well that start each of the services at boot time. Some examples
                /etc/crontab file defines all automated jobs, etc/fstab is a table of storage devices
                and their associated mount points.
               * /home each user has his own home folder
               * /lib this containes shared libraries used by the core system programs
               * /media stores removable disks and usb drives
               * /mnt mount points for removable devises
               * /opt is used to install "optional" software 
               * /root home directory of the root user
               * /sbin contains system binaries
               * /tmp is used to store temporary transitient files
               * /usr it contains all the programms and support files used by regular users
               * /var stores the data that is likely to be change   

               
            '''
            )    
    