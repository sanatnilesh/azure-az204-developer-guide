From mcr.microsoft.com/dotnet/aspnet:8.0

RUN mkdir /app
WORKDIR /app

COPY ./bin/Release/net8.0/publish ./

#COPY ./config.sh ./ /app/
#RUN bash config.sh

EXPOSE 80
ENTRYPOINT [ "dotnet", "HelloWorldWebApp.dll" ]