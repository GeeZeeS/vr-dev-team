# vr-dev-team

# Installation:
### Docker:
###### build a docker image
```
> docker-compose build
```
###### run a docker container
###### silent (no debug)
```
> docker-compose up -d
```
###### debug mode
```
> docker-compose up
```
###### Clear/Migrate DB
```
> docker-compose exec web python manage.py create_db
```
###### Fetch Database Exchange Info
```
> docker-compose exec web python manage.py fetch
```

###### Now you can access
```
> http://127.0.0.1:5000/
```
###### If today no data was fetched from exchangeratesapi, 
###### flask will automatically fetch it by accessing the web page 