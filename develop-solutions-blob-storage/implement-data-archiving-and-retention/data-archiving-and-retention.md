***Azure Blob Storage Access Tiers ****

```
Hot - Frequently accessed data
Cool - Infrequently accessed data stored for at least 30 days
Archive - Data that can be archieved for at least 180 days

Only StorageV2 account and BlobStorage account supports access Tiers
```

***set Access Tiers in Azure .NET***
```
await blobClient.SetAccessTiersAsync(AccessTier.Cool);
```

***LifeCycle Management of Blob Storage***
```
Add Rule in Azure Portal in storage account
```

***Turn soft Delete for Blobs***
```
Keep Deleted blobs for in days - 7 days - default
```

***Snapshots and Versions***
```
Snapshots - is read only copy of blob in a specific point of time. 
Version - Track all changes on blob
```

***Leases***
```
Blob can be change or delete by acquired lease id or break lease
```

***Immutable Blob Storage***
```
Time based retention - once written blob, it can't be changed until specific days 
Legal Hold - Keep it until some years
```

