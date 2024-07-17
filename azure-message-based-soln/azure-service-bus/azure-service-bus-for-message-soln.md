***Azure Service Bus***
```
Fully-managed enterprise message broker service that enables multiple modes of messaging with integration of common messaging systems including JMS (Java Message Service)

Supports Both HTTPS/HTTP & AMQP Protocols
Includes messaging for both queues and topics
Supports three different performance tiers: basic, standard, peremium

Supports Advanced configurablity: 
Ordering - (FIFO ordering - must be enable on queue or topic before it use)
Batching
DLQ
Duplicate deletion
```

***Oragnization of Azure Service Bus***
```
Namespace (Queue, Topic)

Producer -> Queue -> Consumer
Publisher -> Topic -> Subscriber
```

***Dead-letter Queue(DLQ)***
```
Azure Service Bus supports a DLQ for a queue or topic. This enables you to capture messages that were not processes during their lifetime, and act accordingly with those messages.
```

***Interacting with Service Bus Queues using the CLI***
```
Create a queue
az servicebus queue create --namespace-name testspace --name testqueue --resource-group test-rg

delete a queeu
az servicebus queue delete --namespace-name testspace --name testqueue
```

***Utlizing a Message-based Architecture***
```                                                                      |--- Expedited Shipping Handler   
User Order -> Order Queue -> Order FulFillment Service -> Order Topic ---|--- Standard Shipping Handler
                                                                         |--- Analytics & Financial Reports
```

***Azrue Service Bus Topics***
```
-> Enables a one-to-many relationship between messages and consumers
-> A Consumer creates a subscription to a topic
-> Subscriptions act as dedicated queues for a subscriber with configuration options
-> Topic filters can be specified as: Boolean filter, SQL Filter
```

***Azure CLI Command***
```

Create a topic

az servicebus topic create --namespace-name testnamespace --name testtopic --resource-group testresourcegroup

Delete a topic

az servicebus topic delete --namespace-name testnamespace --name testtopic

Create a Subscription

az servicebus topic subscription create --namespace-name testnamespace --name testsubscription --topic-name testtopic

```