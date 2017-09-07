---
plugin_type: install
description: 
subparsers:
    container-check:
        help: Checks overcloud containers if they shell be updated
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
        groups:
            - title: check overcloud containers if they shell be updated
              options:
                  host-ip:
                      type: Value
                      help: 'ip of the machine that containers are running on'
                      required: False
                  host-username:
                      type: Value
                      help: 'username to ssh to the machine that containers are running on'
                      required: False
                  host-key_file:
                      type: Value
                      help: 'Private SSH key for the user <username>'
                      required: False
                  component-name:
                      type: Value
                      help: 'name of the component (cinder, neutron, nova, etc)'
                      required: True
