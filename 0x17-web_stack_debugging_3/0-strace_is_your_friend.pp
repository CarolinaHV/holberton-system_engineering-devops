# find out why Apache is returning a 500 error.
exec { 'sed -i s@.phpp @.php @ /var/www/html/wp-settings.ph':
  command => 'sed  -i "s@.phpp@.php@" /var/www/html/wp-settings.php',
  path    => ['/bin','/sbin','usr/bin','usr/sbin'],
}