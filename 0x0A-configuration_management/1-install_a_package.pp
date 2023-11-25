#!/usr/bin/pup
# Puppet manifest for installing Flask using pip3

# Install Flask using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
