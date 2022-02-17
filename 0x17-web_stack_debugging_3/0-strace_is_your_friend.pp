# Using puppet to send a command sed and fix bad type phpp to php

exec { 'FixingTypo':
    command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    provider => shell
}
