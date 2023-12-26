# Puppet manifest for installing and configuring Nginx
exec { 'update_ubuntu':
  command  => 'sudo apt-get update',
  provider => 'shell',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update_ubuntu'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
  subscribe => [
    File['/etc/nginx/sites-available/default'],
    File['/etc/nginx/html/index.html'],
    File['/etc/nginx/html/404.html'],
  ],
}

file { '/etc/nginx/html':
  ensure => 'directory',
}

file { '/etc/nginx/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

file { '/etc/nginx/html/404.html':
  ensure  => 'file',
  content => 'Ceci n\'est pas une page',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
    listen 80;
    listen [::]:80 default_server;
    root /etc/nginx/html;
    index index.html;
    location /redirect_me {
        return 301 https://johnombuya.pythonanywhere.com;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /etc/nginx/html;
        internal;
    }
  }",
  require => File['/etc/nginx/html'],
  notify  => Service['nginx'],
}
