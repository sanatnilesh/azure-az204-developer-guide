***Azure Monitor Strcture***
```
Insights, Visulize, Analyze, Respond, Integrate

Metrics - numberical values that describe some aspect of the system at a particular time.
Example of metrics can be cpu or memory usage.

Logs - Events that occured in the system. Example of logs can be info. about exception thrown during application execution.
```

***Azure Monitor Capabilities***
```
=> Co-relate infrastructure issues
=> Detect and diagnose issues across applications and dependancies
=> Support operations with smart alerts and automated actions
=> Create visulization with Azure dashboards and workbooks

Azure Monitor can collect log data from any REST client what allows to create custom monitoring scenarios, including on-premises solutions
```

***Azure Application Insight***
```
Web APP ---> WEB API ---> Database  |                               |----> PowerBI
               |                    |                               |----> REST API
               |                    |<------Application Insights--->|  
               |                    |                               |----> Visual Studio
            External System


Sampel - Code Resource - https://github.com/Daniel-Krzyczkowski/Pluralsight
```


***Handle Transient Fault***
```
Azure Application Insight WEB Tests
Availablity Test (is enpoint is availble?)
    - URL Pin Test
    - Custom Track Availablity Tests
    - Multi-step web test

An Action Group: group to be notified

Polly Open-source library Pattern
    - Retry
    - Timeout
    - Circuit Breaker
```
