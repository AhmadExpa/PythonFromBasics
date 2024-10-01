# >>>>>>>>>>>>>>>>>>>>>>>>>Virtual environment<<<<<<<<<<<<<<<<<<<<<<<<<
''' An environment which is same as the system interpreter but isolated from
the other environment of the system : virtual environment 
we create a virtual environment in python by installing a module called virtualenv
// pip install virtualenv 
// virtualenv {filename} you want to create in this folder or file your virtualenv runs 
to activate the virtualenv in your terminal run this command in terminal
source myprojectenv/bin/activate // for linux and mac os
'''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>pip freeze<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
''' Pip freeze command is used when we want to see the packages or modules installed in
the current version of python we are using 
we can also create a file from pip that show the all the modules with version downloaded 
in our system
pip freeze > {filename.txt}
if someone wants to download the exact same modules in their python you send this file 
to that person and run this command
pip install -r {filename.txt}
'''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Lambda Function/Method<<<<<<<<<<<<<<<<<<<<<<<<<<
''' when you want to use a function like
def func(a)
return a+50
for that purpose we use lambda 
func = lambda x : x+50
this works exactly the same as above
'''