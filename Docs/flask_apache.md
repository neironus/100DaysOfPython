# Flask on an apache server

vhost
```
<VirtualHost *:80>
    WSGIDaemonProcess nameapp user=www-data group=www-data threads=5
       
    WSGIScriptAlias / /path/to/.wsgi
    WSGIScriptReloading On
    
    ServerName servername.com
    DocumentRoot /path/to/folder
    
    <Directory /opt/to/folder>
        WSGIProcessGroup nameapp
        WSGIApplicationGroup %{GLOBAL}
        
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

.wsgi file located in python project folder
```
    activate_this = '/path/to/env'
    with open(activate_this) as file_f:
        exec(file_.read(), dict(__file__=activate_this))
        
    import sys
    sys.path.insert(0, '/path/to/folder')
    
    from app import app as appliation  #Care folder
```
