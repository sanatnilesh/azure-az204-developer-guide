# Create a sql api cosmos db account

```
az cosmosdb create --name cosmosdbdemobysanat --resource-group cosmosdbexample
```

#create a sql database

```
az cosmosdb sql database create --account-name cosmosdbdemobysanat --name sampledb
```

#create a sql database container

```
az cosmosdb sql container create --resource-group cosmosdbexample --accountname cosmosdbdemobysanat --database-name sampledb --name samplecontainer --partition-key-path "id"
```