# Feelingsmeter REST API
This repository contains a Python wrapper for the trained Mallet classifier together with a REST API.
The REST API currently has 1 endpoint, which allows for classification of strings.

## Prerequisites
This library is dependent on a specific classifier (Written in Mallet), which is not included in this repository.
In the future this might be dockerized, to make it easy to redistribute.

## Usage

### POST /classify
This endpoint can be used to classify one-to-many strings of text. Try keeping each call under 30000 data entries - otherwise you might encounter a HTTP 413 Request entity too large.
**A small note to the current output** <br>
_The output is currently composed of multiple classifications. That is, a 4-way classifier, a 27-way classifier and a positive/negative classifier._

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
      "accomplished": "6.708522850097586",
      "amused": "0.0045626658439780",
      "angry": "0.0015081536584954",
      "animated": "0.2171312901094528",
      "annoyed": "0.0034403067707441",
      "aroused_excited_angry_pissed": "0.9069036021971633",
      "awesome": "0.0068032673783330",
      "bad": "1.3831012643729604",
      "calm_tired_relaxed_sleepy": "0.0930963978028366",
      "confident": "8.17373058896177",
      "confused": "2.2296190825557967",
      "depressed": "5.193363554382204",
      "determined": "0.0154843379424245",
      "disappointed": "2.6149649685420283",
      "disgusted": "9.798025161611611",
      "down": "4.5519024031206296",
      "empowered": "0.0967755823490431",
      "excited": "0.3024631434549241",
      "fantastic": "1.3123759101179113",
      "fearful": "0.0406727382644913",
      "great": "0.0301416552726511",
      "happy": "0.2356623652938178",
      "heartbroken": "0.0020130365052385",
      "hopeful": "0.0273657676624707",
      "joy": "0.3320726169938702",
      "neg_sad_disgusted_disappointed": "0.5869567541939524",
      "pissed": "1.083402516701651",
      "pos_happy_great_wonderful": "0.4130432458060476",
      "proud": "0.0298204801299957",
      "pumped": "1.3710221217981802",
      "sad": "0.2692904024654815",
      "scared": "5.0228975655649",
      "super": "1.609438922192805",
      "text": "I love dogs",
      "wonderful": "0.0687501018393262",
      "worried": "2.2428860754512153"
    },
    {
      "accomplished": "6.072347534908887",
      "amused": "0.0035880012554734",
      "angry": "0.0038114617426785",
      "animated": "0.2345730347789068",
      "annoyed": "0.0148337821545188",
      "aroused_excited_angry_pissed": "0.9121731820568444",
      "awesome": "0.0092148493283697",
      "bad": "2.0574475664063005",
      "calm_tired_relaxed_sleepy": "0.0878268179431555",
      "confident": "2.706807912093861",
      "confused": "4.4120554835201247",
      "depressed": "6.50227039588693",
      "determined": "0.0450628692880672",
      "disappointed": "3.695681297630133",
      "disgusted": "1.6653360345160132",
      "down": "8.925390147670965",
      "empowered": "0.0972024990800085",
      "excited": "0.4816190339966227",
      "fantastic": "8.679308965418483",
      "fearful": "0.0255318228061800",
      "great": "0.0606224683832814",
      "happy": "0.1966062300211734",
      "heartbroken": "1.364420069519892",
      "hopeful": "0.0140905064678496",
      "joy": "0.3755360837168270",
      "neg_sad_disgusted_disappointed": "0.6478717759254994",
      "pissed": "0.0010773032674606",
      "pos_happy_great_wonderful": "0.3521282240745007",
      "proud": "0.0107433121823647",
      "pumped": "1.0325486359021687",
      "sad": "0.0976760282151627",
      "scared": "3.1064692401994626",
      "super": "1.963971884042896",
      "text": "Cats are OK",
      "wonderful": "0.0588311258816230",
      "worried": "3.6510633896586983"
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


