# Traditionally there are two kinds of scalling Vertical and Horizontal,  but in Azure it handles by Request Unit

***Request Unit***
```
With Cosmos DB, a Request Unit encapsulates(CPU, Memory, IOPS) many of the resources needed for the database into a single unit.
As a baseline, 1 RU = 1 kb item read operation from a Cosmos DB Container. 
```

***Managing Cosmos DB Throughput***
```
There are two options to configure throughput for azure cosmos db
    1. Provisioned 
    2. Serverless
```

***Provisioned Throughput***
```
It's recommended to use for Production environment.
Provisioned Throughput at container for predictable performance.
```

***Cosmos DB Serverless***
```
Pay only for the RU consumed and storage used
Best option for development environment 
```

