# DashButtonContainer

A Dockerfile and python script that makes it easy to run an environment for listening to Amazon Dash button communications

Got the original code from : https://gist.github.com/eob/a8b5632f23e75b311df2
On that gist you'll see code that will likely not work with a newer Dash button that is now available. Below is modified code to listen to new button. 


The default code will listen for everything on the network sending the type of messages we expect from the Dash button.

Once you have the hardware address of the button(s) you care for, you can update the python code with filters for your button(s)

```python
if pkt[ARP].op == 1: #who-has (request)
  # Checking for specific hardware address of my button
  if pkt[ARP].hwsrc == 'c0:ff:ee:c0:ff:ee':
    print "You need coffee"
    print "Now you can do stuff when this button is pressed"
  else:
    print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
```

This docker image isn't hosted on Docker hub, so you'll need to build it locally. In order for this to work you'll need

* To have [docker](https://www.docker.com/products/docker) installed and running on this machine
* To run it on a machine on the same network as the dash button
* To run the container with it's network attached to the host (--network=host)

## Build Container from top level of project : 

docker build --tag "dashbuttonlistener:latest" .

## Run Container after it has been built : 

Running it in the fore ground, so its console out is seen

docker run --rm --network=host dashbuttonlistener:latest

Running it in the back ground. You'll need to tail the container to see its output

docker run --detach --network=host dashbuttonlistener:latest
