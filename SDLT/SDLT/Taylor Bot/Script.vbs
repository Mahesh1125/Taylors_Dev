Dim objOL 
Dim objFile
Dim objPath
Dim Eml
Dim Arg
Dim Bilal
Set Arg = WScript.Arguments
Dim File
File = Arg(0)

Set objOL = CreateObject("Scripting.FileSystemObject")
Set objFile = objOL.GetFile(File)
Set Bilal = CreateObject("Outlook.Application")
Set Eml = Bilal.CreateItemFromTemplate(File)
Download(Eml)
Sub Download(objEml)
For Each Attch In objEml.Attachments
Attch.SaveAsFile objOL.GetParentFolderName(objFile)  & "\" & Attch.FileName
Next
End Sub