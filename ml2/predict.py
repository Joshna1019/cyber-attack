import numpy  as np
import pandas as pd
import joblib
g=joblib.load("model.h5")
f=g.feature_names_in_
f1=input("enter flow_id")
s=input("enter source_ip")
p=int(input("enter source_port"))
d=int(input("destination_port"))
b=input("destination_ip")
t=input("enter timestamp")
l=input("enter label")
s1=float(input("enter flow_bytes_per_second"))
fp=float(input("enter flow_packets_per_second"))
fwp=float(input("enter fwd_packets_per_second"))
s_data={'Flow_ID':f1,' Source_IP':s,' Source_Port':p,' Destination_IP':b,'Destination_Port':d,' Timestamp':t,'Label':l,'Flow_Bytes_per_second':s,' Flow_Packets_per_second':fp,'Fwd_Packets_per_second':fwp}
s_data=pd.DataFrame([s_data])
s_data=pd.get_dummies(s_data)
s_data=s_data.reindex(columns=f,fill_value=0)
pre=g.predict(s_data)
print(pre)
if pre==1:  
      print("cyber attack")
else:
    print("not cyber attack")
