***Event Types***
```
Descrete: report state changes and are actionable. (Event Grid)
Series: report a condition, time-ordered, and analyzable.(Event Hub)
User notifications: prompt user or their device for attention. (Notification Hub)
```

***Azure Event Grid***
```
-> Event-based architectures (pub/sub)
-> publishers emit and subscribers consume (Azure/Custom)
-> Support many subscribers to one publisher
-> Filter events
-> Scalable up and down
-> Pay for what you use
```

***Register Event Grid Provider***
```
az provider register --namespace Microsoft.EventGrid
az provider show --namespace Microsoft.EventGrid --query "registrationState"
```

***Event Grid Terminology***
```
Events - What happened (Smallest unit of data)
Publishers - (Where it happended)
Topics - Endpoint(Collection of related Events)
Subscriptions - Event rounting (Event Grid routes and filter events to handlers)
Handlers - Event Handling (Apps consume events) (Azure function, Event Hubs, Service Bus, Storage Queues, Webhooks)
```
***WorkFlow***
```
Create a topic
Send publisher events
Add subscriptions info with filtering 
```

***Event Hub Benefits***
```
Scalable event processing service
Good for Big Data scenarios
Can Handle Millions of events/second
Decouples sending and reciving data
Integration with Azure and non-Azure services
Capture events to Azure blob storage or data lake
```

***Scenarios***
```
Telemetry, Data Archival, Transaction Processing, Anamoly detection
```

***Components of Event Hub***
```
Namespace - Container for Event Hubs
Event producers - Send data to Event Hubs
Partitions - Bucket of messages
Cosumer groups - View of an Event Hub
Subscriber - Reads data from Event Hubs
```

***Namespace creation command CLI***
```
az eventhubs namespace create --resource-group <GROUP NAME> --location <Location>/
    --name <NAMESPACE NAME>/
    --sku Standard
```

***Event Hubs Creation***
```
az eventhubs eventhubs create --name <EVENT HUB NAME>/
    --namespace <NAMESPACE NAME>/
    --message-retention 3
    --partion-count 4
    -g <GROUP NAME>
```

***Send Events to Event Hub***
```
1. Install .NET SDK (Controls communication)
2. Obtain connection Info (Endpoint will include key)
3. Open connection (OK to cache this object)
4. Prepare data (Convert to library - size limitations apply)
5. Send data (Single or batch events - May specify a partitions)
```

***Read Events from Event Hub***
```
1. Install .NET SDK 
2. Obtain connection info
3. Open coonection (EventHubConsumerClient)
4. Retrieve Data (Connection remain open, can specify partition, offset, date, and sequence number)
5. Decode data (Event body is binary)
```

***Partitions***
```
Like a bucket for event messages 
Hold events time-ordered as they arrive
Events not deleted once read
Event Hubs decides which partition events are sent to - (Can specify partition with partion key)
Maximum 32 partitions
Create as many as expected concurrent subscribers
```

***Azure Notification Hubs Solutions(ANH)***
```
Send push notifications - app to user messages
Send to multiple platforms - ios, android, and windows
ANH provides abstraction over platform notification services

Features:
-> Cross-Platform (Front-End and back-End)
-> Multiple delivery Formats (Push to user, Push to Device, localization, Silent push)
-> Telemetry
-> Scalable

Components
1. PNS (Platform Notification Service)
2. Notification Hub
3. Namespace
```

***Sending Notifications Workflow***
```
Setup PNS - Vendor Specific (implment it for each platform) 
Setup ANH - (Create namespace and hub through portal)
Map PNS to ANH - Apply keys - Find from PNS
Register devices - Use .NET SDK - Web API backend
Send pushes - .NET SDK via web API Targeted, silet, broadcast etc
```
