***Azure-Queue-Storage-Queues***
```

User Order -> Server

User Order -> Order Queue -> Order Fulfillment Service -> Post Order Queue -> Anaytics Ingestion Service

If anything goes down, still we don't lose our new orders.

Benefits:
1. Encourages application logic modularity
2. Enables fault tolerance between modules

```

***Azure Queue Sotrage***
```
Req. Storage account
Support Message upto 64Kib in size
Messages exist winin a single queue
Number of messages limited only by size of storage account
time-to-live per message (Default at 7 days)
Data in queue by defult encrypted 
Azure storage stored access policies can work with queues 

URL structure: https://pluralsight.queue.core.windows.net/pluralsight-queue
                       storage account                    queue name
```

***CLI Commands***
```
create a queue

az storage queue create --name storagequeuesample

delete a queue

az storage queue delete --name storagequeuesample

view a message in a queue

az storage message peek --queue-name storagequeuesample

delete all messages in a queue

az storage message clear --queue-name storagequeuesample
```