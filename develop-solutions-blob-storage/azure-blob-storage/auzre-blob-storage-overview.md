***Azure Blob Storage Overview***

```
Supported Data Format: Unstrcutred Data (Text,Log, Binary(Images/Videos, Virtual Disk))
Accessible via Rest API over HTTP/HTTPS
Options to access Rest API : Azure Portal, PowerShell, CLI, SDKs
```

```
storage account -> containers -> Blobs
https://storageaccount.blob.core.windows.net/images/photo.ping
https://storageaccount.blob.core.windows.net/images?comp=list
```

*** Create a Storage account using Azure CLI ***
```
az storage account create
    --name storage-demo-account
    --resource-group demo-resource-group
    --location "Canada Central"
    --sku Standard_RAGRS
    --kind StorageV2
```

*** Create a Storage account using Azure Powershell ***
```
New-AzStorageAccount
    --Name storage-demo-account
    --ResourceGroupName demo-resource-group
    --Location "Canada Central"
    --SkuName Standard_RAGRS
    --Kind StorageV2
```

```
Perfomance: Standard vs Premium 
```
***Blob Types***
```
1. Block Blob (images/vidoes), Append Blob (log files)
2. Page Blob (random read & write) (virtual disk)
```

***Authorize Requests to Blob Storage ***
```
Shared Key, SAS (Shared Access Signature), Azure Active Directory, Anonyms on Blob Container
```


***Storage Accounts***
```
StorageV2 account (Blob, File, Table, Queue)
    Standard (Magnetic Disk) vs Premium (SSD) (Storage V2 General Purpose(Blob Page Type), BlockBlobSotrage(Block and Append), FileStorage)
StorageV1 account (General Purpose) (Blob, File, Table, Queue) - Legacy
BlobStorage (Blob)
```

***Replication Strategy***
```
LRS - Locally Redundant Storage -  GRS - Geo-redundant stroage(GRS) - (Read Access)RA-GRS
ZRS - Zone-redundant stroage - GZRS - Geo-zone-redundant-storage(GZRS) - RA-GZRS
```

Azure SDK
***
Azure.<service-category>.<service-name> e.g. Azure.Storage.Blobs
Nuget package

BlobServiceClient ~ Storage Account
BlobContainerClient ~ Containers
BlobClient ~ Blob
***