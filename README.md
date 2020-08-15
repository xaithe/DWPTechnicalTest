# DWPGeocoding
DWPGeocoding is an API written for a technical test. It returns users from https://bpdts-test-app.herokuapp.com/ in a given radius, or those listed as in London


## Prerequisites
The script has a few dependencies, all defined in _requirements.txt_.

They can be installed with:

```
pip install -r requirements.txt
```

## Endpoints


### /radius

Returns all users in a given radius. The default value is 50 miles (as per the test spec) but can be defined with ```?miles=(distance) ```

### /london

Returns all users with the listed city of London
