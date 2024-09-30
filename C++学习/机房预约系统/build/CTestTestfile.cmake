# CMake generated Testfile for 
# Source directory: C:/Users/Administrator/typora/my_try/C++学习/机房预约系统
# Build directory: C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
if(CTEST_CONFIGURATION_TYPE MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
  add_test(AllTestsInMain "C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/build/Debug/test_csv.exe")
  set_tests_properties(AllTestsInMain PROPERTIES  _BACKTRACE_TRIPLES "C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/CMakeLists.txt;47;add_test;C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
  add_test(AllTestsInMain "C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/build/Release/test_csv.exe")
  set_tests_properties(AllTestsInMain PROPERTIES  _BACKTRACE_TRIPLES "C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/CMakeLists.txt;47;add_test;C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
  add_test(AllTestsInMain "C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/build/MinSizeRel/test_csv.exe")
  set_tests_properties(AllTestsInMain PROPERTIES  _BACKTRACE_TRIPLES "C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/CMakeLists.txt;47;add_test;C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
  add_test(AllTestsInMain "C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/build/RelWithDebInfo/test_csv.exe")
  set_tests_properties(AllTestsInMain PROPERTIES  _BACKTRACE_TRIPLES "C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/CMakeLists.txt;47;add_test;C:/Users/Administrator/typora/my_try/C++学习/机房预约系统/CMakeLists.txt;0;")
else()
  add_test(AllTestsInMain NOT_AVAILABLE)
endif()
