#!/usr/bin/env python3

import instapy
from instapy.util import smart_run
from instapy.util import get_relationship_counts
from instapy.util import reload_webpage

import sys
import os
import time
import segm8

INSTAGRAM_USERNAME = 'your_account_name'
INSTAGRAM_PASSWORD = 'your_account_password'
INSTAGRAM_TRACKED_USER_NAME = 'amperkaru'
REQUEST_INTERVAL_SECONDS = 360

segm8_module = segm8.SegM8(0, 4)

subscribers_count = 0
previous_subscribers_count = 0

session = instapy.InstaPy(username=INSTAGRAM_USERNAME,password=INSTAGRAM_PASSWORD, headless_browser=True)

with smart_run(session):
	while True:
		reload_webpage(session.browser)
		subscribers_count, following_count = get_relationship_counts(session.browser,INSTAGRAM_TRACKED_USER_NAME, session.logger)
		print('Subscribers count: ', subscribers_count)
		sys.stdout.flush()

		segm8_module.display_int(subscribers_count, 0, 4, segm8.Align.RIGHT)

		if subscribers_count != previous_subscribers_count:
			if subscribers_count > previous_subscribers_count:
				os.system('mpg123 /home/pi/instagram_subscriber_counter/sound_files/Sound_05810.mp3')
			else:
				os.system('mpg123 /home/pi/instagram_subscriber_counter/sound_files/Sound_05829.mp3')

			previous_subscribers_count = subscribers_count

		time.sleep(REQUEST_INTERVAL_SECONDS)
