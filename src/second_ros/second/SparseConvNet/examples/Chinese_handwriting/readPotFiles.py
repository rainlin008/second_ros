# Copyright 2016-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import os
import sys
import array
import pickle
import torch
c3755 = [
    0xa1b0, 0xa2b0, 0xa3b0, 0xa4b0, 0xa5b0, 0xa6b0, 0xa7b0, 0xa8b0, 0xa9b0,
    0xaab0, 0xabb0, 0xacb0, 0xadb0, 0xaeb0, 0xafb0, 0xb0b0, 0xb1b0, 0xb2b0,
    0xb3b0, 0xb4b0, 0xb5b0, 0xb6b0, 0xb7b0, 0xb8b0, 0xb9b0, 0xbab0, 0xbbb0,
    0xbcb0, 0xbdb0, 0xbeb0, 0xbfb0, 0xc0b0, 0xc1b0, 0xc2b0, 0xc3b0, 0xc4b0,
    0xc5b0, 0xc6b0, 0xc7b0, 0xc8b0, 0xc9b0, 0xcab0, 0xcbb0, 0xccb0, 0xcdb0,
    0xceb0, 0xcfb0, 0xd0b0, 0xd1b0, 0xd2b0, 0xd3b0, 0xd4b0, 0xd5b0, 0xd6b0,
    0xd7b0, 0xd8b0, 0xd9b0, 0xdab0, 0xdbb0, 0xdcb0, 0xddb0, 0xdeb0, 0xdfb0,
    0xe0b0, 0xe1b0, 0xe2b0, 0xe3b0, 0xe4b0, 0xe5b0, 0xe6b0, 0xe7b0, 0xe8b0,
    0xe9b0, 0xeab0, 0xebb0, 0xecb0, 0xedb0, 0xeeb0, 0xefb0, 0xf0b0, 0xf1b0,
    0xf2b0, 0xf3b0, 0xf4b0, 0xf5b0, 0xf6b0, 0xf7b0, 0xf8b0, 0xf9b0, 0xfab0,
    0xfbb0, 0xfcb0, 0xfdb0, 0xfeb0, 0xa1b1, 0xa2b1, 0xa3b1, 0xa4b1, 0xa5b1,
    0xa6b1, 0xa7b1, 0xa8b1, 0xa9b1, 0xaab1, 0xabb1, 0xacb1, 0xadb1, 0xaeb1,
    0xafb1, 0xb0b1, 0xb1b1, 0xb2b1, 0xb3b1, 0xb4b1, 0xb5b1, 0xb6b1, 0xb7b1,
    0xb8b1, 0xb9b1, 0xbab1, 0xbbb1, 0xbcb1, 0xbdb1, 0xbeb1, 0xbfb1, 0xc0b1,
    0xc1b1, 0xc2b1, 0xc3b1, 0xc4b1, 0xc5b1, 0xc6b1, 0xc7b1, 0xc8b1, 0xc9b1,
    0xcab1, 0xcbb1, 0xccb1, 0xcdb1, 0xceb1, 0xcfb1, 0xd0b1, 0xd1b1, 0xd2b1,
    0xd3b1, 0xd4b1, 0xd5b1, 0xd6b1, 0xd7b1, 0xd8b1, 0xd9b1, 0xdab1, 0xdbb1,
    0xdcb1, 0xddb1, 0xdeb1, 0xdfb1, 0xe0b1, 0xe1b1, 0xe2b1, 0xe3b1, 0xe4b1,
    0xe5b1, 0xe6b1, 0xe7b1, 0xe8b1, 0xe9b1, 0xeab1, 0xebb1, 0xecb1, 0xedb1,
    0xeeb1, 0xefb1, 0xf0b1, 0xf1b1, 0xf2b1, 0xf3b1, 0xf4b1, 0xf5b1, 0xf6b1,
    0xf7b1, 0xf8b1, 0xf9b1, 0xfab1, 0xfbb1, 0xfcb1, 0xfdb1, 0xfeb1, 0xa1b2,
    0xa2b2, 0xa3b2, 0xa4b2, 0xa5b2, 0xa6b2, 0xa7b2, 0xa8b2, 0xa9b2, 0xaab2,
    0xabb2, 0xacb2, 0xadb2, 0xaeb2, 0xafb2, 0xb0b2, 0xb1b2, 0xb2b2, 0xb3b2,
    0xb4b2, 0xb5b2, 0xb6b2, 0xb7b2, 0xb8b2, 0xb9b2, 0xbab2, 0xbbb2, 0xbcb2,
    0xbdb2, 0xbeb2, 0xbfb2, 0xc0b2, 0xc1b2, 0xc2b2, 0xc3b2, 0xc4b2, 0xc5b2,
    0xc6b2, 0xc7b2, 0xc8b2, 0xc9b2, 0xcab2, 0xcbb2, 0xccb2, 0xcdb2, 0xceb2,
    0xcfb2, 0xd0b2, 0xd1b2, 0xd2b2, 0xd3b2, 0xd4b2, 0xd5b2, 0xd6b2, 0xd7b2,
    0xd8b2, 0xd9b2, 0xdab2, 0xdbb2, 0xdcb2, 0xddb2, 0xdeb2, 0xdfb2, 0xe0b2,
    0xe1b2, 0xe2b2, 0xe3b2, 0xe4b2, 0xe5b2, 0xe6b2, 0xe7b2, 0xe8b2, 0xe9b2,
    0xeab2, 0xebb2, 0xecb2, 0xedb2, 0xeeb2, 0xefb2, 0xf0b2, 0xf1b2, 0xf2b2,
    0xf3b2, 0xf4b2, 0xf5b2, 0xf6b2, 0xf7b2, 0xf8b2, 0xf9b2, 0xfab2, 0xfbb2,
    0xfcb2, 0xfdb2, 0xfeb2, 0xa1b3, 0xa2b3, 0xa3b3, 0xa4b3, 0xa5b3, 0xa6b3,
    0xa7b3, 0xa8b3, 0xa9b3, 0xaab3, 0xabb3, 0xacb3, 0xadb3, 0xaeb3, 0xafb3,
    0xb0b3, 0xb1b3, 0xb2b3, 0xb3b3, 0xb4b3, 0xb5b3, 0xb6b3, 0xb7b3, 0xb8b3,
    0xb9b3, 0xbab3, 0xbbb3, 0xbcb3, 0xbdb3, 0xbeb3, 0xbfb3, 0xc0b3, 0xc1b3,
    0xc2b3, 0xc3b3, 0xc4b3, 0xc5b3, 0xc6b3, 0xc7b3, 0xc8b3, 0xc9b3, 0xcab3,
    0xcbb3, 0xccb3, 0xcdb3, 0xceb3, 0xcfb3, 0xd0b3, 0xd1b3, 0xd2b3, 0xd3b3,
    0xd4b3, 0xd5b3, 0xd6b3, 0xd7b3, 0xd8b3, 0xd9b3, 0xdab3, 0xdbb3, 0xdcb3,
    0xddb3, 0xdeb3, 0xdfb3, 0xe0b3, 0xe1b3, 0xe2b3, 0xe3b3, 0xe4b3, 0xe5b3,
    0xe6b3, 0xe7b3, 0xe8b3, 0xe9b3, 0xeab3, 0xebb3, 0xecb3, 0xedb3, 0xeeb3,
    0xefb3, 0xf0b3, 0xf1b3, 0xf2b3, 0xf3b3, 0xf4b3, 0xf5b3, 0xf6b3, 0xf7b3,
    0xf8b3, 0xf9b3, 0xfab3, 0xfbb3, 0xfcb3, 0xfdb3, 0xfeb3, 0xa1b4, 0xa2b4,
    0xa3b4, 0xa4b4, 0xa5b4, 0xa6b4, 0xa7b4, 0xa8b4, 0xa9b4, 0xaab4, 0xabb4,
    0xacb4, 0xadb4, 0xaeb4, 0xafb4, 0xb0b4, 0xb1b4, 0xb2b4, 0xb3b4, 0xb4b4,
    0xb5b4, 0xb6b4, 0xb7b4, 0xb8b4, 0xb9b4, 0xbab4, 0xbbb4, 0xbcb4, 0xbdb4,
    0xbeb4, 0xbfb4, 0xc0b4, 0xc1b4, 0xc2b4, 0xc3b4, 0xc4b4, 0xc5b4, 0xc6b4,
    0xc7b4, 0xc8b4, 0xc9b4, 0xcab4, 0xcbb4, 0xccb4, 0xcdb4, 0xceb4, 0xcfb4,
    0xd0b4, 0xd1b4, 0xd2b4, 0xd3b4, 0xd4b4, 0xd5b4, 0xd6b4, 0xd7b4, 0xd8b4,
    0xd9b4, 0xdab4, 0xdbb4, 0xdcb4, 0xddb4, 0xdeb4, 0xdfb4, 0xe0b4, 0xe1b4,
    0xe2b4, 0xe3b4, 0xe4b4, 0xe5b4, 0xe6b4, 0xe7b4, 0xe8b4, 0xe9b4, 0xeab4,
    0xebb4, 0xecb4, 0xedb4, 0xeeb4, 0xefb4, 0xf0b4, 0xf1b4, 0xf2b4, 0xf3b4,
    0xf4b4, 0xf5b4, 0xf6b4, 0xf7b4, 0xf8b4, 0xf9b4, 0xfab4, 0xfbb4, 0xfcb4,
    0xfdb4, 0xfeb4, 0xa1b5, 0xa2b5, 0xa3b5, 0xa4b5, 0xa5b5, 0xa6b5, 0xa7b5,
    0xa8b5, 0xa9b5, 0xaab5, 0xabb5, 0xacb5, 0xadb5, 0xaeb5, 0xafb5, 0xb0b5,
    0xb1b5, 0xb2b5, 0xb3b5, 0xb4b5, 0xb5b5, 0xb6b5, 0xb7b5, 0xb8b5, 0xb9b5,
    0xbab5, 0xbbb5, 0xbcb5, 0xbdb5, 0xbeb5, 0xbfb5, 0xc0b5, 0xc1b5, 0xc2b5,
    0xc3b5, 0xc4b5, 0xc5b5, 0xc6b5, 0xc7b5, 0xc8b5, 0xc9b5, 0xcab5, 0xcbb5,
    0xccb5, 0xcdb5, 0xceb5, 0xcfb5, 0xd0b5, 0xd1b5, 0xd2b5, 0xd3b5, 0xd4b5,
    0xd5b5, 0xd6b5, 0xd7b5, 0xd8b5, 0xd9b5, 0xdab5, 0xdbb5, 0xdcb5, 0xddb5,
    0xdeb5, 0xdfb5, 0xe0b5, 0xe1b5, 0xe2b5, 0xe3b5, 0xe4b5, 0xe5b5, 0xe6b5,
    0xe7b5, 0xe8b5, 0xe9b5, 0xeab5, 0xebb5, 0xecb5, 0xedb5, 0xeeb5, 0xefb5,
    0xf0b5, 0xf1b5, 0xf2b5, 0xf3b5, 0xf4b5, 0xf5b5, 0xf6b5, 0xf7b5, 0xf8b5,
    0xf9b5, 0xfab5, 0xfbb5, 0xfcb5, 0xfdb5, 0xfeb5, 0xa1b6, 0xa2b6, 0xa3b6,
    0xa4b6, 0xa5b6, 0xa6b6, 0xa7b6, 0xa8b6, 0xa9b6, 0xaab6, 0xabb6, 0xacb6,
    0xadb6, 0xaeb6, 0xafb6, 0xb0b6, 0xb1b6, 0xb2b6, 0xb3b6, 0xb4b6, 0xb5b6,
    0xb6b6, 0xb7b6, 0xb8b6, 0xb9b6, 0xbab6, 0xbbb6, 0xbcb6, 0xbdb6, 0xbeb6,
    0xbfb6, 0xc0b6, 0xc1b6, 0xc2b6, 0xc3b6, 0xc4b6, 0xc5b6, 0xc6b6, 0xc7b6,
    0xc8b6, 0xc9b6, 0xcab6, 0xcbb6, 0xccb6, 0xcdb6, 0xceb6, 0xcfb6, 0xd0b6,
    0xd1b6, 0xd2b6, 0xd3b6, 0xd4b6, 0xd5b6, 0xd6b6, 0xd7b6, 0xd8b6, 0xd9b6,
    0xdab6, 0xdbb6, 0xdcb6, 0xddb6, 0xdeb6, 0xdfb6, 0xe0b6, 0xe1b6, 0xe2b6,
    0xe3b6, 0xe4b6, 0xe5b6, 0xe6b6, 0xe7b6, 0xe8b6, 0xe9b6, 0xeab6, 0xebb6,
    0xecb6, 0xedb6, 0xeeb6, 0xefb6, 0xf0b6, 0xf1b6, 0xf2b6, 0xf3b6, 0xf4b6,
    0xf5b6, 0xf6b6, 0xf7b6, 0xf8b6, 0xf9b6, 0xfab6, 0xfbb6, 0xfcb6, 0xfdb6,
    0xfeb6, 0xa1b7, 0xa2b7, 0xa3b7, 0xa4b7, 0xa5b7, 0xa6b7, 0xa7b7, 0xa8b7,
    0xa9b7, 0xaab7, 0xabb7, 0xacb7, 0xadb7, 0xaeb7, 0xafb7, 0xb0b7, 0xb1b7,
    0xb2b7, 0xb3b7, 0xb4b7, 0xb5b7, 0xb6b7, 0xb7b7, 0xb8b7, 0xb9b7, 0xbab7,
    0xbbb7, 0xbcb7, 0xbdb7, 0xbeb7, 0xbfb7, 0xc0b7, 0xc1b7, 0xc2b7, 0xc3b7,
    0xc4b7, 0xc5b7, 0xc6b7, 0xc7b7, 0xc8b7, 0xc9b7, 0xcab7, 0xcbb7, 0xccb7,
    0xcdb7, 0xceb7, 0xcfb7, 0xd0b7, 0xd1b7, 0xd2b7, 0xd3b7, 0xd4b7, 0xd5b7,
    0xd6b7, 0xd7b7, 0xd8b7, 0xd9b7, 0xdab7, 0xdbb7, 0xdcb7, 0xddb7, 0xdeb7,
    0xdfb7, 0xe0b7, 0xe1b7, 0xe2b7, 0xe3b7, 0xe4b7, 0xe5b7, 0xe6b7, 0xe7b7,
    0xe8b7, 0xe9b7, 0xeab7, 0xebb7, 0xecb7, 0xedb7, 0xeeb7, 0xefb7, 0xf0b7,
    0xf1b7, 0xf2b7, 0xf3b7, 0xf4b7, 0xf5b7, 0xf6b7, 0xf7b7, 0xf8b7, 0xf9b7,
    0xfab7, 0xfbb7, 0xfcb7, 0xfdb7, 0xfeb7, 0xa1b8, 0xa2b8, 0xa3b8, 0xa4b8,
    0xa5b8, 0xa6b8, 0xa7b8, 0xa8b8, 0xa9b8, 0xaab8, 0xabb8, 0xacb8, 0xadb8,
    0xaeb8, 0xafb8, 0xb0b8, 0xb1b8, 0xb2b8, 0xb3b8, 0xb4b8, 0xb5b8, 0xb6b8,
    0xb7b8, 0xb8b8, 0xb9b8, 0xbab8, 0xbbb8, 0xbcb8, 0xbdb8, 0xbeb8, 0xbfb8,
    0xc0b8, 0xc1b8, 0xc2b8, 0xc3b8, 0xc4b8, 0xc5b8, 0xc6b8, 0xc7b8, 0xc8b8,
    0xc9b8, 0xcab8, 0xcbb8, 0xccb8, 0xcdb8, 0xceb8, 0xcfb8, 0xd0b8, 0xd1b8,
    0xd2b8, 0xd3b8, 0xd4b8, 0xd5b8, 0xd6b8, 0xd7b8, 0xd8b8, 0xd9b8, 0xdab8,
    0xdbb8, 0xdcb8, 0xddb8, 0xdeb8, 0xdfb8, 0xe0b8, 0xe1b8, 0xe2b8, 0xe3b8,
    0xe4b8, 0xe5b8, 0xe6b8, 0xe7b8, 0xe8b8, 0xe9b8, 0xeab8, 0xebb8, 0xecb8,
    0xedb8, 0xeeb8, 0xefb8, 0xf0b8, 0xf1b8, 0xf2b8, 0xf3b8, 0xf4b8, 0xf5b8,
    0xf6b8, 0xf7b8, 0xf8b8, 0xf9b8, 0xfab8, 0xfbb8, 0xfcb8, 0xfdb8, 0xfeb8,
    0xa1b9, 0xa2b9, 0xa3b9, 0xa4b9, 0xa5b9, 0xa6b9, 0xa7b9, 0xa8b9, 0xa9b9,
    0xaab9, 0xabb9, 0xacb9, 0xadb9, 0xaeb9, 0xafb9, 0xb0b9, 0xb1b9, 0xb2b9,
    0xb3b9, 0xb4b9, 0xb5b9, 0xb6b9, 0xb7b9, 0xb8b9, 0xb9b9, 0xbab9, 0xbbb9,
    0xbcb9, 0xbdb9, 0xbeb9, 0xbfb9, 0xc0b9, 0xc1b9, 0xc2b9, 0xc3b9, 0xc4b9,
    0xc5b9, 0xc6b9, 0xc7b9, 0xc8b9, 0xc9b9, 0xcab9, 0xcbb9, 0xccb9, 0xcdb9,
    0xceb9, 0xcfb9, 0xd0b9, 0xd1b9, 0xd2b9, 0xd3b9, 0xd4b9, 0xd5b9, 0xd6b9,
    0xd7b9, 0xd8b9, 0xd9b9, 0xdab9, 0xdbb9, 0xdcb9, 0xddb9, 0xdeb9, 0xdfb9,
    0xe0b9, 0xe1b9, 0xe2b9, 0xe3b9, 0xe4b9, 0xe5b9, 0xe6b9, 0xe7b9, 0xe8b9,
    0xe9b9, 0xeab9, 0xebb9, 0xecb9, 0xedb9, 0xeeb9, 0xefb9, 0xf0b9, 0xf1b9,
    0xf2b9, 0xf3b9, 0xf4b9, 0xf5b9, 0xf6b9, 0xf7b9, 0xf8b9, 0xf9b9, 0xfab9,
    0xfbb9, 0xfcb9, 0xfdb9, 0xfeb9, 0xa1ba, 0xa2ba, 0xa3ba, 0xa4ba, 0xa5ba,
    0xa6ba, 0xa7ba, 0xa8ba, 0xa9ba, 0xaaba, 0xabba, 0xacba, 0xadba, 0xaeba,
    0xafba, 0xb0ba, 0xb1ba, 0xb2ba, 0xb3ba, 0xb4ba, 0xb5ba, 0xb6ba, 0xb7ba,
    0xb8ba, 0xb9ba, 0xbaba, 0xbbba, 0xbcba, 0xbdba, 0xbeba, 0xbfba, 0xc0ba,
    0xc1ba, 0xc2ba, 0xc3ba, 0xc4ba, 0xc5ba, 0xc6ba, 0xc7ba, 0xc8ba, 0xc9ba,
    0xcaba, 0xcbba, 0xccba, 0xcdba, 0xceba, 0xcfba, 0xd0ba, 0xd1ba, 0xd2ba,
    0xd3ba, 0xd4ba, 0xd5ba, 0xd6ba, 0xd7ba, 0xd8ba, 0xd9ba, 0xdaba, 0xdbba,
    0xdcba, 0xddba, 0xdeba, 0xdfba, 0xe0ba, 0xe1ba, 0xe2ba, 0xe3ba, 0xe4ba,
    0xe5ba, 0xe6ba, 0xe7ba, 0xe8ba, 0xe9ba, 0xeaba, 0xebba, 0xecba, 0xedba,
    0xeeba, 0xefba, 0xf0ba, 0xf1ba, 0xf2ba, 0xf3ba, 0xf4ba, 0xf5ba, 0xf6ba,
    0xf7ba, 0xf8ba, 0xf9ba, 0xfaba, 0xfbba, 0xfcba, 0xfdba, 0xfeba, 0xa1bb,
    0xa2bb, 0xa3bb, 0xa4bb, 0xa5bb, 0xa6bb, 0xa7bb, 0xa8bb, 0xa9bb, 0xaabb,
    0xabbb, 0xacbb, 0xadbb, 0xaebb, 0xafbb, 0xb0bb, 0xb1bb, 0xb2bb, 0xb3bb,
    0xb4bb, 0xb5bb, 0xb6bb, 0xb7bb, 0xb8bb, 0xb9bb, 0xbabb, 0xbbbb, 0xbcbb,
    0xbdbb, 0xbebb, 0xbfbb, 0xc0bb, 0xc1bb, 0xc2bb, 0xc3bb, 0xc4bb, 0xc5bb,
    0xc6bb, 0xc7bb, 0xc8bb, 0xc9bb, 0xcabb, 0xcbbb, 0xccbb, 0xcdbb, 0xcebb,
    0xcfbb, 0xd0bb, 0xd1bb, 0xd2bb, 0xd3bb, 0xd4bb, 0xd5bb, 0xd6bb, 0xd7bb,
    0xd8bb, 0xd9bb, 0xdabb, 0xdbbb, 0xdcbb, 0xddbb, 0xdebb, 0xdfbb, 0xe0bb,
    0xe1bb, 0xe2bb, 0xe3bb, 0xe4bb, 0xe5bb, 0xe6bb, 0xe7bb, 0xe8bb, 0xe9bb,
    0xeabb, 0xebbb, 0xecbb, 0xedbb, 0xeebb, 0xefbb, 0xf0bb, 0xf1bb, 0xf2bb,
    0xf3bb, 0xf4bb, 0xf5bb, 0xf6bb, 0xf7bb, 0xf8bb, 0xf9bb, 0xfabb, 0xfbbb,
    0xfcbb, 0xfdbb, 0xfebb, 0xa1bc, 0xa2bc, 0xa3bc, 0xa4bc, 0xa5bc, 0xa6bc,
    0xa7bc, 0xa8bc, 0xa9bc, 0xaabc, 0xabbc, 0xacbc, 0xadbc, 0xaebc, 0xafbc,
    0xb0bc, 0xb1bc, 0xb2bc, 0xb3bc, 0xb4bc, 0xb5bc, 0xb6bc, 0xb7bc, 0xb8bc,
    0xb9bc, 0xbabc, 0xbbbc, 0xbcbc, 0xbdbc, 0xbebc, 0xbfbc, 0xc0bc, 0xc1bc,
    0xc2bc, 0xc3bc, 0xc4bc, 0xc5bc, 0xc6bc, 0xc7bc, 0xc8bc, 0xc9bc, 0xcabc,
    0xcbbc, 0xccbc, 0xcdbc, 0xcebc, 0xcfbc, 0xd0bc, 0xd1bc, 0xd2bc, 0xd3bc,
    0xd4bc, 0xd5bc, 0xd6bc, 0xd7bc, 0xd8bc, 0xd9bc, 0xdabc, 0xdbbc, 0xdcbc,
    0xddbc, 0xdebc, 0xdfbc, 0xe0bc, 0xe1bc, 0xe2bc, 0xe3bc, 0xe4bc, 0xe5bc,
    0xe6bc, 0xe7bc, 0xe8bc, 0xe9bc, 0xeabc, 0xebbc, 0xecbc, 0xedbc, 0xeebc,
    0xefbc, 0xf0bc, 0xf1bc, 0xf2bc, 0xf3bc, 0xf4bc, 0xf5bc, 0xf6bc, 0xf7bc,
    0xf8bc, 0xf9bc, 0xfabc, 0xfbbc, 0xfcbc, 0xfdbc, 0xfebc, 0xa1bd, 0xa2bd,
    0xa3bd, 0xa4bd, 0xa5bd, 0xa6bd, 0xa7bd, 0xa8bd, 0xa9bd, 0xaabd, 0xabbd,
    0xacbd, 0xadbd, 0xaebd, 0xafbd, 0xb0bd, 0xb1bd, 0xb2bd, 0xb3bd, 0xb4bd,
    0xb5bd, 0xb6bd, 0xb7bd, 0xb8bd, 0xb9bd, 0xbabd, 0xbbbd, 0xbcbd, 0xbdbd,
    0xbebd, 0xbfbd, 0xc0bd, 0xc1bd, 0xc2bd, 0xc3bd, 0xc4bd, 0xc5bd, 0xc6bd,
    0xc7bd, 0xc8bd, 0xc9bd, 0xcabd, 0xcbbd, 0xccbd, 0xcdbd, 0xcebd, 0xcfbd,
    0xd0bd, 0xd1bd, 0xd2bd, 0xd3bd, 0xd4bd, 0xd5bd, 0xd6bd, 0xd7bd, 0xd8bd,
    0xd9bd, 0xdabd, 0xdbbd, 0xdcbd, 0xddbd, 0xdebd, 0xdfbd, 0xe0bd, 0xe1bd,
    0xe2bd, 0xe3bd, 0xe4bd, 0xe5bd, 0xe6bd, 0xe7bd, 0xe8bd, 0xe9bd, 0xeabd,
    0xebbd, 0xecbd, 0xedbd, 0xeebd, 0xefbd, 0xf0bd, 0xf1bd, 0xf2bd, 0xf3bd,
    0xf4bd, 0xf5bd, 0xf6bd, 0xf7bd, 0xf8bd, 0xf9bd, 0xfabd, 0xfbbd, 0xfcbd,
    0xfdbd, 0xfebd, 0xa1be, 0xa2be, 0xa3be, 0xa4be, 0xa5be, 0xa6be, 0xa7be,
    0xa8be, 0xa9be, 0xaabe, 0xabbe, 0xacbe, 0xadbe, 0xaebe, 0xafbe, 0xb0be,
    0xb1be, 0xb2be, 0xb3be, 0xb4be, 0xb5be, 0xb6be, 0xb7be, 0xb8be, 0xb9be,
    0xbabe, 0xbbbe, 0xbcbe, 0xbdbe, 0xbebe, 0xbfbe, 0xc0be, 0xc1be, 0xc2be,
    0xc3be, 0xc4be, 0xc5be, 0xc6be, 0xc7be, 0xc8be, 0xc9be, 0xcabe, 0xcbbe,
    0xccbe, 0xcdbe, 0xcebe, 0xcfbe, 0xd0be, 0xd1be, 0xd2be, 0xd3be, 0xd4be,
    0xd5be, 0xd6be, 0xd7be, 0xd8be, 0xd9be, 0xdabe, 0xdbbe, 0xdcbe, 0xddbe,
    0xdebe, 0xdfbe, 0xe0be, 0xe1be, 0xe2be, 0xe3be, 0xe4be, 0xe5be, 0xe6be,
    0xe7be, 0xe8be, 0xe9be, 0xeabe, 0xebbe, 0xecbe, 0xedbe, 0xeebe, 0xefbe,
    0xf0be, 0xf1be, 0xf2be, 0xf3be, 0xf4be, 0xf5be, 0xf6be, 0xf7be, 0xf8be,
    0xf9be, 0xfabe, 0xfbbe, 0xfcbe, 0xfdbe, 0xfebe, 0xa1bf, 0xa2bf, 0xa3bf,
    0xa4bf, 0xa5bf, 0xa6bf, 0xa7bf, 0xa8bf, 0xa9bf, 0xaabf, 0xabbf, 0xacbf,
    0xadbf, 0xaebf, 0xafbf, 0xb0bf, 0xb1bf, 0xb2bf, 0xb3bf, 0xb4bf, 0xb5bf,
    0xb6bf, 0xb7bf, 0xb8bf, 0xb9bf, 0xbabf, 0xbbbf, 0xbcbf, 0xbdbf, 0xbebf,
    0xbfbf, 0xc0bf, 0xc1bf, 0xc2bf, 0xc3bf, 0xc4bf, 0xc5bf, 0xc6bf, 0xc7bf,
    0xc8bf, 0xc9bf, 0xcabf, 0xcbbf, 0xccbf, 0xcdbf, 0xcebf, 0xcfbf, 0xd0bf,
    0xd1bf, 0xd2bf, 0xd3bf, 0xd4bf, 0xd5bf, 0xd6bf, 0xd7bf, 0xd8bf, 0xd9bf,
    0xdabf, 0xdbbf, 0xdcbf, 0xddbf, 0xdebf, 0xdfbf, 0xe0bf, 0xe1bf, 0xe2bf,
    0xe3bf, 0xe4bf, 0xe5bf, 0xe6bf, 0xe7bf, 0xe8bf, 0xe9bf, 0xeabf, 0xebbf,
    0xecbf, 0xedbf, 0xeebf, 0xefbf, 0xf0bf, 0xf1bf, 0xf2bf, 0xf3bf, 0xf4bf,
    0xf5bf, 0xf6bf, 0xf7bf, 0xf8bf, 0xf9bf, 0xfabf, 0xfbbf, 0xfcbf, 0xfdbf,
    0xfebf, 0xa1c0, 0xa2c0, 0xa3c0, 0xa4c0, 0xa5c0, 0xa6c0, 0xa7c0, 0xa8c0,
    0xa9c0, 0xaac0, 0xabc0, 0xacc0, 0xadc0, 0xaec0, 0xafc0, 0xb0c0, 0xb1c0,
    0xb2c0, 0xb3c0, 0xb4c0, 0xb5c0, 0xb6c0, 0xb7c0, 0xb8c0, 0xb9c0, 0xbac0,
    0xbbc0, 0xbcc0, 0xbdc0, 0xbec0, 0xbfc0, 0xc0c0, 0xc1c0, 0xc2c0, 0xc3c0,
    0xc4c0, 0xc5c0, 0xc6c0, 0xc7c0, 0xc8c0, 0xc9c0, 0xcac0, 0xcbc0, 0xccc0,
    0xcdc0, 0xcec0, 0xcfc0, 0xd0c0, 0xd1c0, 0xd2c0, 0xd3c0, 0xd4c0, 0xd5c0,
    0xd6c0, 0xd7c0, 0xd8c0, 0xd9c0, 0xdac0, 0xdbc0, 0xdcc0, 0xddc0, 0xdec0,
    0xdfc0, 0xe0c0, 0xe1c0, 0xe2c0, 0xe3c0, 0xe4c0, 0xe5c0, 0xe6c0, 0xe7c0,
    0xe8c0, 0xe9c0, 0xeac0, 0xebc0, 0xecc0, 0xedc0, 0xeec0, 0xefc0, 0xf0c0,
    0xf1c0, 0xf2c0, 0xf3c0, 0xf4c0, 0xf5c0, 0xf6c0, 0xf7c0, 0xf8c0, 0xf9c0,
    0xfac0, 0xfbc0, 0xfcc0, 0xfdc0, 0xfec0, 0xa1c1, 0xa2c1, 0xa3c1, 0xa4c1,
    0xa5c1, 0xa6c1, 0xa7c1, 0xa8c1, 0xa9c1, 0xaac1, 0xabc1, 0xacc1, 0xadc1,
    0xaec1, 0xafc1, 0xb0c1, 0xb1c1, 0xb2c1, 0xb3c1, 0xb4c1, 0xb5c1, 0xb6c1,
    0xb7c1, 0xb8c1, 0xb9c1, 0xbac1, 0xbbc1, 0xbcc1, 0xbdc1, 0xbec1, 0xbfc1,
    0xc0c1, 0xc1c1, 0xc2c1, 0xc3c1, 0xc4c1, 0xc5c1, 0xc6c1, 0xc7c1, 0xc8c1,
    0xc9c1, 0xcac1, 0xcbc1, 0xccc1, 0xcdc1, 0xcec1, 0xcfc1, 0xd0c1, 0xd1c1,
    0xd2c1, 0xd3c1, 0xd4c1, 0xd5c1, 0xd6c1, 0xd7c1, 0xd8c1, 0xd9c1, 0xdac1,
    0xdbc1, 0xdcc1, 0xddc1, 0xdec1, 0xdfc1, 0xe0c1, 0xe1c1, 0xe2c1, 0xe3c1,
    0xe4c1, 0xe5c1, 0xe6c1, 0xe7c1, 0xe8c1, 0xe9c1, 0xeac1, 0xebc1, 0xecc1,
    0xedc1, 0xeec1, 0xefc1, 0xf0c1, 0xf1c1, 0xf2c1, 0xf3c1, 0xf4c1, 0xf5c1,
    0xf6c1, 0xf7c1, 0xf8c1, 0xf9c1, 0xfac1, 0xfbc1, 0xfcc1, 0xfdc1, 0xfec1,
    0xa1c2, 0xa2c2, 0xa3c2, 0xa4c2, 0xa5c2, 0xa6c2, 0xa7c2, 0xa8c2, 0xa9c2,
    0xaac2, 0xabc2, 0xacc2, 0xadc2, 0xaec2, 0xafc2, 0xb0c2, 0xb1c2, 0xb2c2,
    0xb3c2, 0xb4c2, 0xb5c2, 0xb6c2, 0xb7c2, 0xb8c2, 0xb9c2, 0xbac2, 0xbbc2,
    0xbcc2, 0xbdc2, 0xbec2, 0xbfc2, 0xc0c2, 0xc1c2, 0xc2c2, 0xc3c2, 0xc4c2,
    0xc5c2, 0xc6c2, 0xc7c2, 0xc8c2, 0xc9c2, 0xcac2, 0xcbc2, 0xccc2, 0xcdc2,
    0xcec2, 0xcfc2, 0xd0c2, 0xd1c2, 0xd2c2, 0xd3c2, 0xd4c2, 0xd5c2, 0xd6c2,
    0xd7c2, 0xd8c2, 0xd9c2, 0xdac2, 0xdbc2, 0xdcc2, 0xddc2, 0xdec2, 0xdfc2,
    0xe0c2, 0xe1c2, 0xe2c2, 0xe3c2, 0xe4c2, 0xe5c2, 0xe6c2, 0xe7c2, 0xe8c2,
    0xe9c2, 0xeac2, 0xebc2, 0xecc2, 0xedc2, 0xeec2, 0xefc2, 0xf0c2, 0xf1c2,
    0xf2c2, 0xf3c2, 0xf4c2, 0xf5c2, 0xf6c2, 0xf7c2, 0xf8c2, 0xf9c2, 0xfac2,
    0xfbc2, 0xfcc2, 0xfdc2, 0xfec2, 0xa1c3, 0xa2c3, 0xa3c3, 0xa4c3, 0xa5c3,
    0xa6c3, 0xa7c3, 0xa8c3, 0xa9c3, 0xaac3, 0xabc3, 0xacc3, 0xadc3, 0xaec3,
    0xafc3, 0xb0c3, 0xb1c3, 0xb2c3, 0xb3c3, 0xb4c3, 0xb5c3, 0xb6c3, 0xb7c3,
    0xb8c3, 0xb9c3, 0xbac3, 0xbbc3, 0xbcc3, 0xbdc3, 0xbec3, 0xbfc3, 0xc0c3,
    0xc1c3, 0xc2c3, 0xc3c3, 0xc4c3, 0xc5c3, 0xc6c3, 0xc7c3, 0xc8c3, 0xc9c3,
    0xcac3, 0xcbc3, 0xccc3, 0xcdc3, 0xcec3, 0xcfc3, 0xd0c3, 0xd1c3, 0xd2c3,
    0xd3c3, 0xd4c3, 0xd5c3, 0xd6c3, 0xd7c3, 0xd8c3, 0xd9c3, 0xdac3, 0xdbc3,
    0xdcc3, 0xddc3, 0xdec3, 0xdfc3, 0xe0c3, 0xe1c3, 0xe2c3, 0xe3c3, 0xe4c3,
    0xe5c3, 0xe6c3, 0xe7c3, 0xe8c3, 0xe9c3, 0xeac3, 0xebc3, 0xecc3, 0xedc3,
    0xeec3, 0xefc3, 0xf0c3, 0xf1c3, 0xf2c3, 0xf3c3, 0xf4c3, 0xf5c3, 0xf6c3,
    0xf7c3, 0xf8c3, 0xf9c3, 0xfac3, 0xfbc3, 0xfcc3, 0xfdc3, 0xfec3, 0xa1c4,
    0xa2c4, 0xa3c4, 0xa4c4, 0xa5c4, 0xa6c4, 0xa7c4, 0xa8c4, 0xa9c4, 0xaac4,
    0xabc4, 0xacc4, 0xadc4, 0xaec4, 0xafc4, 0xb0c4, 0xb1c4, 0xb2c4, 0xb3c4,
    0xb4c4, 0xb5c4, 0xb6c4, 0xb7c4, 0xb8c4, 0xb9c4, 0xbac4, 0xbbc4, 0xbcc4,
    0xbdc4, 0xbec4, 0xbfc4, 0xc0c4, 0xc1c4, 0xc2c4, 0xc3c4, 0xc4c4, 0xc5c4,
    0xc6c4, 0xc7c4, 0xc8c4, 0xc9c4, 0xcac4, 0xcbc4, 0xccc4, 0xcdc4, 0xcec4,
    0xcfc4, 0xd0c4, 0xd1c4, 0xd2c4, 0xd3c4, 0xd4c4, 0xd5c4, 0xd6c4, 0xd7c4,
    0xd8c4, 0xd9c4, 0xdac4, 0xdbc4, 0xdcc4, 0xddc4, 0xdec4, 0xdfc4, 0xe0c4,
    0xe1c4, 0xe2c4, 0xe3c4, 0xe4c4, 0xe5c4, 0xe6c4, 0xe7c4, 0xe8c4, 0xe9c4,
    0xeac4, 0xebc4, 0xecc4, 0xedc4, 0xeec4, 0xefc4, 0xf0c4, 0xf1c4, 0xf2c4,
    0xf3c4, 0xf4c4, 0xf5c4, 0xf6c4, 0xf7c4, 0xf8c4, 0xf9c4, 0xfac4, 0xfbc4,
    0xfcc4, 0xfdc4, 0xfec4, 0xa1c5, 0xa2c5, 0xa3c5, 0xa4c5, 0xa5c5, 0xa6c5,
    0xa7c5, 0xa8c5, 0xa9c5, 0xaac5, 0xabc5, 0xacc5, 0xadc5, 0xaec5, 0xafc5,
    0xb0c5, 0xb1c5, 0xb2c5, 0xb3c5, 0xb4c5, 0xb5c5, 0xb6c5, 0xb7c5, 0xb8c5,
    0xb9c5, 0xbac5, 0xbbc5, 0xbcc5, 0xbdc5, 0xbec5, 0xbfc5, 0xc0c5, 0xc1c5,
    0xc2c5, 0xc3c5, 0xc4c5, 0xc5c5, 0xc6c5, 0xc7c5, 0xc8c5, 0xc9c5, 0xcac5,
    0xcbc5, 0xccc5, 0xcdc5, 0xcec5, 0xcfc5, 0xd0c5, 0xd1c5, 0xd2c5, 0xd3c5,
    0xd4c5, 0xd5c5, 0xd6c5, 0xd7c5, 0xd8c5, 0xd9c5, 0xdac5, 0xdbc5, 0xdcc5,
    0xddc5, 0xdec5, 0xdfc5, 0xe0c5, 0xe1c5, 0xe2c5, 0xe3c5, 0xe4c5, 0xe5c5,
    0xe6c5, 0xe7c5, 0xe8c5, 0xe9c5, 0xeac5, 0xebc5, 0xecc5, 0xedc5, 0xeec5,
    0xefc5, 0xf0c5, 0xf1c5, 0xf2c5, 0xf3c5, 0xf4c5, 0xf5c5, 0xf6c5, 0xf7c5,
    0xf8c5, 0xf9c5, 0xfac5, 0xfbc5, 0xfcc5, 0xfdc5, 0xfec5, 0xa1c6, 0xa2c6,
    0xa3c6, 0xa4c6, 0xa5c6, 0xa6c6, 0xa7c6, 0xa8c6, 0xa9c6, 0xaac6, 0xabc6,
    0xacc6, 0xadc6, 0xaec6, 0xafc6, 0xb0c6, 0xb1c6, 0xb2c6, 0xb3c6, 0xb4c6,
    0xb5c6, 0xb6c6, 0xb7c6, 0xb8c6, 0xb9c6, 0xbac6, 0xbbc6, 0xbcc6, 0xbdc6,
    0xbec6, 0xbfc6, 0xc0c6, 0xc1c6, 0xc2c6, 0xc3c6, 0xc4c6, 0xc5c6, 0xc6c6,
    0xc7c6, 0xc8c6, 0xc9c6, 0xcac6, 0xcbc6, 0xccc6, 0xcdc6, 0xcec6, 0xcfc6,
    0xd0c6, 0xd1c6, 0xd2c6, 0xd3c6, 0xd4c6, 0xd5c6, 0xd6c6, 0xd7c6, 0xd8c6,
    0xd9c6, 0xdac6, 0xdbc6, 0xdcc6, 0xddc6, 0xdec6, 0xdfc6, 0xe0c6, 0xe1c6,
    0xe2c6, 0xe3c6, 0xe4c6, 0xe5c6, 0xe6c6, 0xe7c6, 0xe8c6, 0xe9c6, 0xeac6,
    0xebc6, 0xecc6, 0xedc6, 0xeec6, 0xefc6, 0xf0c6, 0xf1c6, 0xf2c6, 0xf3c6,
    0xf4c6, 0xf5c6, 0xf6c6, 0xf7c6, 0xf8c6, 0xf9c6, 0xfac6, 0xfbc6, 0xfcc6,
    0xfdc6, 0xfec6, 0xa1c7, 0xa2c7, 0xa3c7, 0xa4c7, 0xa5c7, 0xa6c7, 0xa7c7,
    0xa8c7, 0xa9c7, 0xaac7, 0xabc7, 0xacc7, 0xadc7, 0xaec7, 0xafc7, 0xb0c7,
    0xb1c7, 0xb2c7, 0xb3c7, 0xb4c7, 0xb5c7, 0xb6c7, 0xb7c7, 0xb8c7, 0xb9c7,
    0xbac7, 0xbbc7, 0xbcc7, 0xbdc7, 0xbec7, 0xbfc7, 0xc0c7, 0xc1c7, 0xc2c7,
    0xc3c7, 0xc4c7, 0xc5c7, 0xc6c7, 0xc7c7, 0xc8c7, 0xc9c7, 0xcac7, 0xcbc7,
    0xccc7, 0xcdc7, 0xcec7, 0xcfc7, 0xd0c7, 0xd1c7, 0xd2c7, 0xd3c7, 0xd4c7,
    0xd5c7, 0xd6c7, 0xd7c7, 0xd8c7, 0xd9c7, 0xdac7, 0xdbc7, 0xdcc7, 0xddc7,
    0xdec7, 0xdfc7, 0xe0c7, 0xe1c7, 0xe2c7, 0xe3c7, 0xe4c7, 0xe5c7, 0xe6c7,
    0xe7c7, 0xe8c7, 0xe9c7, 0xeac7, 0xebc7, 0xecc7, 0xedc7, 0xeec7, 0xefc7,
    0xf0c7, 0xf1c7, 0xf2c7, 0xf3c7, 0xf4c7, 0xf5c7, 0xf6c7, 0xf7c7, 0xf8c7,
    0xf9c7, 0xfac7, 0xfbc7, 0xfcc7, 0xfdc7, 0xfec7, 0xa1c8, 0xa2c8, 0xa3c8,
    0xa4c8, 0xa5c8, 0xa6c8, 0xa7c8, 0xa8c8, 0xa9c8, 0xaac8, 0xabc8, 0xacc8,
    0xadc8, 0xaec8, 0xafc8, 0xb0c8, 0xb1c8, 0xb2c8, 0xb3c8, 0xb4c8, 0xb5c8,
    0xb6c8, 0xb7c8, 0xb8c8, 0xb9c8, 0xbac8, 0xbbc8, 0xbcc8, 0xbdc8, 0xbec8,
    0xbfc8, 0xc0c8, 0xc1c8, 0xc2c8, 0xc3c8, 0xc4c8, 0xc5c8, 0xc6c8, 0xc7c8,
    0xc8c8, 0xc9c8, 0xcac8, 0xcbc8, 0xccc8, 0xcdc8, 0xcec8, 0xcfc8, 0xd0c8,
    0xd1c8, 0xd2c8, 0xd3c8, 0xd4c8, 0xd5c8, 0xd6c8, 0xd7c8, 0xd8c8, 0xd9c8,
    0xdac8, 0xdbc8, 0xdcc8, 0xddc8, 0xdec8, 0xdfc8, 0xe0c8, 0xe1c8, 0xe2c8,
    0xe3c8, 0xe4c8, 0xe5c8, 0xe6c8, 0xe7c8, 0xe8c8, 0xe9c8, 0xeac8, 0xebc8,
    0xecc8, 0xedc8, 0xeec8, 0xefc8, 0xf0c8, 0xf1c8, 0xf2c8, 0xf3c8, 0xf4c8,
    0xf5c8, 0xf6c8, 0xf7c8, 0xf8c8, 0xf9c8, 0xfac8, 0xfbc8, 0xfcc8, 0xfdc8,
    0xfec8, 0xa1c9, 0xa2c9, 0xa3c9, 0xa4c9, 0xa5c9, 0xa6c9, 0xa7c9, 0xa8c9,
    0xa9c9, 0xaac9, 0xabc9, 0xacc9, 0xadc9, 0xaec9, 0xafc9, 0xb0c9, 0xb1c9,
    0xb2c9, 0xb3c9, 0xb4c9, 0xb5c9, 0xb6c9, 0xb7c9, 0xb8c9, 0xb9c9, 0xbac9,
    0xbbc9, 0xbcc9, 0xbdc9, 0xbec9, 0xbfc9, 0xc0c9, 0xc1c9, 0xc2c9, 0xc3c9,
    0xc4c9, 0xc5c9, 0xc6c9, 0xc7c9, 0xc8c9, 0xc9c9, 0xcac9, 0xcbc9, 0xccc9,
    0xcdc9, 0xcec9, 0xcfc9, 0xd0c9, 0xd1c9, 0xd2c9, 0xd3c9, 0xd4c9, 0xd5c9,
    0xd6c9, 0xd7c9, 0xd8c9, 0xd9c9, 0xdac9, 0xdbc9, 0xdcc9, 0xddc9, 0xdec9,
    0xdfc9, 0xe0c9, 0xe1c9, 0xe2c9, 0xe3c9, 0xe4c9, 0xe5c9, 0xe6c9, 0xe7c9,
    0xe8c9, 0xe9c9, 0xeac9, 0xebc9, 0xecc9, 0xedc9, 0xeec9, 0xefc9, 0xf0c9,
    0xf1c9, 0xf2c9, 0xf3c9, 0xf4c9, 0xf5c9, 0xf6c9, 0xf7c9, 0xf8c9, 0xf9c9,
    0xfac9, 0xfbc9, 0xfcc9, 0xfdc9, 0xfec9, 0xa1ca, 0xa2ca, 0xa3ca, 0xa4ca,
    0xa5ca, 0xa6ca, 0xa7ca, 0xa8ca, 0xa9ca, 0xaaca, 0xabca, 0xacca, 0xadca,
    0xaeca, 0xafca, 0xb0ca, 0xb1ca, 0xb2ca, 0xb3ca, 0xb4ca, 0xb5ca, 0xb6ca,
    0xb7ca, 0xb8ca, 0xb9ca, 0xbaca, 0xbbca, 0xbcca, 0xbdca, 0xbeca, 0xbfca,
    0xc0ca, 0xc1ca, 0xc2ca, 0xc3ca, 0xc4ca, 0xc5ca, 0xc6ca, 0xc7ca, 0xc8ca,
    0xc9ca, 0xcaca, 0xcbca, 0xccca, 0xcdca, 0xceca, 0xcfca, 0xd0ca, 0xd1ca,
    0xd2ca, 0xd3ca, 0xd4ca, 0xd5ca, 0xd6ca, 0xd7ca, 0xd8ca, 0xd9ca, 0xdaca,
    0xdbca, 0xdcca, 0xddca, 0xdeca, 0xdfca, 0xe0ca, 0xe1ca, 0xe2ca, 0xe3ca,
    0xe4ca, 0xe5ca, 0xe6ca, 0xe7ca, 0xe8ca, 0xe9ca, 0xeaca, 0xebca, 0xecca,
    0xedca, 0xeeca, 0xefca, 0xf0ca, 0xf1ca, 0xf2ca, 0xf3ca, 0xf4ca, 0xf5ca,
    0xf6ca, 0xf7ca, 0xf8ca, 0xf9ca, 0xfaca, 0xfbca, 0xfcca, 0xfdca, 0xfeca,
    0xa1cb, 0xa2cb, 0xa3cb, 0xa4cb, 0xa5cb, 0xa6cb, 0xa7cb, 0xa8cb, 0xa9cb,
    0xaacb, 0xabcb, 0xaccb, 0xadcb, 0xaecb, 0xafcb, 0xb0cb, 0xb1cb, 0xb2cb,
    0xb3cb, 0xb4cb, 0xb5cb, 0xb6cb, 0xb7cb, 0xb8cb, 0xb9cb, 0xbacb, 0xbbcb,
    0xbccb, 0xbdcb, 0xbecb, 0xbfcb, 0xc0cb, 0xc1cb, 0xc2cb, 0xc3cb, 0xc4cb,
    0xc5cb, 0xc6cb, 0xc7cb, 0xc8cb, 0xc9cb, 0xcacb, 0xcbcb, 0xcccb, 0xcdcb,
    0xcecb, 0xcfcb, 0xd0cb, 0xd1cb, 0xd2cb, 0xd3cb, 0xd4cb, 0xd5cb, 0xd6cb,
    0xd7cb, 0xd8cb, 0xd9cb, 0xdacb, 0xdbcb, 0xdccb, 0xddcb, 0xdecb, 0xdfcb,
    0xe0cb, 0xe1cb, 0xe2cb, 0xe3cb, 0xe4cb, 0xe5cb, 0xe6cb, 0xe7cb, 0xe8cb,
    0xe9cb, 0xeacb, 0xebcb, 0xeccb, 0xedcb, 0xeecb, 0xefcb, 0xf0cb, 0xf1cb,
    0xf2cb, 0xf3cb, 0xf4cb, 0xf5cb, 0xf6cb, 0xf7cb, 0xf8cb, 0xf9cb, 0xfacb,
    0xfbcb, 0xfccb, 0xfdcb, 0xfecb, 0xa1cc, 0xa2cc, 0xa3cc, 0xa4cc, 0xa5cc,
    0xa6cc, 0xa7cc, 0xa8cc, 0xa9cc, 0xaacc, 0xabcc, 0xaccc, 0xadcc, 0xaecc,
    0xafcc, 0xb0cc, 0xb1cc, 0xb2cc, 0xb3cc, 0xb4cc, 0xb5cc, 0xb6cc, 0xb7cc,
    0xb8cc, 0xb9cc, 0xbacc, 0xbbcc, 0xbccc, 0xbdcc, 0xbecc, 0xbfcc, 0xc0cc,
    0xc1cc, 0xc2cc, 0xc3cc, 0xc4cc, 0xc5cc, 0xc6cc, 0xc7cc, 0xc8cc, 0xc9cc,
    0xcacc, 0xcbcc, 0xcccc, 0xcdcc, 0xcecc, 0xcfcc, 0xd0cc, 0xd1cc, 0xd2cc,
    0xd3cc, 0xd4cc, 0xd5cc, 0xd6cc, 0xd7cc, 0xd8cc, 0xd9cc, 0xdacc, 0xdbcc,
    0xdccc, 0xddcc, 0xdecc, 0xdfcc, 0xe0cc, 0xe1cc, 0xe2cc, 0xe3cc, 0xe4cc,
    0xe5cc, 0xe6cc, 0xe7cc, 0xe8cc, 0xe9cc, 0xeacc, 0xebcc, 0xeccc, 0xedcc,
    0xeecc, 0xefcc, 0xf0cc, 0xf1cc, 0xf2cc, 0xf3cc, 0xf4cc, 0xf5cc, 0xf6cc,
    0xf7cc, 0xf8cc, 0xf9cc, 0xfacc, 0xfbcc, 0xfccc, 0xfdcc, 0xfecc, 0xa1cd,
    0xa2cd, 0xa3cd, 0xa4cd, 0xa5cd, 0xa6cd, 0xa7cd, 0xa8cd, 0xa9cd, 0xaacd,
    0xabcd, 0xaccd, 0xadcd, 0xaecd, 0xafcd, 0xb0cd, 0xb1cd, 0xb2cd, 0xb3cd,
    0xb4cd, 0xb5cd, 0xb6cd, 0xb7cd, 0xb8cd, 0xb9cd, 0xbacd, 0xbbcd, 0xbccd,
    0xbdcd, 0xbecd, 0xbfcd, 0xc0cd, 0xc1cd, 0xc2cd, 0xc3cd, 0xc4cd, 0xc5cd,
    0xc6cd, 0xc7cd, 0xc8cd, 0xc9cd, 0xcacd, 0xcbcd, 0xcccd, 0xcdcd, 0xcecd,
    0xcfcd, 0xd0cd, 0xd1cd, 0xd2cd, 0xd3cd, 0xd4cd, 0xd5cd, 0xd6cd, 0xd7cd,
    0xd8cd, 0xd9cd, 0xdacd, 0xdbcd, 0xdccd, 0xddcd, 0xdecd, 0xdfcd, 0xe0cd,
    0xe1cd, 0xe2cd, 0xe3cd, 0xe4cd, 0xe5cd, 0xe6cd, 0xe7cd, 0xe8cd, 0xe9cd,
    0xeacd, 0xebcd, 0xeccd, 0xedcd, 0xeecd, 0xefcd, 0xf0cd, 0xf1cd, 0xf2cd,
    0xf3cd, 0xf4cd, 0xf5cd, 0xf6cd, 0xf7cd, 0xf8cd, 0xf9cd, 0xfacd, 0xfbcd,
    0xfccd, 0xfdcd, 0xfecd, 0xa1ce, 0xa2ce, 0xa3ce, 0xa4ce, 0xa5ce, 0xa6ce,
    0xa7ce, 0xa8ce, 0xa9ce, 0xaace, 0xabce, 0xacce, 0xadce, 0xaece, 0xafce,
    0xb0ce, 0xb1ce, 0xb2ce, 0xb3ce, 0xb4ce, 0xb5ce, 0xb6ce, 0xb7ce, 0xb8ce,
    0xb9ce, 0xbace, 0xbbce, 0xbcce, 0xbdce, 0xbece, 0xbfce, 0xc0ce, 0xc1ce,
    0xc2ce, 0xc3ce, 0xc4ce, 0xc5ce, 0xc6ce, 0xc7ce, 0xc8ce, 0xc9ce, 0xcace,
    0xcbce, 0xccce, 0xcdce, 0xcece, 0xcfce, 0xd0ce, 0xd1ce, 0xd2ce, 0xd3ce,
    0xd4ce, 0xd5ce, 0xd6ce, 0xd7ce, 0xd8ce, 0xd9ce, 0xdace, 0xdbce, 0xdcce,
    0xddce, 0xdece, 0xdfce, 0xe0ce, 0xe1ce, 0xe2ce, 0xe3ce, 0xe4ce, 0xe5ce,
    0xe6ce, 0xe7ce, 0xe8ce, 0xe9ce, 0xeace, 0xebce, 0xecce, 0xedce, 0xeece,
    0xefce, 0xf0ce, 0xf1ce, 0xf2ce, 0xf3ce, 0xf4ce, 0xf5ce, 0xf6ce, 0xf7ce,
    0xf8ce, 0xf9ce, 0xface, 0xfbce, 0xfcce, 0xfdce, 0xfece, 0xa1cf, 0xa2cf,
    0xa3cf, 0xa4cf, 0xa5cf, 0xa6cf, 0xa7cf, 0xa8cf, 0xa9cf, 0xaacf, 0xabcf,
    0xaccf, 0xadcf, 0xaecf, 0xafcf, 0xb0cf, 0xb1cf, 0xb2cf, 0xb3cf, 0xb4cf,
    0xb5cf, 0xb6cf, 0xb7cf, 0xb8cf, 0xb9cf, 0xbacf, 0xbbcf, 0xbccf, 0xbdcf,
    0xbecf, 0xbfcf, 0xc0cf, 0xc1cf, 0xc2cf, 0xc3cf, 0xc4cf, 0xc5cf, 0xc6cf,
    0xc7cf, 0xc8cf, 0xc9cf, 0xcacf, 0xcbcf, 0xcccf, 0xcdcf, 0xcecf, 0xcfcf,
    0xd0cf, 0xd1cf, 0xd2cf, 0xd3cf, 0xd4cf, 0xd5cf, 0xd6cf, 0xd7cf, 0xd8cf,
    0xd9cf, 0xdacf, 0xdbcf, 0xdccf, 0xddcf, 0xdecf, 0xdfcf, 0xe0cf, 0xe1cf,
    0xe2cf, 0xe3cf, 0xe4cf, 0xe5cf, 0xe6cf, 0xe7cf, 0xe8cf, 0xe9cf, 0xeacf,
    0xebcf, 0xeccf, 0xedcf, 0xeecf, 0xefcf, 0xf0cf, 0xf1cf, 0xf2cf, 0xf3cf,
    0xf4cf, 0xf5cf, 0xf6cf, 0xf7cf, 0xf8cf, 0xf9cf, 0xfacf, 0xfbcf, 0xfccf,
    0xfdcf, 0xfecf, 0xa1d0, 0xa2d0, 0xa3d0, 0xa4d0, 0xa5d0, 0xa6d0, 0xa7d0,
    0xa8d0, 0xa9d0, 0xaad0, 0xabd0, 0xacd0, 0xadd0, 0xaed0, 0xafd0, 0xb0d0,
    0xb1d0, 0xb2d0, 0xb3d0, 0xb4d0, 0xb5d0, 0xb6d0, 0xb7d0, 0xb8d0, 0xb9d0,
    0xbad0, 0xbbd0, 0xbcd0, 0xbdd0, 0xbed0, 0xbfd0, 0xc0d0, 0xc1d0, 0xc2d0,
    0xc3d0, 0xc4d0, 0xc5d0, 0xc6d0, 0xc7d0, 0xc8d0, 0xc9d0, 0xcad0, 0xcbd0,
    0xccd0, 0xcdd0, 0xced0, 0xcfd0, 0xd0d0, 0xd1d0, 0xd2d0, 0xd3d0, 0xd4d0,
    0xd5d0, 0xd6d0, 0xd7d0, 0xd8d0, 0xd9d0, 0xdad0, 0xdbd0, 0xdcd0, 0xddd0,
    0xded0, 0xdfd0, 0xe0d0, 0xe1d0, 0xe2d0, 0xe3d0, 0xe4d0, 0xe5d0, 0xe6d0,
    0xe7d0, 0xe8d0, 0xe9d0, 0xead0, 0xebd0, 0xecd0, 0xedd0, 0xeed0, 0xefd0,
    0xf0d0, 0xf1d0, 0xf2d0, 0xf3d0, 0xf4d0, 0xf5d0, 0xf6d0, 0xf7d0, 0xf8d0,
    0xf9d0, 0xfad0, 0xfbd0, 0xfcd0, 0xfdd0, 0xfed0, 0xa1d1, 0xa2d1, 0xa3d1,
    0xa4d1, 0xa5d1, 0xa6d1, 0xa7d1, 0xa8d1, 0xa9d1, 0xaad1, 0xabd1, 0xacd1,
    0xadd1, 0xaed1, 0xafd1, 0xb0d1, 0xb1d1, 0xb2d1, 0xb3d1, 0xb4d1, 0xb5d1,
    0xb6d1, 0xb7d1, 0xb8d1, 0xb9d1, 0xbad1, 0xbbd1, 0xbcd1, 0xbdd1, 0xbed1,
    0xbfd1, 0xc0d1, 0xc1d1, 0xc2d1, 0xc3d1, 0xc4d1, 0xc5d1, 0xc6d1, 0xc7d1,
    0xc8d1, 0xc9d1, 0xcad1, 0xcbd1, 0xccd1, 0xcdd1, 0xced1, 0xcfd1, 0xd0d1,
    0xd1d1, 0xd2d1, 0xd3d1, 0xd4d1, 0xd5d1, 0xd6d1, 0xd7d1, 0xd8d1, 0xd9d1,
    0xdad1, 0xdbd1, 0xdcd1, 0xddd1, 0xded1, 0xdfd1, 0xe0d1, 0xe1d1, 0xe2d1,
    0xe3d1, 0xe4d1, 0xe5d1, 0xe6d1, 0xe7d1, 0xe8d1, 0xe9d1, 0xead1, 0xebd1,
    0xecd1, 0xedd1, 0xeed1, 0xefd1, 0xf0d1, 0xf1d1, 0xf2d1, 0xf3d1, 0xf4d1,
    0xf5d1, 0xf6d1, 0xf7d1, 0xf8d1, 0xf9d1, 0xfad1, 0xfbd1, 0xfcd1, 0xfdd1,
    0xfed1, 0xa1d2, 0xa2d2, 0xa3d2, 0xa4d2, 0xa5d2, 0xa6d2, 0xa7d2, 0xa8d2,
    0xa9d2, 0xaad2, 0xabd2, 0xacd2, 0xadd2, 0xaed2, 0xafd2, 0xb0d2, 0xb1d2,
    0xb2d2, 0xb3d2, 0xb4d2, 0xb5d2, 0xb6d2, 0xb7d2, 0xb8d2, 0xb9d2, 0xbad2,
    0xbbd2, 0xbcd2, 0xbdd2, 0xbed2, 0xbfd2, 0xc0d2, 0xc1d2, 0xc2d2, 0xc3d2,
    0xc4d2, 0xc5d2, 0xc6d2, 0xc7d2, 0xc8d2, 0xc9d2, 0xcad2, 0xcbd2, 0xccd2,
    0xcdd2, 0xced2, 0xcfd2, 0xd0d2, 0xd1d2, 0xd2d2, 0xd3d2, 0xd4d2, 0xd5d2,
    0xd6d2, 0xd7d2, 0xd8d2, 0xd9d2, 0xdad2, 0xdbd2, 0xdcd2, 0xddd2, 0xded2,
    0xdfd2, 0xe0d2, 0xe1d2, 0xe2d2, 0xe3d2, 0xe4d2, 0xe5d2, 0xe6d2, 0xe7d2,
    0xe8d2, 0xe9d2, 0xead2, 0xebd2, 0xecd2, 0xedd2, 0xeed2, 0xefd2, 0xf0d2,
    0xf1d2, 0xf2d2, 0xf3d2, 0xf4d2, 0xf5d2, 0xf6d2, 0xf7d2, 0xf8d2, 0xf9d2,
    0xfad2, 0xfbd2, 0xfcd2, 0xfdd2, 0xfed2, 0xa1d3, 0xa2d3, 0xa3d3, 0xa4d3,
    0xa5d3, 0xa6d3, 0xa7d3, 0xa8d3, 0xa9d3, 0xaad3, 0xabd3, 0xacd3, 0xadd3,
    0xaed3, 0xafd3, 0xb0d3, 0xb1d3, 0xb2d3, 0xb3d3, 0xb4d3, 0xb5d3, 0xb6d3,
    0xb7d3, 0xb8d3, 0xb9d3, 0xbad3, 0xbbd3, 0xbcd3, 0xbdd3, 0xbed3, 0xbfd3,
    0xc0d3, 0xc1d3, 0xc2d3, 0xc3d3, 0xc4d3, 0xc5d3, 0xc6d3, 0xc7d3, 0xc8d3,
    0xc9d3, 0xcad3, 0xcbd3, 0xccd3, 0xcdd3, 0xced3, 0xcfd3, 0xd0d3, 0xd1d3,
    0xd2d3, 0xd3d3, 0xd4d3, 0xd5d3, 0xd6d3, 0xd7d3, 0xd8d3, 0xd9d3, 0xdad3,
    0xdbd3, 0xdcd3, 0xddd3, 0xded3, 0xdfd3, 0xe0d3, 0xe1d3, 0xe2d3, 0xe3d3,
    0xe4d3, 0xe5d3, 0xe6d3, 0xe7d3, 0xe8d3, 0xe9d3, 0xead3, 0xebd3, 0xecd3,
    0xedd3, 0xeed3, 0xefd3, 0xf0d3, 0xf1d3, 0xf2d3, 0xf3d3, 0xf4d3, 0xf5d3,
    0xf6d3, 0xf7d3, 0xf8d3, 0xf9d3, 0xfad3, 0xfbd3, 0xfcd3, 0xfdd3, 0xfed3,
    0xa1d4, 0xa2d4, 0xa3d4, 0xa4d4, 0xa5d4, 0xa6d4, 0xa7d4, 0xa8d4, 0xa9d4,
    0xaad4, 0xabd4, 0xacd4, 0xadd4, 0xaed4, 0xafd4, 0xb0d4, 0xb1d4, 0xb2d4,
    0xb3d4, 0xb4d4, 0xb5d4, 0xb6d4, 0xb7d4, 0xb8d4, 0xb9d4, 0xbad4, 0xbbd4,
    0xbcd4, 0xbdd4, 0xbed4, 0xbfd4, 0xc0d4, 0xc1d4, 0xc2d4, 0xc3d4, 0xc4d4,
    0xc5d4, 0xc6d4, 0xc7d4, 0xc8d4, 0xc9d4, 0xcad4, 0xcbd4, 0xccd4, 0xcdd4,
    0xced4, 0xcfd4, 0xd0d4, 0xd1d4, 0xd2d4, 0xd3d4, 0xd4d4, 0xd5d4, 0xd6d4,
    0xd7d4, 0xd8d4, 0xd9d4, 0xdad4, 0xdbd4, 0xdcd4, 0xddd4, 0xded4, 0xdfd4,
    0xe0d4, 0xe1d4, 0xe2d4, 0xe3d4, 0xe4d4, 0xe5d4, 0xe6d4, 0xe7d4, 0xe8d4,
    0xe9d4, 0xead4, 0xebd4, 0xecd4, 0xedd4, 0xeed4, 0xefd4, 0xf0d4, 0xf1d4,
    0xf2d4, 0xf3d4, 0xf4d4, 0xf5d4, 0xf6d4, 0xf7d4, 0xf8d4, 0xf9d4, 0xfad4,
    0xfbd4, 0xfcd4, 0xfdd4, 0xfed4, 0xa1d5, 0xa2d5, 0xa3d5, 0xa4d5, 0xa5d5,
    0xa6d5, 0xa7d5, 0xa8d5, 0xa9d5, 0xaad5, 0xabd5, 0xacd5, 0xadd5, 0xaed5,
    0xafd5, 0xb0d5, 0xb1d5, 0xb2d5, 0xb3d5, 0xb4d5, 0xb5d5, 0xb6d5, 0xb7d5,
    0xb8d5, 0xb9d5, 0xbad5, 0xbbd5, 0xbcd5, 0xbdd5, 0xbed5, 0xbfd5, 0xc0d5,
    0xc1d5, 0xc2d5, 0xc3d5, 0xc4d5, 0xc5d5, 0xc6d5, 0xc7d5, 0xc8d5, 0xc9d5,
    0xcad5, 0xcbd5, 0xccd5, 0xcdd5, 0xced5, 0xcfd5, 0xd0d5, 0xd1d5, 0xd2d5,
    0xd3d5, 0xd4d5, 0xd5d5, 0xd6d5, 0xd7d5, 0xd8d5, 0xd9d5, 0xdad5, 0xdbd5,
    0xdcd5, 0xddd5, 0xded5, 0xdfd5, 0xe0d5, 0xe1d5, 0xe2d5, 0xe3d5, 0xe4d5,
    0xe5d5, 0xe6d5, 0xe7d5, 0xe8d5, 0xe9d5, 0xead5, 0xebd5, 0xecd5, 0xedd5,
    0xeed5, 0xefd5, 0xf0d5, 0xf1d5, 0xf2d5, 0xf3d5, 0xf4d5, 0xf5d5, 0xf6d5,
    0xf7d5, 0xf8d5, 0xf9d5, 0xfad5, 0xfbd5, 0xfcd5, 0xfdd5, 0xfed5, 0xa1d6,
    0xa2d6, 0xa3d6, 0xa4d6, 0xa5d6, 0xa6d6, 0xa7d6, 0xa8d6, 0xa9d6, 0xaad6,
    0xabd6, 0xacd6, 0xadd6, 0xaed6, 0xafd6, 0xb0d6, 0xb1d6, 0xb2d6, 0xb3d6,
    0xb4d6, 0xb5d6, 0xb6d6, 0xb7d6, 0xb8d6, 0xb9d6, 0xbad6, 0xbbd6, 0xbcd6,
    0xbdd6, 0xbed6, 0xbfd6, 0xc0d6, 0xc1d6, 0xc2d6, 0xc3d6, 0xc4d6, 0xc5d6,
    0xc6d6, 0xc7d6, 0xc8d6, 0xc9d6, 0xcad6, 0xcbd6, 0xccd6, 0xcdd6, 0xced6,
    0xcfd6, 0xd0d6, 0xd1d6, 0xd2d6, 0xd3d6, 0xd4d6, 0xd5d6, 0xd6d6, 0xd7d6,
    0xd8d6, 0xd9d6, 0xdad6, 0xdbd6, 0xdcd6, 0xddd6, 0xded6, 0xdfd6, 0xe0d6,
    0xe1d6, 0xe2d6, 0xe3d6, 0xe4d6, 0xe5d6, 0xe6d6, 0xe7d6, 0xe8d6, 0xe9d6,
    0xead6, 0xebd6, 0xecd6, 0xedd6, 0xeed6, 0xefd6, 0xf0d6, 0xf1d6, 0xf2d6,
    0xf3d6, 0xf4d6, 0xf5d6, 0xf6d6, 0xf7d6, 0xf8d6, 0xf9d6, 0xfad6, 0xfbd6,
    0xfcd6, 0xfdd6, 0xfed6, 0xa1d7, 0xa2d7, 0xa3d7, 0xa4d7, 0xa5d7, 0xa6d7,
    0xa7d7, 0xa8d7, 0xa9d7, 0xaad7, 0xabd7, 0xacd7, 0xadd7, 0xaed7, 0xafd7,
    0xb0d7, 0xb1d7, 0xb2d7, 0xb3d7, 0xb4d7, 0xb5d7, 0xb6d7, 0xb7d7, 0xb8d7,
    0xb9d7, 0xbad7, 0xbbd7, 0xbcd7, 0xbdd7, 0xbed7, 0xbfd7, 0xc0d7, 0xc1d7,
    0xc2d7, 0xc3d7, 0xc4d7, 0xc5d7, 0xc6d7, 0xc7d7, 0xc8d7, 0xc9d7, 0xcad7,
    0xcbd7, 0xccd7, 0xcdd7, 0xced7, 0xcfd7, 0xd0d7, 0xd1d7, 0xd2d7, 0xd3d7,
    0xd4d7, 0xd5d7, 0xd6d7, 0xd7d7, 0xd8d7, 0xd9d7, 0xdad7, 0xdbd7, 0xdcd7,
    0xddd7, 0xded7, 0xdfd7, 0xe0d7, 0xe1d7, 0xe2d7, 0xe3d7, 0xe4d7, 0xe5d7,
    0xe6d7, 0xe7d7, 0xe8d7, 0xe9d7, 0xead7, 0xebd7, 0xecd7, 0xedd7, 0xeed7,
    0xefd7, 0xf0d7, 0xf1d7, 0xf2d7, 0xf3d7, 0xf4d7, 0xf5d7, 0xf6d7, 0xf7d7,
    0xf8d7, 0xf9d7]


