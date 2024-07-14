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
```

***Configuring Authentication for Azure Key Vault***
```
1. Use Azure AD App Registration.
2. Use Managed Identity. 
    Best resource to learn about how managed Identity used to authenticate azureweb app with azure key vault.
    (https://learn.microsoft.com/en-us/azure/key-vault/general/tutorial-net-create-vault-azure-web-app)
3. Use Key Value References.
   - Move Configruation to Key Vault
   - Deploy your App Service or Azure Function
   - Create a system-assigned identity for your App
   - Give GET KV SECRETS access to the app identity 
   - Update configruation values with KV reference syntax
   - Verify your application functionality

```
***Azure Key Vault Soft-delete***
```
Allow recovery of the deleted vaults and key vault objects (keys, secrets, and certificates)

1. Soft-delete is enabled on the vault
2. A key, certificate, secret or the vault is deleted
3. It remains recoverable for 7 to 90 days
4. To permanently delete the secret, a user should perform the PURGE operation
```

***Azure Key Vault Purge Protection***
```
When Purge protection is enabled, a vault or an object in the deleted state can not be purged until the retention period has passed.
```

***Azure Key Vault Keys and Azure Storage Service Encryption***

***Azure Key Vault Certificates***
