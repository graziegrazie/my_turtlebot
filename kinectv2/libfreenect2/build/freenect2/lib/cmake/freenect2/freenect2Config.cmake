FIND_LIBRARY(freenect2_LIBRARY freenect2
    PATHS /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/build/freenect2/lib
    NO_DEFAULT_PATH
)
SET(freenect2_LIBRARIES ${freenect2_LIBRARY} )
FIND_PATH(freenect2_INCLUDE_DIR libfreenect2/libfreenect2.hpp
    PATHS /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/build/freenect2/include
    NO_DEFAULT_PATH
)
SET(freenect2_INCLUDE_DIRS ${freenect2_INCLUDE_DIR})
SET(freenect2_VERSION 0.2.0)
