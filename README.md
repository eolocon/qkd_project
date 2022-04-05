# QKD project
Project on quantum key distribution for my Computer Science bachelor degree

## Quickstart (local installation)
(assuming commands are executed from the project root directory)

install the required packages:

`pip install -r requirements.txt`

then run what you neet to; example:

`jupyter notebook ./notebooks/<notebook to run>`

**NOTE**: the code is tested with python 3.9  
**TIP**: if you need to install a specific python version  
and you don't want to take the chance of breaking your system installation,  
try using **pyenv** (https://github.com/pyenv/pyenv)  
**TIP**: it's a good practice to use a virtual environment to install  
python packages for a specific use (for example, a new project);     
this way differents virtual environment are indepentent from each other;  
try using the pyenv plug-in for virtual environment management, **pyenv-virtualenv** (https://github.com/pyenv/pyenv-virtualenv)  

## Quickstart (using Docker)
(assuming commands are executed from the project root directory)

### Building the image

`docker build -t <image_name> .  `

example:  
`docker build -t qkd-project .  `

### Setting execute permission to convenience scripts  

`chmod u+x docker-scripts/*  `

### Running containers using convenience scripts  

`docker-scripts/<script-name>  `

example:    
`docker-scripts/start-jupyter.sh <image_name>  `

### Jupyter notebooks inside containers  
When running inside a container, the output from jupyter will look like:  

`To access the notebook, open this file in a browser:   
        file:///root/.local/share/jupyter/runtime/nbserver-1-open.html    
    Or copy and paste one of these URLs:    
        http://jupyter:8888/?token=d8315e57f7a6f343015a77dfb7758913913c7a7978a7d554    
     or http://127.0.0.1:8888/?token=d8315e57f7a6f343015a77dfb7758913913c7a7978a7d554    
`

to access from outside the container, copy the link starting with `http://127.0.0.1:8888` in a browser.   

**NOTE**: this will work if the server port in the container is binded to a local port; if you used a convenience script, this would be the case

