>> docker pull quay.io/fenicsproject/stable:latest

To share files between host and container: Copy files into /shared, to see them in the current directory:
>> docker run -ti -v ${pwd}:/home/fenics/shared quay.io/fenicsproject/stable

To view plots on web browser
>> docker run -ti -p 127.0.0.1:8000:8000 -v ${pwd}:/home/fenics/shared quay.io/fenicsproject/stable:latest

To start jupyter notebooks
>> docker run --name fenics-notebook -w /home/fenics -v ${pwd}:/home/fenics/shared -d -p 127.0.0.1:8888:8888 quay.io/fenicsproject/stable 'jupyter-notebook --ip=0.0.0.0'

>> docker ps 

to find container hash (say f4756481f7c4). Then

>> docker logs 3b4c7bcee5de

```
Near the bottom of the output you should see something like:

Copy/paste this URL into your browser when you connect for the first time,
to login with a token:
            http://0.0.0.0:8888/?token=b8d00059b0a71a94edd67d03d8ebecaa09d8c28eb7e7a0a9

Got to that site
```


Do it all in one command

>> docker logs `docker ps | grep fenics-notebook | awk '{print $1}'`