***Azure API Management***
```
Azure service to create consistent and modern API gateways for existing back-end services.
It provides secure, scalable API access for your applications.

Components.
1. API Gateway - Accepts API Calls and routes them to your backends
2. Azure Portal - The administrative interface where you set up your API program
3. Developer Portal - Web user interface for developers where they can read API documentation
```

***API Gateway Capabilites***
```
-> Accepts API calls and routes them to your backends
-> Verifies API Keys, JWT tokens, Certificates, and other credentials
-> Enforces usage quotas and rate limits
-> Caches backend responses
```

***Azure Portal Capabilites***
```
-> Define or import API schema
-> Set up policies like quotas or transformations on APIs
-> Package APIs into products
-> Manage Users
```

***Developer Portal Capabilities***
```
-> Read API documentation
-> Create an account and subscribe to get API keys
-> Try out an API via the interactive console
-> Access anlytics
```

***Versions***
```
-> Versions allow to presents greoups of realted APIs to the developers.
-> You can use versions to handle breaking changes in you API safely.
```

***Revision***
```
-> Revisions allow you to make changes to the APIs in a controlled and safe way, without disturbing your API consumers
```

***Typically versiosn are used to seprate API versiosn with breaking changes, while revisions can be used for minor and non-breaking changes to an API***

***Products & Groups***

***Protect APIS and Improve Performance with API management***
```
Policies: Collection of statement that are execute sequentially on the request or response of an API

Example:
Format conversion from XML to JSON
Restrict the amount of incoming calls
value of HTTP Header
Caches responses according to the specified cache control configuration
```