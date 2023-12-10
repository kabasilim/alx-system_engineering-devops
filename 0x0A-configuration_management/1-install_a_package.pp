# installs flask version 2.1.0 with pip3

class { 'python':
  ensure => 'installed',
}

package { 'python3-pip':
  ensure => 'installed',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

