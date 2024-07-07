Sample Code to Create a Virtual Machine(Windows/Linux) Using Powershell on Azure.

Step 1: Sign in to Azure Account

```
Connect-AzAccount
```
Step 2: Instead of directly providing parameter values, we can create variables and assign values to them. These variables can be used anytime in different commands for creating or configuring virtual machines.

```
$resourceGroupName = "demo-powershell-vm-win-rg"
$location = "Canada Central-Toronto"
$vmName = "vm-win-powershell"
$username = "demo-az-vm-user"
$password = ConvertTo-SecureString 'FAANG5@' -AsPlainText -Force
$windowsCredential = New-Object System.management.Automation.PSCredential($username, $password)
```

Step 3: Create a Virtual Machine

```
New-AzVM \
  -- ResourceGroupName $resourceGroupName \
  -- Name $vmName \
  -- Image 'Win2019DataCenter' \
  -- Credential $windowsCredential \
  -- OpenPorts 3389
```

Step 4: Retrieve IP Address of Virtual Machine
```
Get-AzPublicIpAddress -ResourceGroupName $resourceGroupName -Name $vmName | Select-Object IPAddress
```

Step 5:<font color="red"> It's necessary to delete created resources if they were created only for training purposes. Otherwise, leaving VMs running can result in significant costs on your Azure bill. Use the following command to delete resources.</font>

```
Remove-Az -ResourceGroupName $resourceGroupName
```