az group create -n azure-app-web-app-rg -l canadacentral

az appservice plan create --name web-app-plan \
    --resource-group azure-app-web-app-rg \
    --sku s1 \
    --is-linux 

az webapp create --resource-group azure-app-web-app-rg \
    --plan web-app-plan \
    --name sanat-dhobi-web-app \
    --deployment-container-image-name nginx 