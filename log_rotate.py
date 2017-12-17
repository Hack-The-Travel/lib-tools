#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
log_rotate
~~~~~~~~~~

0. Setup list of log directories, timezone and user name (who has access to logs).
1. Put it into `/etc/cron.daily/`.
2. Make it executable.
3. Rename this script to delete .py extension.
"""
from shell import shell
from datetime import datetime, timedelta
import pytz

LOG_DIRS = [
    '/var/log/sig',
    '/var/log/sig_test',
]
TIMEZONE = 'Europe/Moscow'
USER = 'uwsgi'


def result(sh):
    """Prints shell errors."""
    errors = sh.errors()
    for error in errors:
        print('\033[1mError:\033[0m {0}'.format(error))
    if len(errors)>0:
        print '-----'


if __name__ == '__main__':
    now = datetime.now(pytz.timezone(TIMEZONE))
    archive_dt = now - timedelta(hours=1)
    oblivion_dt = now - timedelta(days=60)
    for log_dir in LOG_DIRS:
        # Remote old files
        oblivion_dir = '{log_dir}/{oblivion}'.format(
            log_dir=log_dir,
            oblivion=oblivion_dt.strftime('%Y%m%d')
        )
        sh = shell(
            'sudo -u {user} rm -rf {oblivion_dir}/'.format(
                user=USER,
                oblivion_dir=oblivion_dir
            )
        )
        result(sh)

        # Create archive directory
        archive_dir = '{log_dir}/{date}/{hour}'.format(
            log_dir=log_dir,
            date=archive_dt.strftime('%Y%m%d'),
            hour=archive_dt.strftime('%H00')
        )
        sh = shell(
            'sudo -u {user} mkdir -p {archive_dir}'.format(
                user=USER,
                archive_dir=archive_dir
            )
        )
        result(sh)

        # Archive logs
        sh = shell(
            'sudo -u {user} find {log_dir} -maxdepth 1 -name "{archive_logs}" -exec mv -t {archive_dir} {{}} +'.format(
                user=USER,
                log_dir=log_dir,
                archive_dir=archive_dir,
                archive_logs=archive_dt.strftime('%Y%m%dT%H*')
            )
        )
        result(sh)
