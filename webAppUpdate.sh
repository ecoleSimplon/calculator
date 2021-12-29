## IMPORT ENVIRONNEMNT VARIABLES
set -o allexport
source ./.env
set +o allexport

function deployWebApp() {
    # CREATE ARTIFACT
    zip -r $AZURE_WEB_APP_NAME.zip .

    # DEPLOY ARTIFACT TO AZURE WEB APP
    az appservice plan create --name $ASP_NAME --resource-group $RG_NAME --sku $SKU --is-linux
    az webapp create --plan $ASP_NAME --resource-group $RG_NAME --name $AZURE_WEB_APP_NAME -r "python|3.6"
    az webapp config appsettings set --resource-group $RG_NAME --name $AZURE_WEB_APP_NAME --settings SCM_DO_BUILD_DURING_DEPLOYMENT=$SCM_DO_BUILD_DURING_DEPLOYMENT
    az webapp deployment source config-zip -g $RG_NAME -n $AZURE_WEB_APP_NAME --src $AZURE_WEB_APP_NAME.zip
    rm -fr $AZURE_WEB_APP_NAME.zip
}

function destroyWebApp() {
    az webapp delete --name $AZURE_WEB_APP_NAME --resource-group $RG_NAME
}

function main() {
    updateType=$1

    if [ $updateType == "deploy" ] ; then
        deployWebApp
    elif [ $updateType == "destroy" ] ; then
        destroyWebApp
    else 
        echo "Usage error"
        echo "Required arguments : [deploy] [destroy]"
        echo "Exemple : $0 deploy"
    fi
}

# MAIN WILL DEPLOY OR DESTROY WEB APP BASED ON PASSED ARGUMENT
main $1

