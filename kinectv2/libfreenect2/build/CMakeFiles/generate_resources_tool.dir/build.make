# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/yoshi/catkin_ws/src/kinectv2/libfreenect2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/build

# Include any dependencies generated for this target.
include CMakeFiles/generate_resources_tool.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/generate_resources_tool.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/generate_resources_tool.dir/flags.make

CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o: CMakeFiles/generate_resources_tool.dir/flags.make
CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o: ../tools/generate_resources.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/yoshi/catkin_ws/src/kinectv2/libfreenect2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o -c /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/tools/generate_resources.cpp

CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/tools/generate_resources.cpp > CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.i

CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/tools/generate_resources.cpp -o CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.s

CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o.requires:

.PHONY : CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o.requires

CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o.provides: CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o.requires
	$(MAKE) -f CMakeFiles/generate_resources_tool.dir/build.make CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o.provides.build
.PHONY : CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o.provides

CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o.provides.build: CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o


# Object files for target generate_resources_tool
generate_resources_tool_OBJECTS = \
"CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o"

# External object files for target generate_resources_tool
generate_resources_tool_EXTERNAL_OBJECTS =

bin/generate_resources_tool: CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o
bin/generate_resources_tool: CMakeFiles/generate_resources_tool.dir/build.make
bin/generate_resources_tool: CMakeFiles/generate_resources_tool.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/yoshi/catkin_ws/src/kinectv2/libfreenect2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable bin/generate_resources_tool"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/generate_resources_tool.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/generate_resources_tool.dir/build: bin/generate_resources_tool

.PHONY : CMakeFiles/generate_resources_tool.dir/build

CMakeFiles/generate_resources_tool.dir/requires: CMakeFiles/generate_resources_tool.dir/tools/generate_resources.cpp.o.requires

.PHONY : CMakeFiles/generate_resources_tool.dir/requires

CMakeFiles/generate_resources_tool.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/generate_resources_tool.dir/cmake_clean.cmake
.PHONY : CMakeFiles/generate_resources_tool.dir/clean

CMakeFiles/generate_resources_tool.dir/depend:
	cd /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/yoshi/catkin_ws/src/kinectv2/libfreenect2 /home/yoshi/catkin_ws/src/kinectv2/libfreenect2 /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/build /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/build /home/yoshi/catkin_ws/src/kinectv2/libfreenect2/build/CMakeFiles/generate_resources_tool.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/generate_resources_tool.dir/depend

