# YOLO3 


ho messo yolo solo nella modalità 'get'

c'è un thread in background che fa l'acquisizione dell'immagine dalla camera
e il thread principale che fa inferenza e mette a video

non sono riuscito a farglielo fare ad un terzo thread ma già cosi va bene

run on laptop camera
```
python3 thread_demo.py -s 0 -t get
```


run on remote camera
```
python3 thread_demo.py -s "rtsp://user:pw@dvrip:554/cam/realmonitor?channel=1&subtype=1" -t get
```

