using System.Net;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", GetHostName);

app.Run();

string GetHostName()
{
    string hostName = Dns.GetHostName();
    return $"Hello World! Running on host: {hostName}";
}