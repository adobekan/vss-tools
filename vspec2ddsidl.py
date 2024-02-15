#!/usr/bin/env python3
#
# Copyright (c) 2022 Contributors to COVESA
#
# This program and the accompanying materials are made available under the
# terms of the Mozilla Public License 2.0 which is available at
# https://www.mozilla.org/en-US/MPL/2.0/
#
# SPDX-License-Identifier: MPL-2.0

#
# Convert vspec2idl wrapper for vspec2x
#

import sys
from vspec.vspec2x import Vspec2X
from vspec.vspec2vss_config import Vspec2VssConfig
from vspec.vssexporters.vss2ddsidl import Vss2DdsIdl

if __name__ == "__main__":
    vspec2vss_config = Vspec2VssConfig()
    vss2json = Vss2DdsIdl(vspec2vss_config)
    vspec2x = Vspec2X(vss2json, vspec2vss_config)
    vspec2x.main(sys.argv[1:])
