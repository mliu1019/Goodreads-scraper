export $(cat config.env | xargs) 
gitlab-runner exec shell $1 \
    --env MONGODB_DB=$MONGODB_DB \
    --env MONGODB_USER=$MONGODB_USER \
    --env MONGODB_PSWD=$MONGODB_PSWD \
    --env HEROKU_API_KEY=$HEROKU_API_KEY