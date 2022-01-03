# Manifest that kills a procces using Puppet

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
