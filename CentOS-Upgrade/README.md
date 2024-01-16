# CentosStreamupgrade

Centos doesnt support in-place upgrades, so i made my ownv

ansible-playbook upgrade_playbook.yml --extra-vars "target_host=your_target_host"

# Directadmin

Only works with php 8.1 and up


cd /usr/local/directadmin/custombuild

./build update

./build all d

# Warning

Quite unstable and very janky. Not to be used in a production enviroment

Sucky sucky

leaves a lot of old centos 8 packages

https://groups.google.com/g/ansible-project/c/LFQPk-8OU1Q 


# To DO

Vars

Logs 
