@echo off
setlocal EnableDelayedExpansion
SET /A delay= %RANDOM% %% 12
echo %delay%
timeout %delay%
start cmd.exe /k "chdir C:\Users\Dolan\Dropbox\SwagbucksAutomation\Home Desktop & Python code.pyw"


