import subprocess
#subprocess.call(["powershell.exe", "D:\Python\getserverinfo.ps1"])

#p = subprocess.Popen(["powershell.exe", "D:\Python\getserverinfo.ps1"])
#p.communicate()

#subprocess.Popen('echo "Arockia"', shell=True)
#subprocess.run('echo "Arockia"', shell=True)

subprocess.call(["powershell.exe", "(get-service).Name"])