"""
================================
00. Fetch MNE-Python sample data
================================

This script makes use of mne sample data to drive the scripts. It downloads the
sample data and stores it at mne default directory.

Replace this script with something that downloads and stores your data if needed.
"""  # noqa: E501


import mne

mne.datasets.sample.data_path(update_path=True)
