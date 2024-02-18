#!/usr/bin/env python

###########################################
### NZBGET POST-PROCESSING SCRIPT       ###

# Move downloaded media to a shared directory.
#

################################
### OPTIONS                  ###

# Destination directory
#
# Enable moving of TV Series Media

#MoveSeries=yes
#SeriesDir=/downloads

# Enable moving of Magazine Media
#
#MoveMagazines=yes
#MagazineDir=/downloads

### NZBGET POST-PROCESSING SCRIPT       ###
###########################################

import os
import sys
import shutil

## Exit codes used by NZBGet
POSTPROCESS_SUCCESS=93
POSTPROCESS_ERROR=94

required_options = ('NZBPP_NZBNAME', 'NZBPP_DIRECTORY', 'NZBPP_CATEGORY', 'NZBPP_TOTALSTATUS', 'NZBPO_MagazineDir')

print("[INFO] Mag move script starting.")
try:
	for optname in required_options:
		if optname not in os.environ:
			raise Exception("Option {optname[6:]} is missing in configuration file. Please chack script settings")

	nzb_name = os.environ['NZBPP_NZBNAME']
	nzb_dir = os.environ['NZBPP_DIRECTORY']
	nzb_category = os.environ['NZBPP_CATEGORY']
	nzb_status = os.environ['NZBPP_TOTALSTATUS']
	dest_dir = os.environ['NZBPO_MagazineDir']

	if nzb_category == 'Magazines' and nzb_status == 'SUCCESS':
		result = shutil.move(nzb_dir, dest_dir)
	else:
		raise Exception(f"Not characterized as a Magazine or unsuccessfully decompressed: {nzb_name}")

except Exception as e:
    print("[Error] %s" %e)
    sys.exit(POSTPROCESS_ERROR)

sys.exit(POSTPROCESS_SUCCESS)
