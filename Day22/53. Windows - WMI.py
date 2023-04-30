    
import wmi

# For Local Connection
c = wmi.WMI()

# For Remote Connection
#c = wmi.WMI("12.18.128.123", user = "admin", password = "pass@123")

#print(c.classes)
#print(c.Win32_Service())
#print(c.Win32_Service.methods.keys())
#print(c.Win32_Service.properties.keys())  

for s in c.Win32_Service():
    print(s.Name,"-",s.State)
