# Setup client SSH using puppet
$path_conf = '/etc/ssh/ssh_config'

file { $path_conf:
  ensure => file,
}
file_line { 'Turn off passwd auth':
  path    => $path_conf,
  line    => 'PasswordAuthentication no',
  match   => '^\s*PasswordAuthentication',
  require => File[$path_conf],
}
file_line { 'Declare identity file':
  path    => $path_conf,
  line    => 'IdentityFile ~/.ssh/holberton',
  match   => '^\s*IdentityFile',
  require => File[$path_conf],
}
