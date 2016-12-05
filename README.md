# fire,starter
A script to convert data from a csv file into JSON, and upload it to firebase.

### Installation
```
pip install requests
```
Requires Python 3

### Format
item|quantity|done
--- | --- | ---
chocolate chips|1000|yes
butter|1|no
eggs|2|no

becomes
```
{
  "chocolate chips":{
    "done":"yes",
    "quantity":1000
  },
  "butter":{
    "done":"no",
    "quantity":1
  },
  "eggs":{
    "done":"no",
    "quantity":2
  }
}
```
