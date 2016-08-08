#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Chris
@license:
@file: models.py
@time: 8/4/16 3:04 PM
"""
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    platform = models.CharField(max_length=30)
    variant = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=30, blank=True, null=True)


class Spec(models.Model):
    product = models.ForeignKey(Product)
    network_technology = models.CharField(max_length=40, blank=True, null=True)
    launch_date = models.CharField(max_length=30, blank=True, null=True)
    launch_status = models.CharField(max_length=40, blank=True, null=True)
    body_dimensions = models.CharField(max_length=50, blank=True, null=True)
    body_weight = models.CharField(max_length=30, blank=True, null=True)
    body_sim = models.CharField(max_length=200, blank=True, null=True)
    display_type = models.CharField(max_length=50, blank=True, null=True)
    display_size = models.CharField(max_length=40, blank=True, null=True)
    display_resolution = models.CharField(max_length=40, blank=True, null=True)
    display_multitouch = models.CharField(max_length=20, blank=True, null=True)
    display_protection = models.CharField(max_length=100, blank=True, null=True)
    platform_os = models.CharField(max_length=50, blank=True, null=True)
    platform_chipset = models.CharField(max_length=30, blank=True, null=True)
    platform_cpu = models.CharField(max_length=30, blank=True, null=True)
    platform_gpu = models.CharField(max_length=30, blank=True, null=True)
    memery_card_slot = models.CharField(max_length=10, blank=True, null=True)
    memery_internal = models.CharField(max_length=20, blank=True, null=True)
    camera_primary = models.CharField(max_length=100, blank=True, null=True)
    camera_features = models.CharField(max_length=200, blank=True, null=True)
    camera_video = models.CharField(max_length=100, blank=True, null=True)
    camera_secondary = models.CharField(max_length=100, blank=True, null=True)
    sound_alert_types = models.CharField(max_length=50, blank=True, null=True)
    sound_loudspeaker = models.CharField(max_length=20, blank=True, null=True)
    sound_mmjack = models.CharField(max_length=20, blank=True, null=True)
    comms_wlan = models.CharField(max_length=50, blank=True, null=True)
    comms_bluetooth = models.CharField(max_length=20, blank=True, null=True)
    comms_gps = models.CharField(max_length=30, blank=True, null=True)
    comms_radio = models.CharField(max_length=20, blank=True, null=True)
    comms_usb = models.CharField(max_length=30, blank=True, null=True)
    comms_nfc = models.CharField(max_length=30, blank=True, null=True)
    features_sensors = models.CharField(max_length=100, blank=True, null=True)
    features_messaging = models.CharField(max_length=100, blank=True, null=True)
    features_browser = models.CharField(max_length=40, blank=True, null=True)
    features_others = models.CharField(max_length=300, blank=True, null=True)
    battery_battery = models.CharField(max_length=50, blank=True, null=True)
    battery_standby = models.CharField(max_length=30, blank=True, null=True)
    battery_talktime = models.CharField(max_length=30, blank=True, null=True)
    battery_musicplay = models.CharField(max_length=30, blank=True, null=True)
    misc_colors = models.CharField(max_length=50, blank=True, null=True)
    misc_price_group = models.CharField(max_length=20, blank=True, null=True)


class BatteryTest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    hardware = models.CharField(max_length=10, blank=True, null=True)
    software = models.CharField(max_length=20, blank=True, null=True)
    edit_date = models.DateTimeField(auto_now=True)
    talk_time = models.FloatField()

