***Copy Items in Blob Storage***

***Azure CLI Copy blob***

```
az storage blob copy start 
    --source-account-name ###
    --source-accuont-key ###
    --source-container ###
    --source-blob ###
    --account-name ###
    --account-key ###
    --destination-container ###
```

***Copy container all blobs***
```
az storage blob copy start-batch
    --source-account-name ###
    --source-accuont-key ###
    --source-container ###
    --source-blob ###
    --account-name ###
    --account-key ###
    --destination-container ###
```

***AzCopy is additional way to copy blobs in Azure Blob Storage***
