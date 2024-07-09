***Securing Azure Storage***
```
There are three ways to secure azure storage
1. Management Plane - (Role Based Access Control - RBAC) (Security Principal, Role Defination, Scope) (Role assignment)
2. Data Plane - (Keys, Shared access Signature, Azure AD)
3. Encryption - (Data Encryption alogrithms to be used to encrypt store data)
```

***Share Access Signature***
```
1. User delegation SAS - (User level)
2. Service SAS - (Service Level e.g. Blob Storage, File Storage)
3. Account SAS - (Get set, read, write)
```
***Example of SAS Token***
```
URL: https://sample.blob.core.windows.net/?
signedVersion: sv=2019-12-12&
signedService: ss=bfqt&
signedResourceType: srt=s&
signedPermission: sp=rwdlacupx&
signedExpiry and signedstart: se=date1& st=date2&
signedProtocol: spr=https&
signature: HMAC encryption
```
***Kinds of SAS***
```
1. AD-Hoc SAS
2. Service SAS with Stored Access Policy
```

***Stored Access Policy***
```
Reused by Multiple SAS
Defined on Resource Container
Permissions & Validatiy Period
Service Level SAS only
It can only implemented at container level
```

***Example of Stored Access Policy***
```
URL: https://sample.blob.core.windows.net/?
signedResourceType: srt=s&
Policy: si=mypolicy&
signature: HMAC encryption
```





