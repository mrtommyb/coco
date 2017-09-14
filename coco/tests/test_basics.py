import numpy as np


def test_import():
    """Can we import tvguide successfully?"""
    import coco
    from coco import coco
    from coco import coco_sex
    from coco import Coordinates
    from coco import CoordinatesSex
    from coco import CoordinatesName

def test_coords():
    from coco import Coordinates
    from coco import CoordinatesSex
    from coco import CoordinatesName

    ra, dec = 15.0, 15.0
    c = Coordinates(ra, dec)
    assert np.allclose(c.get_icrs()[0], 15.0)
    assert np.allclose(c.get_icrs()[1], 15.0)

    ra, dec = '1 00 00', '15 00 00'
    c = CoordinatesSex(ra, dec)
    assert np.allclose(c.get_icrs()[0], 15.0)
    assert np.allclose(c.get_icrs()[1], 15.0)

    name = 'alpha cen'
    c = CoordinatesName(name)
    assert np.allclose(c.get_icrs()[0], 219.90085)
    assert np.allclose(c.get_icrs()[1], -60.83561944444)