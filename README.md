# QKD project
Project on quantum key distribution for my Computer Science bachelor degree

## Quickstart
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
`docker-scripts/start-jupyter.sh  `

### Jupyter notebooks inside containers  
When running inside a container, the output from jupyter will look like:  

`http://jupyter:8888/?token=<access token>  `

to access from outside the container, copy that link in a browser and replace 'jupyter' with 'localhost':  

`http://localhost:8888/?token=<access token>  `

**NOTE**: this will work if the server port in the container is binded to a local port; if you used a convenience script, this would be the case

