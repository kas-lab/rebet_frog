# Use the official ROS 2 Humble base image with Gazebo Fortress pre-installed
FROM osrf/ros:humble-desktop-full

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install additional dependencies if needed
RUN apt-get update 

RUN apt-get install -y \
    openssh-client \
    ros-humble-gazebo-ros-pkgs \
    ros-${ROS_DISTRO}-ros-ign \
    vim \
    nano \
    openjdk-21-jdk \
    ros-dev-tools \
    python3-colcon-common-extensions \
    python3-venv \
    wget \
    unzip \
    zip \
    python3-pip \
    xterm \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME="/usr/lib/jvm/java-21-openjdk-amd64"
ENV PATH="$JAVA_HOME/bin:$PATH"
ENV WORKSPACE="rebet_ws"

RUN pip install masced_bandits

RUN python3 -m venv venv --system-site-packages --symlinks

RUN /bin/bash -c "source venv/bin/activate && \
    pip install ultralytics transforms3d numpy==1.26.4"

RUN pip install JPype1

RUN pip install pandas

RUN gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-key 17507562824cfdcc
RUN gpg --export 17507562824cfdcc | sudo tee /etc/apt/trusted.gpg.d/vaticle.gpg > /dev/null
RUN echo "deb https://repo.typedb.com/public/public-release/deb/ubuntu trusty main" | tee /etc/apt/sources.list.d/vaticle.list > /dev/null

RUN apt-get update && apt-get install -y \
    typedb=2.28.3 \
    && rm -rf /var/lib/apt/lists/*
 
RUN pip3 install typedb-driver==2.28.0

ENV REBET_TERMINAL_PREFIX=""
# Create workspace directories
RUN mkdir -p /${WORKSPACE}/src

RUN mkdir -p /root/.ssh && ssh-keyscan github.com >> /root/.ssh/known_hosts

# Copy dependencies.repos into the container
COPY frog.rosinstall /${WORKSPACE}/

WORKDIR /${WORKSPACE}

# Use vcs to import and clone all packages
RUN --mount=type=ssh vcs import /${WORKSPACE}/src < /${WORKSPACE}/frog.rosinstall

COPY . /${WORKSPACE}/src/rebet_frog

RUN mv /${WORKSPACE}/src/rebet_frog/docker/shell_scripts/*.sh /${WORKSPACE}/.

# Initialize rosdep
RUN rosdep update && apt update


RUN /bin/bash -c "source /opt/ros/humble/setup.bash && \
    rosdep install --from-paths src --ignore-src -r -y"

RUN ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash \
    && apt update \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src -r -y \
    && sudo rm -rf /var/lib/apt/lists/"]


RUN /bin/bash -c "source /opt/ros/humble/setup.bash && \
    colcon build --symlink-install"
    
#RUN rm -rf /var/lib/apt/lists/*

# Set the default entrypoint
ENTRYPOINT ["/bin/bash"]
