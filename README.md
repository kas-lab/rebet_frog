# rebet_frog
ReBeT applied a to a Turtlebot, now with TypeDB

## How to Build the Docker:
We are using private repos from the kas-lab, so there are some extra steps in building the docker.

Please use this command to build, it assumes you have git set up with ssh:

This is assuming you are in the root of the rebet_frog folder. Please use it from there, it copies the source code of this repo into the docker image.

```bash
docker build --ssh default -f docker/Dockerfile -t rebetfrog:eval1 .
```

Once it is built, you should expose xhost

```bash
xhost +
```

Then you can run it like so:
```bash
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:ro rebetfrog:eval1
````

## Usage:
There are some handy-dandy shell scripts.

./ADX opens the java-based adaptation engine and typedb_tactics, don't forget to start typedb server!

./EVAL1_gui.sh does everything.

./GZ opens gazebo classic, useful for getting measurements to be entered into typedb.