def readPOTfile(name, clist):
    filename = 'POT/' + name + '-c.pot'
    a = array.array('H')  # unsigned shorts
    a.fromfile(open(filename, 'rb'), os.path.getsize(filename) // a.itemsize)
    a.reverse()
    characters = []
    labels = []
    while len(a) > 0:
        sample_size = a.pop()
        label = a.pop() + a.pop() * 65536
        label = (label % 256) * 256 + label // 256
        numStrokes = a.pop()
        strokes = []
        for i in range(numStrokes):
            stroke = []
            point = [a.pop(), a.pop()]
            while point != [65535, 0]:
                stroke.append(point)
                point = [a.pop(), a.pop()]
            strokes.append(stroke)
        [a.pop(), a.pop()]  # End of character
        if label in clist:
            label = clist.index(label)
            labels.append(label)
            characters.append([torch.FloatTensor(stroke)
                               for stroke in strokes])
    return [characters, labels]


for dataset, f1, f2 in [('train', 1001, 1240), ('test', 1241, 1300)]:
    chars = []
    labels = []
    for f in range(f1, f2 + 1):
        [chars_, labels_] = readPOTfile(str(f), c3755)
        chars.extend(chars_)
        labels.extend(labels_)
    print(len(chars), len(labels))
    for c in chars:
        cc = torch.cat(c, 0)
        m = cc.min(0)[0]
        s = (cc.max(0)[0] - m).float()
        for i, stroke in enumerate(c):
            c[i] = ((stroke - m.expand_as(stroke)) /
                    s.expand_as(stroke) * 255.59).byte()
    pickle.dump([{'input': c, 'target': l} for c, l in zip(chars, labels)], open(
        'pickle/' + dataset + '.pickle', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
