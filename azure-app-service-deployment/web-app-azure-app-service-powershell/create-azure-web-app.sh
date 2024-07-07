$rgname = 'az-app-service-ps-rg'
$location = 'candacentral'
$webappplan = 'az-web-app-plan'
$webappname = 'az-web-app'

#Create a resource group
New-AzResourceGroup -Name $rgname -Location $location

#Create an App Service plan in S1 tier
New-AzAppServicePlan -Name $webappplan -Location $location -ResourceGroupName $rgname -Tier S1

#Create a web app
New-AzWebApp -Name $webappname -Location $location -AppSericePlan $webappplan -ResourceGroupName $rgname