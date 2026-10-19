@rem Gradle wrapper launcher (custom, uses gradle-wrapper-main + shared)
@echo off
set DIRNAME=%~dp0
if "%DIRNAME%"=="" set DIRNAME=.
set APP_HOME=%DIRNAME%
set CP=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar;%APP_HOME%\gradle\wrapper\gradle-wrapper-shared.jar
if defined JAVA_HOME (
  set JAVA_EXE=%JAVA_HOME%\bin\java.exe
) else (
  set JAVA_EXE=java.exe
)
"%JAVA_EXE%" -classpath "%CP%" org.gradle.wrapper.GradleWrapperMain %*
