# 2-puppet_custom_http_response_header.pp

# Install Nginx
class { 'nginx':
  ensure => 'installed',
}

# Define a custom fact to get the hostname
Facter.add('custom_hostname') do
  setcode 'hostname'
end

# Configure Nginx to add X-Served-By header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80;
        server_name _;

        location / {
            add_header X-Served-By $custom_hostname;
            try_files \$uri \$uri/ =404;
        }
    }
  ",
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx service after making changes
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => File['/etc/nginx/sites-available/default'],
}
