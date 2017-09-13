from __future__ import absolute_import
# import numpy as np
import argparse
from . import Highlight
from . import logger
from astropy.coordinates import SkyCoord
from astropy import units as u


class Coordinates(object):

    def __init__(self, ra_deg, dec_deg):
        self.validate_coordinates(ra_deg, dec_deg)
        self.ra_deg = ra_deg
        self.dec_deg = dec_deg

        self.skobj = SkyCoord(ra=self.ra_deg * u.degree,
                              dec=self.dec_deg * u.degree,
                              frame='icrs')

    def validate_coordinates(self, ra_deg, dec_deg):
        pass

    def get_ecliptic(self):
        lon_deg = self.skobj.barycentrictrueecliptic.lon.value
        lat_deg = self.skobj.barycentrictrueecliptic.lat.value
        return lon_deg, lat_deg

    def get_galactic(self):
        l_deg = self.skobj.galactic.l.value
        b_deg = self.skobj.galactic.b.value
        return l_deg, b_deg

    def get_icrs(self):
        ra_deg = self.skobj.icrs.ra.value
        dec_deg = self.skobj.icrs.dec.value
        return ra_deg, dec_deg

class CoordinatesSex(Coordinates):

    def __init__(self, ra_sex, dec_sex):
        self.validate_coordinates(ra_sex, dec_sex)
        self.ra_sex = ra_sex
        self.dec_sex = dec_sex

        self.skobj = SkyCoord(ra=self.ra_sex,
                              dec=self.dec_sex,
                              unit=(u.hourangle, u.deg),
                              frame='icrs')


    def validate_coordinates(self, ra_sex, dec_sex):
        pass


def coco(args=None):
    """
    exposes coco to the command line
    """
    if args is None:
        parser = argparse.ArgumentParser(
            description="Convert between astronomical coordiantes")
        parser.add_argument('ra', type=float,
                            help="Right Ascension in decimal degrees (J2000).")
        parser.add_argument('dec', type=float,
                            help="Declination in decimal degrees (J2000).")
        args = parser.parse_args(args)
        args = vars(args)
    ra = args['ra']
    dec = args['dec']

    _output = print_results(ra, dec)


def coco_sex(args=None):
    """
    exposes coco to the command line
    """
    if args is None:
        parser = argparse.ArgumentParser(
            description="Convert between astronomical coordiantes")
        parser.add_argument('ra', nargs=3,
                            help="Right Ascension in decimal degrees (J2000).")
        parser.add_argument('dec', nargs=3,
                            help="Declination in decimal degrees (J2000).")
        args = parser.parse_args(args)
        args.ra = '{} {} {}'.format(*args.ra)
        args.dec = '{} {} {}'.format(*args.dec)
        args = vars(args)
    ra = args['ra']
    dec = args['dec']

    _output = print_results(ra, dec, sex=True)


def print_results(ra, dec, sex=False):
    if sex:
        coords = CoordinatesSex(ra, dec)
    else:
        coords = Coordinates(ra, dec)

    ra_deg, dec_deg = coords.get_icrs()
    lon, lat = coords.get_ecliptic()
    l, b = coords.get_galactic()

    print()
    print(Highlight.CYAN +
          "icrs     = {:.10} {:.10}".format(ra_deg, dec_deg) +
          Highlight.END)
    print(Highlight.RED +
          "ecliptic = {:.10} {:.10}".format(lon, lat) +
          Highlight.END)
    print(Highlight.BLUE +
          "galactic = {:.10} {:.10}".format(l, b) +
          Highlight.END)

    print()