# Use the official ROS 2 Humble base image with Gazebo Fortress pre-installed
FROM osrf/ros:humble-desktop-full

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install additional dependencies if needed
RUN apt-get update && apt-get install -y \
    ros-humble-gazebo-ros-pkgs \
    ros-${ROS_DISTRO}-ros-ign && \
    python3-vcstool \
    python3-rosdep \
    vim \
    nano \
    openjdk-21-jdk \
    ros-dev-tools \
    python3-colcon-common-extensions \
    wget \
    unzip \
    zip \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME="/usr/lib/jvm/java-21-openjdk-amd64"
ENV PATH="$JAVA_HOME/bin:$PATH"
ENV WORKSPACE="rebet_ws"

RUN pip install masced_bandits
RUN pip install ultralytics

RUN curl -s https://raw.githubusercontent.com/kas-lab/ros_typedb/92f740630ff4ba2efaab00d5ede0640b659b5600/.github/workflows/install_typedb.sh | bash

ENV REBET_TERMINAL_PREFIX=""
# Create workspace directories
RUN mkdir -p /${WORKSPACE}/src

# Copy dependencies.repos into the container
COPY frog.rosinstall /${WORKSPACE}/

WORKDIR /${WORKSPACE}

# Use vcs to import and clone all packages
RUN vcs import /${WORKSPACE}/src < /${WORKSPACE}/frog.rosinstall

COPY . /${WORKSPACE}/src/rebet_frog

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
