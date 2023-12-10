# installs flask version 2.1.0 with pip3

class flask_install {
  package { 'python3-pip':
    ensure => present,
  }

  exec { 'install_flask':
    command => 'pip3 install flask==2.1.0',
    user    => 'root',
    path    => '/usr/local/bin:/usr/bin:/bin',
    require => Package['python3-pip'],
  }
}

