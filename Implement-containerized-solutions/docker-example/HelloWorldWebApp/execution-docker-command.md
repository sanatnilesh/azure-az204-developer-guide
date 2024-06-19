This is a sample .NET HelloWorld Web application, to build and run the application in local machine use following command.

```
dotnet build .
dotnet run --project .
```

Now, publish a local build... this is what will be copied into the container.
```
dotnet publish -c Release .
```

Time to build the image container and tag it... the build is defined in the Dockerfile
```
docker build -t helloworldwebappimage:v1 .
```

Now, run the container locally and test it out. If facing issue to check application running using curl command of container use troubleshoot commands mentioned in the next topic.
```
docker run --name helloworldwebappimage --publish 8080:80 --detach helloworldwebappimage:v1
curl http:localhost:8080
```

Important other docker command to troubleshoot.

To check logs in container
```
docker logs helloworldwebappimage(or container ID)
```

To list out all continer.
```
docker ps -a
```

To access container shell and check application.
```
docker exec -it helloworldwebappimage /bin/bash
curl http:localhost:8080
```
