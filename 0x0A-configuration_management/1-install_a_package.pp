#!/usr/bin/pup
# manifist to install 2.1.0 flask with pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
