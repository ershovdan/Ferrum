Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c starter.cmd"
oShell.Run strArgs, 0, false