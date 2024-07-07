Sample Code to Create a Virtual Machine(Windows/Linux) Using Command Line Interface(CLI) on Azure.

Step 1: If you are familiar with creating Virtual Machines using the Azure Portal, the first thing you need to do is create a resource group under which resources can reside. Here, the virtual machine is the resource.

```
az group create -- name "vm-demo-rg" --location "Canada Central-Toronto"
```

Step 2: This file includes CLI command codes for creating both Windows and Linux virtual machines.
The backslash ('\') is used for multiline commands.

**Windows**

```
az vm create \ 
  -- resource-group "vm-demo-rg" \
  -- name "vm-win-cli" \
  -- image "WindowsServer:WindowsServer:2019-Datacenter:latest" \
  -- admin-username "demo-vm-cli" \
  -- admin-password "demo-vm-cli-passcode" \
```

**Linux**

```
az vm create \ 
  -- resource-group "vm-demo-rg" \
  -- name "vm-linux-cli" \
  -- image "UbuntuLTS" \
  -- admin-username "demo-vm-cli" \
  -- authentication-type "ssh"\
  -- ssh--ssh-key-value ~/.ssh/id_rsa.pub
```

Step 3: After creating the virtual machine, you need to open a network port on the firewall to allow access using the recommended protocol.

**Windows**

```
az vm open-port\
  -- resource-group "vm-demo-rg" \
  -- name "vm-win-cli" \
  -- port "3389" 
```

**Linux**

```
az vm open-port\
  -- resource-group "vm-demo-rg" \
  -- name "vm-linux-cli" \
  -- port "22"
```

Step 4: Next, retrieve the IP address to use for RDP (Windows) or SSH (Linux) access.

```
az vm list-ip address\
  -- resource-group "vm-demo-rg" \
  -- name "vm-linux-cli" \
  -- output table
```

Step 5:<font color="red"> It's necessary to delete created resources if they were created only for training purposes. Otherwise, leaving VMs running can result in significant costs on your Azure bill. Use the following command to delete resources.</font>

```
az group delete --name "vm-demo-rg"
```