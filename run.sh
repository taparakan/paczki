
docker stop kakapi
docker build -t kakapi_image .
docker run --name kakapi --rm -p 9900:9900 kakapi_image