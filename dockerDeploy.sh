## IMPORT ENVIRONNEMNT VARIABLES
set -o allexport
source ./.env
set +o allexport

## BUILD DOCKER IMAGE
#docker build -t $DOCKER_USERNAME/$DOCKER_IMAGE_NAME:$DOCKER_TAG_NAME .
docker run --name $DOCKER_CONTAINER_NAME -d -p 5000:5000 $DOCKER_USERNAME/$DOCKER_IMAGE_NAME:$DOCKER_TAG_NAME 

## RUN TESTS
python3 tests/api_response.py $URL_TEST
if [$? -eq 0]
then
    echo okay
else
    echo notOkay
fi


## PUSH IF TESTS OKAY
# docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
# docker push $DOCKER_USERNAME/$DOCKER_IMAGE_NAME:$DOCKER_TAG_NAME

## CREATE APP SERVICE PLAN 
# az appservice plan create --name $ASP_NAME --resource-group $RG_NAME --sku B1 --is-linux

