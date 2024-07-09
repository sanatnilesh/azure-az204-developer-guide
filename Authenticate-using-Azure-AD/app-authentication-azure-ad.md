***Authenticate using Azure AD***

***Microsoft Identity Platform***
```
The Microsoft identity platform is an authentication service, open-source libraries, and application management tools.
Authentication Serices - Azure Active Directory (Azure AD Connect, ADFS)
Open Source Libraries - MSAL, Micrsoft.Identity.Web, Open ID Connect
Applicaiton Management - Gallery & Non Gallery Apps, Single Tenant and Multi Tenant apps, Authorization, Consent, logs
```

***Modern Authentication***
```
Legacy - Basic Authentication (Username, Password) , Encryption NTLM, Kerberos
Modern - WS-* and SAML, OAuth, OpenId Connect (Access Token, ID Token, Referesh Token)
```

***Kind of App***
```
Single Page Application - Implicit Flow, PKCE
Native Application - AuthCode without secret
Web Applicaiton - AuthCode with secret
Daemon - Client Credential Flow 
Limited UI - Device Code Flow

All Application ask for Access Token to API which is validated by Azure AD
```






