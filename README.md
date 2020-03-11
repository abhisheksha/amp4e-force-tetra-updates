# amp4e-scripts

The TETRAForce.py python script forces an AMP for Endpoint connector to reactively restart the TETRA Definitions Update process and therefore, it lets the user of this script fetch the latest definitions at will. 
It works by stopping the AMP service, changing certain parameters in the local.xml, and forcing the update process to kick start earlier.
The usage of this script requires the following:
* Python - and the following modules must be made available - os, re, datetime, subprocess, and time.
