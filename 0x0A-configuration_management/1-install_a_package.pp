#installing a package usgin Puppet

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
}
