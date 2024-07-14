***How Caching Works***

```
CDN - Conent Delivery Network (Located Nearby User)
Instead of central single point of request/response server, content distributed among different geographic servers/network to benefit following points.

Globally distributed Network
Reduced asset load times
Reduced hosting bandwidth
Increase availabliyt and redundancy
DDoS attach Protection

```

***Content Types**
```
Static vs Dynamic Content
```

***Request Response Lifecycle of CND***
```

User Request -> CDN (No data orginal first time) -> Original Server

From the next request since data stored at CDN most of request handled by CDN

Caching mechnism is imporant to effectively use CDN otherwise it will impact negatively.

```

***Caching Rules***
```
- Azure CDN Standard (Verizon)
- Azure Cdn Standard (Akamai)
- Azure CDN (Microsoft) - Standard rules Engine
- Azure CDN Premium (Verizon)

Global - Only one per endpoint, Overrides cache headers
Custom - One or many rules, Extension or path override global rule
Query String - Key value pair (default: Ignore query strings) (Bypass query strings) (Cache Every unique URL)
```

***Azure Redis Cache***
```
When Caching is best option?
Repeatedly access data
Data source performance
Data contention
Physical location 
```
***Managing Lifetime in Redis Cache***
```
No Default expiration
Content Exists until it's removed
Must set TTL manually
```
***Calculation Cache Duration***
```
Rate of Change
Risk of Outdated Data
```

***Best Practices for Caching***
```
Watch out for data loss
Set Expiry times to manage content lifetime
Add jitter to spread database load
Avoid caching large objects (Divide and conquere)
Host Redis in the same region as your application
```

***Caching Patterns***
```
Cache-aside Pattern
Content Cache Pattern (Static content store at CDN)
Session Cache Pattern (Maintain application state)
Job & Message Queueing 
Distributed Transactions
```

***Configuring a Cache for Optimum Performance***
```
Estimating Cache Size (Cached objects, size of cached objects, number of cache requests, Cache Expiration)

(Redis CLI)Run of VM to Test:

Redis-benchmark -q -n 100000
```

***Retry Redic Cache to make Resilent Connection***
```
Linear Retry Policy
Exponential Retry Policy
```

***Data Encryption in Azure Redis Cache***
```
TLS 1.2
Encryption at Rest
SSL Connections Enablement for Redis Cache
```