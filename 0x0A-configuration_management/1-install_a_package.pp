# installs flask version 2.1.0 with pip3

class { 'python':
  ensure => 'installed',
}

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin',
  unless  => '/usr/bin/pip3 show Flask | grep Version | grep 2.1.0',
}
