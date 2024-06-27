Azure Functions Bindings

* A binding is a connection to data
* Input binding provides read-access to data
* Output binding let us write to an external system
* Function can have multiple input and output bindings

Example of Input Binding Types
+ Blob storage binding - read contents of a file in Blob Storage
+ Cosmos DB binding - look up a document in a Cosmos DB database
+ Microsoft Graph binding - access OneDrive

Example of Output Binding Types
- Blob Storage Binding - Create a new file in Blob Storage
- Queue Storage Binding - Post a message to a queue
- Cosmos DB Binding - Create a new document in a database
- Many others - Event Hub, Service Bus, SendGrid, Twilio etc.
