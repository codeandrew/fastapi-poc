
set -x
#VERSION=$1
BUILD_NUMBER=$1
VERSION=$(date +'%y.%m.%d')-$BUILD_NUMBER
sed -i "s/APPVERSION/$VERSION/" chart/Chart.yaml
sed -i "s/APPVERSION/$VERSION/" chart/values-*.yaml

ENVIRONMENT=dev
helm template ./chart --values ./chart/values.yaml \
    --values ./chart/values-dev.yaml \
    --set app.tag=$VERSION \
    --set env.app_version=$VERSION \
    --set app.environment=$ENVIRONMENT \
    --output-dir ./helmtemplates