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
