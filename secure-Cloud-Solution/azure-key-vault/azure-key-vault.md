***Key-Vault***
```
Azure Key Vault is an Azure service which allows you to securely store and access secrets.

Three Types:
1. Keys: Cryptographic Keys used in other Azure services such as Azure Disk Encryption.
2. Secrets: Any sensitive information including connection strings or passwords.
3. Certificates: x509 certificates used in HTTPS/SSL/TLS communications(encryptions in transit)
```

***Powershell Command to Provision Azure Key Vault***
```
New-AzKeyVault -VaultName 'AZ204-Vault' -ResourceGroupName 'rg-204' -Location 'East US'
```AzureA

***Configuring Authentication for Azure Key Vault***
```
1. Use Azure AD App Registration.
2. Use Managed Identity.
3. Use Key Value References.
```

