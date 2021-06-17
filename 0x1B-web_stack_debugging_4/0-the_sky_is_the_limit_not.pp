# testing how well our web server setup featuring Nginx is doing under pressure
# and it turns out it’s not doing well: we are getting a huge amount of failed requests
exec { 'limit':
    command => "sed -i 's/15/4000/g' /etc/default/nginx; service nginx restart",
    path    =>['/bin', '/usr/bin', '/usr/sbin']

}