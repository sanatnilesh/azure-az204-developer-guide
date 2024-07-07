***Server Side Execution Environment***

```
Stored Procedures, Triggers, and UDF's are executed within the database engine.
These are supported when using SQL API, or It must be defined in Javascirpt.
```

***Stored Procedure***
```
Executes on a Single partition, and it only has access to that partition.
Partition key must be provided with the execution request.
Supports Transaction model as all statements will be removed if it fails.
```

***Triggers***
```
Pre Triggers (Validation & Transformation)
Post Triggers (Aggregation & Change notification)
```

***User Defined Funtions***
```
Use as common logic in query condition
```

***Change Feed***
```
Notification based on insert or update on data
Deletes not direct supported, but you can use soft-delete flag(TTL)
Change will appear exactly once in change feeed
Not supported for Azure Table API
```

```
Create a Change Feed function using Function App
```
