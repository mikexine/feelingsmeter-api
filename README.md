# Feelingsmeter REST API
This repository contains a Python wrapper for the trained Mallet classifier together with a REST API.
The REST API currently has 1 endpoint, which allows for classification of strings.

## Prerequisites
This library is dependent on a specific classifier (Written in Mallet), which is not included in this repository.
In the future this might be dockerized, to make it easy to redistribute.

## Usage

### POST /classify
This endpoint can be used to classify one-to-many strings of text.

```
curl -X POST --data '{"data":["I love dogs","Cats are OK"]}' http://example.com/api/classify
```
... Remember to change `example.com` into the appropriate server ip.

HTTP 200 OK:
```
{
  "count": 2,
  "data": [
    {
      "angry": "0.0473874441892395",
      "animated": "0.2423139592983776",
      "empowered": "0.1517875495879836",
      "fearful": "0.0481171828841359",
      "joy": "0.5103938640402632",
      "text": "I love dogs"
    },
    {
      "angry": "0.0784520622025175",
      "animated": "0.3149160699986181",
      "empowered": "0.1207210308067779",
      "fearful": "0.0390528624322823",
      "joy": "0.4468579745598039",
      "text": "Cats are OK"
    }
  ]
}
```

## Current deployment
The service is currently deployed using Flask + Virtualenv + Gunicorn + Supervisor.

To stop the service run:
```
sudo supervisorctl stop feelingsmeter_v1
```
To start it again:
```
sudo supervisorctl start feelingsmeter_v1
```

The app can be scaled up to handle more requests by adding more worker threads. This, among other things, can be done in the config file.
the config file is located in:
```
/etc/supervisor/conf.d/feelingsmeter_v1.conf
```


